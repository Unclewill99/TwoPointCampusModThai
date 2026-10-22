"""Read-only embedded-font and sara-am feature audit; no game input."""
from pathlib import Path
import hashlib, io, json
import UnityPy
from fontTools.ttLib import TTFont

R=Path(__file__).resolve().parents[1]
base=R/'local/prototype/fresh-translation-005'
UnityPy.config.FALLBACK_UNITY_VERSION='2020.3.47f1'
p=base/'fonts_assets_all.bundle'
env=UnityPy.load(str(p)); fonts=[]; tmp=[]
for o in env.objects:
    if o.type.name=='Font':
        t=o.read_typetree(); data=bytes(t.get('m_FontData',[]))
        if not data:continue
        font=TTFont(io.BytesIO(data)); cmap=font.getBestCmap()
        if 0x0e15 not in cmap:continue
        glyphs=font.getGlyphOrder()
        chars={f'U+{cp:04X}':dict(name=cmap.get(cp),glyph_id=font.getGlyphID(cmap[cp]) if cp in cmap else None) for cp in [0xe15,0xe48,0xe33,0xe4d,0xe32]}
        features={}
        for tag in ['GSUB','GPOS']:
            features[tag]=[x.FeatureTag for x in font[tag].table.FeatureList.FeatureRecord] if tag in font and font[tag].table.FeatureList else []
        fonts.append(dict(path_id=o.path_id,name=t.get('m_Name'),sha256=hashlib.sha256(data).hexdigest(),characters=chars,features=features))
    elif o.type.name=='MonoBehaviour':
        t=o.read_typetree()
        if 'm_FontFeatureTable' not in t:continue
        if 'Arabic_Dynamic' not in t.get('m_Name',''):continue
        tmp.append(dict(path_id=o.path_id,name=t['m_Name'],source=t.get('m_SourceFontFile'),fallbacks=t.get('m_FallbackFontAssetTable'),feature_counts={k:len(v) for k,v in t['m_FontFeatureTable'].items()},feature_records=t['m_FontFeatureTable']))
assert fonts and tmp
report=dict(candidate='fresh-translation-005',bundle_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),sequence=[f'U+{ord(c):04X}' for c in 'à¸•à¹ˆà¸³'],fonts=fonts,tmp=tmp,limits='Serialized records only. No runtime consumption, actual modal font binding, GSUB application or root cause established. No text or glyph modifications.')
full=R/'local/review/sara-am-001/font-audit-full.json'
full.parent.mkdir(parents=True,exist_ok=True)
full.write_text(json.dumps(report,indent=2),encoding='utf-8')
summary={**report,'tmp':[{k:v for k,v in x.items() if k!='feature_records'} for x in tmp],'full_records_local':str(full.relative_to(R))}
(R/'reports/sara-am-font-audit.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps(dict(fonts=fonts,tmp=[{k:v for k,v in x.items() if k!='feature_records'} for x in tmp])))
