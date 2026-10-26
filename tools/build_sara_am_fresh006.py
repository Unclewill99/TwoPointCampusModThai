"""WO008: exclusive offline copy, independent readback and regression inventory."""
from pathlib import Path
import copy, hashlib, io, json, re, subprocess, sys
from collections import Counter
import UnityPy
from fontTools.ttLib import TTFont
R=Path(__file__).resolve().parents[1]; B=R/'local/prototype/fresh-translation-005'; P=R/'local/prototype/probe-sara-am-glyph-002'; O=R/'local/prototype/fresh-translation-006'
targets=[R/'reports/sara-am-fresh006-build.json',R/'reports/sara-am-008-screen-map.json',R/'reports/sara-am-008-preservation-before.json',R/'reports/sara-am-008-preservation-after.json']
assert not O.exists() and all(not p.exists() for p in targets)
def sha(p):
    with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def write(p,d):p.open('x',encoding='utf-8').write(json.dumps(d,ensure_ascii=False,indent=2))
protected=json.loads((R/'reports/sara-am-007-preservation-before.json').read_bytes())
for p in P.iterdir():
    if p.is_file():protected[str(p.relative_to(R.parent))]={'size':p.stat().st_size,'sha256':sha(p)}
def snapshot():return {p:{'size':(R.parent/p).stat().st_size,'sha256':sha(R.parent/p)} for p in protected}
assert snapshot()==protected;write(targets[2],protected)
bm=json.loads((B/'manifest.json').read_bytes());pm=json.loads((P/'manifest.json').read_bytes())
for root,m in [(B,bm),(P,pm)]:
    for x in m['files']:assert sha(root/x['name'])==x['probe_sha256']
O.mkdir(exist_ok=False);files=[]
for x in bm['files']:
    n=x['name'];src=(P if n=='fonts_assets_all.bundle' else B)/n
    with (O/n).open('xb') as f:f.write(src.read_bytes())
    files.append({'name':n,'original_sha256':x['original_sha256'],'probe_sha256':sha(O/n),'parent_sha256':sha(B/n),'source':str(src.relative_to(R)),'bytes':(O/n).stat().st_size})
UnityPy.config.FALLBACK_UNITY_VERSION='2020.3.47f1'
def objects(e):return {(o.assets_file.name,o.path_id,o.type.name):o.get_raw_data() for o in e.objects}
diffs={};envs={}
for x in files:
    n=x['name'];a=UnityPy.load(str(B/n));b=UnityPy.load(str(O/n));aa,bb=objects(a),objects(b);assert aa.keys()==bb.keys();changed=[k for k in aa if aa[k]!=bb[k]]
    assert sorted(k[1] for k in changed)==(sorted([7716434233879021909,-1239755799206566947]) if n=='fonts_assets_all.bundle' else [])
    diffs[n]=[{'asset':k[0],'path_id':k[1],'type':k[2],'before_sha256':hashlib.sha256(aa[k]).hexdigest(),'after_sha256':hashlib.sha256(bb[k]).hexdigest()} for k in changed];envs[n]=(a,b)
    assert sha(O/n)==sha((P if n=='fonts_assets_all.bundle' else B)/n)
a,b=envs['fonts_assets_all.bundle']
def tree(e,pid):return next(o.read_typetree() for o in e.objects if o.path_id==pid)
af,bf=tree(a,7716434233879021909),tree(b,7716434233879021909);at,bt=tree(a,-1239755799206566947),tree(b,-1239755799206566947)
old,new=bytes(af['m_FontData']),bytes(bf['m_FontData']);u=copy.deepcopy(bf);u['m_FontData']=af['m_FontData'];assert u==af
ar=at['m_FontFeatureTable']['m_LigatureSubstitutionRecords'];br=bt['m_FontFeatureTable']['m_LigatureSubstitutionRecords'];assert len(ar)==9 and len(br)==24 and br[:9]==ar
u=copy.deepcopy(bt);u['m_FontFeatureTable']['m_LigatureSubstitutionRecords']=ar;assert u==at
f,g=[TTFont(io.BytesIO(v),recalcBBoxes=False,recalcTimestamp=False) for v in [old,new]];assert len(f.getGlyphOrder())==459 and len(g.getGlyphOrder())==474
assert g.getGlyphOrder()[:459]==f.getGlyphOrder() and f.reader['cmap']==g.reader['cmap']
fl,gl=list(f['loca'].locations),list(g['loca'].locations);assert fl==gl[:460]
assert all(f.reader['glyf'][fl[i]:fl[i+1]]==g.reader['glyf'][gl[i]:gl[i+1]] for i in range(459))
assert all(g['hmtx'][n]==v for n,v in f['hmtx'].metrics.items()) and f.reader['OS/2']==g.reader['OS/2'] and f['hhea'].ascent==g['hhea'].ascent
records=[]
for o in envs['localisation_assets_localisationenglish.bundle'][1].objects:
    if o.type.name!='TextAsset':continue
    t=o.read()
    for i,s in enumerate(t.m_Script.split('[i2t]')):
        if not s:continue
        k,v=s.split('=',1);records.append({'asset':t.m_Name,'segment_index':i,'key':k,'text':v})
assert len(records)==15677
census=json.loads((R/'reports/sara-am-006-census.json').read_bytes());clusters={x['text']:x for x in pm['clusters']};pattern=re.compile('[\u0e01-\u0e2e][\u0e48-\u0e4b]\u0e33');counts=Counter();outside=[];aliases=[];mapping=[];lf=0
cmap=f.getBestCmap();seqs={tuple(x['m_ComponentGlyphIDs']):x['m_LigatureGlyphID'] for x in br[9:]}
def kind(row):
    a,k=row['asset'],row['key']
    if a.startswith('I2LS_VO'):return 'radio/announcement caption; trigger and visibility UNKNOWN'
    if a=='I2LS_Items':return 'item catalogue '+('description' if 'Description' in k else 'label')
    if a=='I2LS_UI_Settings':return 'Settings label/tooltip'
    if a=='I2LS_Characters':return 'character trait/name; spawned availability UNKNOWN'
    if a=='I2LS_Levels':return 'level dialogue/objective; trigger availability UNKNOWN'
    if a=='I2LS_Courses':return 'course/upgrade information; unlock UNKNOWN'
    if a=='I2LS_UI':return 'UI label/tooltip; inferred flow '+k.rsplit('/',1)[0]
    return a.removeprefix('I2LS_')+' text; runtime consumer UNKNOWN'
for row in records:
    text=row['text'];matches=list(pattern.finditer(text))
    for m in matches:
        counts[m.group()]+=1;lf+=int('\n' in text)
        if m.group() not in clusters:outside.append(row|{'offset':m.start()})
    gids=[f.getGlyphID(cmap[ord(c)]) if ord(c) in cmap else None for c in text]
    for i in range(len(gids)-2):
        if tuple(gids[i:i+3]) in seqs and text[i:i+3] not in clusters:aliases.append(row|{'offset':i,'sequence':gids[i:i+3]})
    if matches:mapping.append(row|{'label':'VERIFIED_CORPUS / INFERRED_SCREEN','clusters':sorted(set(m.group() for m in matches)),'kind_and_flow':kind(row),'codepoints':['U+%04X'%ord(c) for c in text],'explicit_lf':'\n' in text,'runtime_reachability':'UNKNOWN; no live navigation performed'})
assert dict(counts)=={x['text']:x['count'] for x in census['direct_base_tone_am_clusters']} and sum(counts.values())==440 and len(counts)==15 and not outside and not aliases and lf==32
for text,x in clusters.items():
    seq=tuple(f.getGlyphID(cmap[ord(c)]) for c in text);assert seqs[seq]==x['gid']
manifest={'wo':'WO-SARA-AM-008','status':'BUILD_READY','probe':O.name,'parent':B.name,'source_probe':P.name,'installed':False,'runtime_status':'NOT_RUN','text_unchanged':True,'text_ui_byte_identical_to':B.name,'fonts_bundle_byte_identical_to':P.name,'files':files,'clusters':pm['clusters'],'limits':'Real-screen runtime regression pending PM; not a production fix approval.'};write(O/'manifest.json',manifest)
check=subprocess.run([sys.executable,str(R/'tools/manage_probe.py'),'check','--probe',O.name],capture_output=True,text=True,check=True);check=json.loads(check.stdout);assert all(x['state']=='original' for x in check['files'])
installed={x['name']:sha(R.parent/'TPC_Data/StreamingAssets/aa/StandaloneWindows64'/x['name']) for x in files};assert all(installed[x['name']]==x['original_sha256'] for x in files)
after=snapshot();assert after==protected;write(targets[3],after)
write(targets[1],{'records':mapping,'record_count':len(mapping),'label':'VERIFIED stored text, key and codepoints; screen/flow INFERRED; reachability UNKNOWN','limits':'Cmap sequence scan is per stored codepoint, per record, same embedded font only; other consumer/fallback mappings, tags/segmentation/dynamic substitutions UNKNOWN.'})
write(targets[0],manifest|{'raw_object_diffs':diffs,'font_sha256':hashlib.sha256(new).hexdigest(),'checks':{'old459_glyph_bytes_equal':True,'cmap_equal':True,'old_metrics_equal':True,'glyph_count':474,'ligatures':24,'first9_unchanged':True,'tmp_other_fields_equal':True,'font_other_fields_equal':True},'census':{'records':15677,'occurrences':440,'distinct_clusters':15,'counts':dict(counts),'outside_set':outside,'same_font_non_census_sequence_matches':aliases,'lf_occurrences':lf,'cross_consumer_aliases':'UNKNOWN: stored corpus alone cannot prove runtime segmentation/font-consumer bindings'},'manager_check':check,'installed_state_hashes':installed,'protected_files_unchanged':len(protected),'source_script_sha256':sha(Path(__file__))})
print(json.dumps({'status':'BUILD_READY','records':len(records),'mapped_records':len(mapping),'occurrences':440,'protected':len(protected),'manager':check}))
