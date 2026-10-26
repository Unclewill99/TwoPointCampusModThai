"""WO007 read-only base/GSUB/anchor audit and preservation snapshot.
Inputs:005,census,prior protected files,glyph-001. New outputs (exclusive):
reports/sara-am-007-base-audit.json,preservation-before.json and local audit XML.
Never edits a font, bundle, text, installation or earlier probe.
"""
from pathlib import Path
import json,hashlib,io
import UnityPy
from fontTools.ttLib import TTFont
R=Path(__file__).resolve().parents[1];OUT=R/'local/review/sara-am-007'
assert not OUT.exists();OUT.mkdir(exist_ok=False)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
prior=json.loads((R/'reports/sara-am-glyph-001-build.json').read_bytes())['protected_before']
paths=[R.parent/p for p in prior]+sorted(p for p in (R/'local/prototype/probe-sara-am-glyph-001').iterdir() if p.is_file())
protected={str(p.relative_to(R.parent)):{'size':p.stat().st_size,'sha256':sha(p)} for p in paths};assert len(protected)==25
assert all(protected[p]['sha256']==v['sha256'] for p,v in prior.items())
(R/'reports/sara-am-007-preservation-before.json').open('x').write(json.dumps(protected,indent=2))
UnityPy.config.FALLBACK_UNITY_VERSION='2020.3.47f1';e=UnityPy.load(str(R/'local/prototype/fresh-translation-005/fonts_assets_all.bundle'))
font=TTFont(io.BytesIO(bytes(next(o for o in e.objects if o.path_id==7716434233879021909).read_typetree()['m_FontData'])))
t=next(o for o in e.objects if o.path_id==-1239755799206566947).read_typetree();census=json.loads((R/'reports/sara-am-006-census.json').read_bytes());clusters=sorted(x['text'] for x in census['direct_base_tone_am_clusters']);names={font.getBestCmap()[ord(s[0])] for s in clusters};base_by_name={}
for name in sorted(names):
    gid=font.getGlyphID(name);g=font['glyf'][name]
    base_by_name[name]={'gid':gid,'codepoints':[f'U+{cp:04X}' for cp,n in font.getBestCmap().items() if n==name],'bbox':[g.xMin,g.yMin,g.xMax,g.yMax],'hmtx':list(font['hmtx'][name]),'clearance_below_ring_bottom':608-g.yMax,'serialized_mark_to_base_anchors':[x for x in t['m_FontFeatureTable']['m_MarkToBaseAdjustmentRecords'] if x['m_BaseGlyphID']==gid and x['m_MarkGlyphID'] in [42,47,59]],'direct_GSUB_substitutions':[],'GSUB_context_mentions':[]}
def visit(obj,path,lookup):
    if isinstance(obj,list):
        for i,x in enumerate(obj):visit(x,path+f'[{i}]',lookup)
    elif hasattr(obj,'__dict__'):
        if hasattr(obj,'glyphs'):
            for n in set(obj.glyphs)&names:base_by_name[n]['GSUB_context_mentions'].append({'lookup':lookup,'path':path,'coverage':True})
        if hasattr(obj,'classDefs'):
            for n in names:
                base_by_name[n]['GSUB_context_mentions'].append({'lookup':lookup,'path':path,'class':obj.classDefs.get(n,0),'explicit_member':n in obj.classDefs})
        for k,v in vars(obj).items():
            if k not in ['mapping','alternates','ligatures','classDefs','glyphs']:visit(v,path+'.'+k,lookup)
for i,l in enumerate(font['GSUB'].table.LookupList.Lookup):
    for j,s in enumerate(l.SubTable):
        st=s.ExtSubTable if l.LookupType==7 else s;typ=s.ExtensionLookupType if l.LookupType==7 else l.LookupType
        for k in ['mapping','alternates','ligatures']:
            mapping=getattr(st,k,{})
            for n in names&set(mapping):base_by_name[n]['direct_GSUB_substitutions'].append({'lookup':i,'type':typ,'field':k,'value':str(mapping[n])})
        visit(st,f'Lookup[{i}].Subtable[{j}]',i)
font.saveXML(str(OUT/'gsub-audit.ttx'),tables=['GSUB'])
records=t['m_FontFeatureTable']['m_LigatureSubstitutionRecords'];newids={x['gid'] for x in base_by_name.values()}
conflicts=[x for x in records if x['m_ComponentGlyphIDs'][0] in newids]
report={'wo':'WO-SARA-AM-007','label':'VERIFIED_STATIC_AUDIT','clusters':clusters,'deterministic_glyph_order':'ascending atomic codepoint string (base then tone)','bases':base_by_name,'original_ligatures':records,'original_first_glyph_conflicts':conflicts,'GSUB_types':[{ 'lookup':i,'type':x.LookupType} for i,x in enumerate(font['GSUB'].table.LookupList.Lookup)],'gsub_xml':str((OUT/'gsub-audit.ttx').relative_to(R)),'limits':'Direct base substitution and contextual references distinguished. Actual browser/TMP variant selection remains UNKNOWN; inspect any mentions before deciding.'}
(R/'reports/sara-am-007-base-audit.json').open('x',encoding='utf-8').write(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({'bases':{k:{'gid':v['gid'],'clearance':v['clearance_below_ring_bottom'],'direct':v['direct_GSUB_substitutions'],'context':v['GSUB_context_mentions']} for k,v in base_by_name.items()},'ligature_conflicts':conflicts,'protected_files':25}))
