"""WO007 offline build/verify only. Inputs: frozen005, census and read-only
base audit/preservation snapshot. NEW exclusive outputs: glyph-002 bundles and
local/review/sara-am-007/structural-build.json + reference.html. Never installs,
launches game, rewrites corpus, or edits any earlier font/probe/cmap/ascent.
"""
from pathlib import Path
import copy,hashlib,io,json,math,base64
from fractions import Fraction
import UnityPy
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._g_l_y_f import Glyph,GlyphComponent
from fontTools.ttLib.sfnt import calcChecksum
from fontTools.pens.svgPathPen import SVGPathPen
R=Path(__file__).resolve().parents[1];BASE=R/'local/prototype/fresh-translation-005';OUT=R/'local/prototype/probe-sara-am-glyph-002';REF=R/'local/review/sara-am-007'
assert not OUT.exists() and not (REF/'structural-build.json').exists() and not (REF/'reference.html').exists()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();digest=lambda b:hashlib.sha256(b).hexdigest()
before=json.loads((R/'reports/sara-am-007-preservation-before.json').read_bytes())
def preserve():
    for p,v in before.items():assert sha(R.parent/p)==v['sha256'],p
preserve();audit=json.loads((R/'reports/sara-am-007-base-audit.json').read_bytes());census=json.loads((R/'reports/sara-am-006-census.json').read_bytes());clusters=audit['clusters']
assert clusters==sorted(x['text'] for x in census['direct_base_tone_am_clusters']) and len(clusters)==15
assert set(clusters)==set('น้ำ ซ้ำ ต่ำ ล้ำ ร่ำ ค่ำ ถ้ำ ด่ำ ฉ่ำ ล่ำ ค้ำ ย้ำ ว่ำ น่ำ ม่ำ'.split())
assert not audit['original_first_glyph_conflicts']
assert all(not x['direct_GSUB_substitutions'] and not x['GSUB_context_mentions'] and x['clearance_below_ring_bottom']>0 for x in audit['bases'].values())
UnityPy.config.FALLBACK_UNITY_VERSION='2020.3.47f1';env=UnityPy.load(str(BASE/'fonts_assets_all.bundle'));fontid=7716434233879021909;tmpid=-1239755799206566947
fo=next(o for o in env.objects if o.path_id==fontid);to=next(o for o in env.objects if o.path_id==tmpid);oldft=fo.read_typetree();oldtmp=to.read_typetree();rawfont=bytes(oldft['m_FontData']);assert digest(rawfont)=='f9855a702e9899b9cfa1e8cb7cbf36c2c7bb6fe31ee0cd6860ae61ae012155d0'
f=TTFont(io.BytesIO(rawfont),recalcBBoxes=False,recalcTimestamp=False);order=f.getGlyphOrder()[:];assert len(order)==459;cmap=f.getBestCmap();glyfraw=f.reader['glyf'];loca=list(f['loca'].locations);metrics=dict(f['hmtx'].metrics);oldcmap=f.reader['cmap'];old_hmtx=f.reader['hmtx']
ascent_before={'hhea':f['hhea'].ascent,'OS2_typo':f['OS/2'].sTypoAscender,'OS2_win':f['OS/2'].usWinAscent}
ring=f['glyf'][order[59]];am=f['glyf'][order[82]];assert am.isComposite();assert [(c.glyphName,c.getComponentInfo()[1]) for c in am.components]==[(order[78],(1,0,0,1,0,0)),(order[59],(1,0,0,1,0,0))]
entries=[];records=[];newnames=[];maxpoints=0;maxcontours=0
for i,text in enumerate(clusters):
    bcp,tcp,acp=map(ord,text);assert acp==0xe33
    bn,tn=cmap[bcp],cmap[tcp];bid,tid=f.getGlyphID(bn),f.getGlyphID(tn);bg,tg=f['glyf'][bn],f['glyf'][tn];A=metrics[bn][0];advance=A+metrics[order[82]][0]
    # Centre own tone bbox over translated ring bbox, nearest integer with
    # positive half ties upward; maximum unavoidable centre error0.5 units.
    ideal=Fraction(2*A+ring.xMin+ring.xMax-tg.xMin-tg.xMax,2)
    tx=math.floor(ideal+Fraction(1,2));ty=ring.yMax+74-tg.yMin
    ringbox=[A+ring.xMin,ring.yMin,A+ring.xMax,ring.yMax];tonebox=[tx+tg.xMin,ty+tg.yMin,tx+tg.xMax,ty+tg.yMax]
    gap=tonebox[1]-ringbox[3];centre_error=Fraction(tonebox[0]+tonebox[2]-ringbox[0]-ringbox[2],2)
    assert gap==74 and abs(centre_error)<=Fraction(1,2) and bg.yMax<ring.yMin
    name=f'saraAm007_{bcp:04X}_{tcp:04X}';newnames.append(name);gid=459+i;g=Glyph();g.numberOfContours=-1;g.components=[]
    components=[(bn,0,0),(order[82],A,0),(tn,tx,ty)]
    for n,x,y in components:
        comp=GlyphComponent();comp.glyphName=n;comp.x=x;comp.y=y;comp.flags=4;g.components.append(comp)
    g.recalcBounds(f['glyf']);coords,ends,_=g.getCoordinates(f['glyf']);maxpoints=max(maxpoints,len(coords));maxcontours=max(maxcontours,len(ends));f['glyf'][name]=g;f['hmtx'][name]=(advance,g.xMin)
    width=g.xMax-g.xMin;height=g.yMax-g.yMin;rw,rh=math.ceil(width*.03),math.ceil(height*.03)
    entries.append({'label':'VERIFIED_GEOMETRY','text':text,'codepoints':[f'U+{x:04X}' for x in [bcp,tcp,acp]],'gid':gid,'name':name,'component_ids':[bid,82,tid],'offsets':[[0,0],[A,0],[tx,ty]],'base_bbox':[bg.xMin,bg.yMin,bg.xMax,bg.yMax],'ring_bbox':ringbox,'tone_bbox':tonebox,'tone_ideal_x':str(ideal),'tone_center_error_units':float(centre_error),'gap_units':gap,'gap_at64px':gap*.064,'bbox':[g.xMin,g.yMin,g.xMax,g.yMax],'advance':advance,'lsb':g.xMin,'top':g.yMax,'ascent_excess':g.yMax-ascent_before['hhea'],'flat_points':len(coords),'flat_contours':len(ends),'atlas_estimate':{'label':'INFERRED','point30_raster':[rw,rh],'with_padding3_each_side':[rw+6,rh+6],'padded_area':(rw+6)*(rh+6),'with_extra1pixel_border_area':(rw+7)*(rh+7)}})
    records.append({'m_ComponentGlyphIDs':[bid,tid,82],'m_LigatureGlyphID':gid})
f.setGlyphOrder(order+newnames);f['maxp'].numGlyphs=474;m=f['maxp'];m.maxCompositePoints=max(m.maxCompositePoints,maxpoints);m.maxCompositeContours=max(m.maxCompositeContours,maxcontours);m.maxComponentElements=max(m.maxComponentElements,3);m.maxComponentDepth=max(m.maxComponentDepth,2)
h=f['head'];hh=f['hhea']
for x in entries:
    xmin,ymin,xmax,ymax=x['bbox'];h.xMin=min(h.xMin,xmin);h.yMin=min(h.yMin,ymin);h.xMax=max(h.xMax,xmax);h.yMax=max(h.yMax,ymax);hh.advanceWidthMax=max(hh.advanceWidthMax,x['advance']);hh.minLeftSideBearing=min(hh.minLeftSideBearing,x['lsb']);hh.minRightSideBearing=min(hh.minRightSideBearing,x['advance']-xmax);hh.xMaxExtent=max(hh.xMaxExtent,xmax)
buf=io.BytesIO();f.save(buf);newfont=buf.getvalue();nf=TTFont(io.BytesIO(newfont),checkChecksums=2,recalcBBoxes=False,recalcTimestamp=False)
assert len(nf.getGlyphOrder())==474 and nf.getGlyphOrder()[:459]==order and nf.getGlyphOrder()[459:]==newnames
nl=list(nf['loca'].locations);nr=nf.reader['glyf'];assert nl[:460]==loca
assert all(glyfraw[loca[i]:loca[i+1]]==nr[nl[i]:nl[i+1]] for i in range(459));assert nf.reader['hmtx'][:len(old_hmtx)]==old_hmtx;assert all(nf['hmtx'][n]==v for n,v in metrics.items());assert nf.reader['cmap']==oldcmap
assert all(nf.getGlyphID(name)<459 for sub in nf['cmap'].tables for name in sub.cmap.values())
assert {'hhea':nf['hhea'].ascent,'OS2_typo':nf['OS/2'].sTypoAscender,'OS2_win':nf['OS/2'].usWinAscent}==ascent_before
assert calcChecksum(newfont)==0xB1B0AFBA
for tag,ent in nf.reader.tables.items():
    data=nf.reader[tag]
    if tag=='head':data=data[:8]+bytes(4)+data[12:]
    assert calcChecksum(data)==ent.checkSum
changedtables=[tag for tag in f.reader.keys() if f.reader[tag]!=nf.reader[tag]];assert set(changedtables)<={'glyf','loca','hmtx','maxp','hhea','head','post'}
for x in entries:
    g=nf['glyf'][x['name']];assert [g.xMin,g.yMin,g.xMax,g.yMax]==x['bbox'];assert nf['hmtx'][x['name']]==(x['advance'],x['lsb']);assert [(c.glyphName,c.getComponentInfo()[1]) for c in g.components]==[(nf.getGlyphOrder()[gid],(1,0,0,1,*offset)) for gid,offset in zip(x['component_ids'],x['offsets'])]
original=oldtmp['m_FontFeatureTable']['m_LigatureSubstitutionRecords'];assert len(original)==9
assert not any(o['m_ComponentGlyphIDs'][0]==n['m_ComponentGlyphIDs'][0] for o in original for n in records)
prefix_conflicts=[]
allrecords=original+records
for i,a in enumerate(allrecords):
    for j,b in enumerate(allrecords):
        if i==j:continue
        aa,bb=a['m_ComponentGlyphIDs'],b['m_ComponentGlyphIDs']
        if len(aa)<=len(bb) and bb[:len(aa)]==aa:prefix_conflicts.append([i,j])
assert not prefix_conflicts
nt=copy.deepcopy(oldtmp);nt['m_FontFeatureTable']['m_LigatureSubstitutionRecords'].extend(records);nft=copy.deepcopy(oldft);nft['m_FontData']=list(newfont);to.save_typetree(nt);fo.save_typetree(nft);fontbundle=next(iter(env.files.values())).save()
lines=['L1: น้ำ ซ้ำ ต่ำ ล้ำ','L2: ร่ำ ค่ำ ถ้ำ ด่ำ','L3: ฉ่ำ ล่ำ ค้ำ ย้ำ','L4: ว่ำ น่ำ ม่ำ ท่ำ','L5: ตา ถี่ ทำ นำ'];diag='\n'.join(lines)
assert all(sum(line.count(s) for line in lines)==1 for s in clusters);assert 'ท่ำ' not in clusters
le=UnityPy.load(str(BASE/'localisation_assets_localisationenglish.bundle'));texts=lambda e:{o.read().m_Name:o.read().m_Script for o in e.objects if o.type.name=='TextAsset'};ltbefore=texts(le);lo=next(o for o in le.objects if o.type.name=='TextAsset' and o.read().m_Name=='I2LS_Levels');locid=lo.path_id;data=lo.read();parts=data.m_Script.split('[i2t]');assert parts[533].startswith('Levels/Freshleigh/Level_Intro_Text=');parts[533]=parts[533].split('=',1)[0]+'='+diag;data.m_Script='[i2t]'.join(parts);data.save();locbundle=next(iter(le.files.values())).save()
parent=json.loads((BASE/'manifest.json').read_bytes());OUT.mkdir(exist_ok=False)
for x in parent['files']:
    n=x['name'];b=fontbundle if n=='fonts_assets_all.bundle' else locbundle if n=='localisation_assets_localisationenglish.bundle' else (BASE/n).read_bytes();(OUT/n).open('xb').write(b)
objects=lambda e:{(o.assets_file.name,str(o.path_id),o.type.name):o.get_raw_data() for o in e.objects};diffs={}
for x in parent['files']:
    n=x['name'];a=objects(UnityPy.load(str(BASE/n)));b=objects(UnityPy.load(str(OUT/n)));assert a.keys()==b.keys();changed=[k for k in a if a[k]!=b[k]];expected=[fontid,tmpid] if n=='fonts_assets_all.bundle' else [locid] if n=='localisation_assets_localisationenglish.bundle' else [];assert sorted(int(k[1]) for k in changed)==sorted(expected)
    diffs[n]=[{'asset':k[0],'path_id':int(k[1]),'type':k[2],'before_bytes':len(a[k]),'after_bytes':len(b[k]),'before_sha256':digest(a[k]),'after_sha256':digest(b[k])} for k in changed]
    if not expected:assert sha(BASE/n)==sha(OUT/n)
re=UnityPy.load(str(OUT/'fonts_assets_all.bundle'));actual=next(o.read_typetree() for o in re.objects if o.path_id==tmpid);assert actual['m_FontFeatureTable']['m_LigatureSubstitutionRecords']==original+records;u=copy.deepcopy(actual);del u['m_FontFeatureTable']['m_LigatureSubstitutionRecords'][9:];assert u==oldtmp
actualfont=next(o.read_typetree() for o in re.objects if o.path_id==fontid);assert bytes(actualfont['m_FontData'])==newfont;u=copy.deepcopy(actualfont);u['m_FontData']=oldft['m_FontData'];assert u==oldft
aftertexts=texts(UnityPy.load(str(OUT/'localisation_assets_localisationenglish.bundle')));assert aftertexts.keys()==ltbefore.keys();changes=[]
for name in ltbefore:
    a,b=ltbefore[name].split('[i2t]'),aftertexts[name].split('[i2t]');assert len(a)==len(b);changes.extend([name,i] for i,(p,q) in enumerate(zip(a,b)) if p!=q)
assert changes==[['I2LS_Levels',533]] and aftertexts['I2LS_Levels'].split('[i2t]')[533].split('=',1)[1]==diag
widths=[];bytext={x['text']:x for x in entries}
for line in lines:
    words=line.split(': ',1)[1].split();units=0
    for word in words:
        if word in bytext:units+=bytext[word]['advance']
        else:units+=sum(metrics[cmap[ord(ch)]][0] for ch in word)
    units+=len(words)*metrics[cmap[32]][0]
    #80native px label budget from accepted menu scale; +50% uncertainty margin.
    nominal=units*.036+80;widths.append({'line':line,'Thai_and_spaces_font_units':units,'nominal_native_width_including_80px_label':nominal,'with50percent_margin':nominal*1.5,'observed_prior_blue_panel_width_native':1050,'label':'INFERRED','limitations':'Not an exact TMP container/kerning/wrapping simulation; fit is runtime UNKNOWN.'})
area=sum(x['atlas_estimate']['padded_area'] for x in entries);borderarea=sum(x['atlas_estimate']['with_extra1pixel_border_area'] for x in entries)
atlas={'label':'INFERRED_ESTIMATE','point_size':30,'padding_each_side':3,'atlas':[512,512],'new_glyph_padded_pixel_area':area,'fraction_of_atlas':area/(512*512),'with_extra1pixel_border_area':borderarea,'fraction_with_border':borderarea/(512*512),'limits':'15 appended glyphs only. Ceil(outline extent*30/1000)+2*3 padding. SDF/hinting/packing fragmentation, all existing glyph allocations and actual free space UNKNOWN. Area is not a packing guarantee.'}
penpaths={}
for x in entries:
    pen=SVGPathPen(nf.getGlyphSet());nf.getGlyphSet()[x['name']].draw(pen);penpaths[x['text']]=pen.getCommands()
enc=lambda x:base64.b64encode(x).decode('ascii');cards=[]
for x in entries:
    width=x['advance']*.064+8;svg=f'<svg width="{width}" height="100" viewBox="0 0 {width} 100"><g transform="translate(0,82) scale(.064,-.064)"><path d="{penpaths[x["text"]]}"/></g></svg>'
    cards.append(f'<section><h3>ID{x["gid"]}: {x["text"]}</h3><div class="pair"><div>{svg}<small>new outline /64px</small></div><div><span class="sample">{x["text"]}</span><small>baseline browser /64px</small></div></div><small>tone offset{x["offsets"][2]}, gap74, top{x["top"]}</small></section>')
accepted=R/'local/qa/WO-SARA-AM-001-REFERENCE/01-reference-page.png'
html=f'''<!doctype html><meta charset="utf-8"><title>WO007 cluster font evidence</title><style>@font-face{{font-family:Base;src:url(data:font/ttf;base64,{enc(rawfont)})}}@font-face{{font-family:Probe;src:url(data:font/ttf;base64,{enc(newfont)})}}body{{font:16px Arial;margin:24px;color:#111;background:#fff}}h1{{margin:8px 0}}p{{margin:8px 0;overflow-wrap:anywhere}}.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}}section{{border:1px solid #aaa;padding:10px;height:188px}}h3{{font-family:Base,Arial;font-size:20px;margin:0}}.pair{{display:flex;gap:36px;align-items:center;height:118px}}.pair>div{{display:flex;flex-direction:column;align-items:center}}.sample{{font-family:Base;font-size:64px;line-height:100px;height:100px}}small{{font-size:12px;display:block}}.old{{height:205px;overflow:hidden}}.old img{{width:1400px;max-width:none;margin-top:-155px}}</style><h1>WO007 —15 appended composite glyphs /font evidence only</h1><p>Chrome155 /CSS64px /1x. Left: exact candidate glyph outlines via SVG. Right: browser-shaped original atomic text using baseline font. No cmap or browser GSUB alias.</p><p id="ready">Loading fonts...</p><div class="grid">{''.join(cards)}</div><h2>Accepted atomic Chrome155/64px reference (original PNG at1x CSS scale)</h2><div class="old"><img src="data:image/png;base64,{enc(accepted.read_bytes())}"></div><p>Qualitative layer order/separation, not pixel identity or game evidence. Game glyph loading/atlas/clipping remain UNKNOWN.</p><script>Promise.all([document.fonts.load('64px Base','{''.join(clusters)}'),document.fonts.load('64px Probe','{''.join(clusters)}')]).then(()=>{{document.getElementById('ready').textContent='Font loaded: baseline='+document.fonts.check('64px Base','ต่ำ')+', probe='+document.fonts.check('64px Probe','ต่ำ')+'; CSS64px; glyph count474; new font SHA256 {digest(newfont)}';document.title='WO007_REFERENCE_READY';}})</script>'''
(REF/'reference.html').open('x',encoding='utf-8').write(html)
files=[x|{'parent_sha256':sha(BASE/x['name']),'probe_sha256':sha(OUT/x['name']),'parent_bytes':(BASE/x['name']).stat().st_size,'probe_bytes':(OUT/x['name']).stat().st_size} for x in parent['files']]
report={'wo':'WO-SARA-AM-007','status':'STRUCTURAL_READY_PENDING_REFERENCE','label':'VERIFIED','probe':OUT.name,'parent':BASE.name,'installed':False,'runtime_status':'NOT_RUN','files':files,'cluster_order':'ascending codepoint string, matches census set; IDs459..473','clusters':entries,'blocked_clusters':[],'new_records':records,'original_nine_ligatures':original,'ligature_count_after':24,'prefix_conflicts':prefix_conflicts,'base_audit':'reports/sara-am-007-base-audit.json','font_before_sha256':digest(rawfont),'font_after_sha256':digest(newfont),'font_bytes_before':len(rawfont),'font_bytes_after':len(newfont),'changed_font_tables':changedtables,'ascent_before':ascent_before,'ascent_after':ascent_before,'maximum_new_top':max(x['top'] for x in entries),'maximum_ascent_excess':max(x['ascent_excess'] for x in entries),'checks':{'glyph_count':474,'all459_old_glyph_slices_byte_equal':True,'old_hmtx_prefix_byte_equal':True,'old_hmtx_values_equal':True,'old_cmap_byte_equal':True,'old_loca_prefix_equal':True,'old_glyph_order_preserved':True,'new_glyphs_in_cmap':False,'all_new_components_offsets_bounds_advances_readback':True,'whole_sfnt_checksum':hex(calcChecksum(newfont)),'table_checksums_valid':True,'original_records_unchanged':True,'new_records_exact':True,'no_other_tmp_fields_changed':True,'no_other_font_fields_changed':True,'raw_object_diffs':diffs,'changed_localization':changes,'ui_bundle_byte_equal':True,'all_output_bundles_reloaded':True},'diagnostic_text':diag,'diagnostic_codepoints':[[f'U+{ord(ch):04X}' for ch in line] for line in lines],'negative_cluster':{'text':'ท่ำ','codepoints':['U+0E17','U+0E48','U+0E33'],'in_census_set':False},'width_estimates':widths,'height_estimate':{'label':'INFERRED','line_count':5,'prior_accepted_line_count':5,'largest_glyph_top_same_as_glyph001':1083,'prior_panel_height_native':342,'design':'Keep5 lines; largest ascent no higher than accepted one-glyph probe, still below existing TMP FaceInfo ascent. Actual per-line height and fit remain runtime UNKNOWN.'},'atlas_estimate':atlas,'protected_before':before,'reference':{'html':str((REF/'reference.html').relative_to(R)),'html_sha256':sha(REF/'reference.html'),'status':'PENDING_RENDER','method':'Candidate glyphs drawn directly viaSVGPathPen at64/1000 scale, baseline Unicode shaped in browser; no cmap alias or candidate GSUB change. Not game evidence.'},'limits':'Diagnostic15 census clusters only; no install/game/runtime/fix claim; no generic generation or corpus rewrite.'}
preserve();(REF/'structural-build.json').open('x',encoding='utf-8').write(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({'probe':OUT.name,'glyphs':474,'new_records':15,'font_bytes_delta':len(newfont)-len(rawfont),'max_top':report['maximum_new_top'],'atlas':atlas,'max_width_with_margin':max(x['with50percent_margin'] for x in widths)}))
