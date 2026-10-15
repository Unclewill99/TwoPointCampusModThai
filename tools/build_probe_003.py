"""Controlled font-feature injection experiment; local assets only, never installs."""
import base64
import copy
import hashlib
import html
import io
import json
from pathlib import Path
import UnityPy
from fontTools.ttLib import TTFont

ROOT=Path(__file__).resolve().parents[1]
base=ROOT/'local/prototype/probe-002'
out=ROOT/'local/prototype/probe-003'
out.mkdir(parents=True,exist_ok=True)
museum=ROOT.parent.parent/'Two Point Museum/TPM_Data/StreamingAssets/aa/StandaloneWindows64'
game=ROOT.parent/'TPC_Data/StreamingAssets/aa/StandaloneWindows64'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
bm=json.loads((base/'manifest.json').read_text())
for f in bm['files']:
    assert sha(base/f['name'])==f['probe_sha256']
    assert sha(game/f['name'])==f['original_sha256'], 'Restore originals before building'
UnityPy.config.FALLBACK_UNITY_VERSION='6000.0.63f1'
env=UnityPy.load(str(museum/'fonts_assets_notosans_thai.bundle'))
source=next(o.read_typetree() for o in env.objects if o.type.name=='MonoBehaviour' and o.read_typetree().get('m_Name')=='NotoSans_Thai')
source_features=source['m_FontFeatureTable']
UnityPy.config.FALLBACK_UNITY_VERSION='2020.3.47f1'
name='fonts_assets_all.bundle'
env=UnityPy.load(str(base/name))
obj=next(o for o in env.objects if o.type.name=='MonoBehaviour' and o.read_typetree().get('m_Name')=='NotoSans_Arabic_Dynamic')
before=obj.read_typetree(); after=copy.deepcopy(before)
assert before['m_FaceInfo']['m_PointSize']==source['m_FaceInfo']['m_PointSize']==30
assert set(source_features)==set(before['m_FontFeatureTable'])
after['m_FontFeatureTable']=copy.deepcopy(source_features)
obj.save_typetree(after)
font_obj=next(o for o in env.objects if o.type.name=='Font' and o.read_typetree().get('m_Name')=='NotoSansArabic-Regular')
font_data=bytes(font_obj.read_typetree()['m_FontData'])
font=TTFont(io.BytesIO(font_data)); glyphs=font.getGlyphOrder()
for records in source_features.values():
    for record in records:
        for k,v in record.items():
            if k.endswith('GlyphID'): assert 0<=v<len(glyphs)
            if k.endswith('GlyphIDs'): assert all(0<=n<len(glyphs) for n in v)
# Legacy family name may include weight while TMP uses the typographic family.
assert font['head'].unitsPerEm==source['m_FaceInfo']['m_UnitsPerEM']
# Validate embedded bytes are identical to the actual Museum source TTF.
UnityPy.config.FALLBACK_UNITY_VERSION='6000.0.63f1'
font_env=UnityPy.load(str(museum/'fonts_assets_notosansthai-medium.bundle'))
assert font_data==bytes(next(o.read_typetree()['m_FontData'] for o in font_env.objects if o.type.name=='Font'))
UnityPy.config.FALLBACK_UNITY_VERSION='2020.3.47f1'
(out/name).write_bytes(next(iter(env.files.values())).save())
# Strictly preserve localisation bytes: no new translation, corpus or mapping changes.
locname='localisation_assets_localisationenglish.bundle'
(out/locname).write_bytes((base/locname).read_bytes())
reloaded=UnityPy.load(str(out/name))
verified=next(o.read_typetree() for o in reloaded.objects if o.type.name=='MonoBehaviour' and o.path_id==obj.path_id)
assert verified['m_FontFeatureTable']==source_features
assert {k:v for k,v in verified.items() if k!='m_FontFeatureTable'}=={k:v for k,v in before.items() if k!='m_FontFeatureTable'}
m={'probe':'probe-003','installed':False,'runtime_status':'NOT_RUN',
   'strategy':'probe-002 plus Museum Thai font feature records in reused dynamic TMP slot; no localisation or other TMP field changes.',
   'feature_counts':{k:len(v) for k,v in source_features.items()},
   'matching_font_sha256':hashlib.sha256(font_data).hexdigest(),'matching_point_size':30,
   'feature_glyph_ids_in_range':True,'localisation_identical_to_probe_002':True,
   'limits':['Serialized feature records reload, but runtime consumption is unverified','Missing or dynamically substituted glyph variants may still prevent correct shaping','Reference browser rendering must be inspected; generated HTML alone proves no visual result'],
   'files':[{'name':f['name'],'original_sha256':f['original_sha256'],'probe_sha256':sha(out/f['name'])} for f in bm['files']]}
(out/'manifest.json').write_text(json.dumps(m,indent=2),encoding='utf-8')
(ROOT/'reports/probe-003-build.json').write_text(json.dumps(m,indent=2),encoding='utf-8')
# Self-contained browser reference: normal browser OpenType shaping, same embedded TTF.
corpus=json.loads((ROOT/'docs/qa/rendering-corpus.json').read_text(encoding='utf-8'))
cases=[{'id':'BUG-THAI-001','text':'ความถี่ ถี่ ที่นี่ พื้นที่ ปิ้ง ฟื้นฟู น้ำ ถ้ำ'}]+corpus['items']
sections=[]
for r in cases:
    cp=' '.join('U+%04X'%ord(c) for c in r['text'])
    sections.append('<section><h2>'+html.escape(r['id'])+'</h2><div class="sample">'+html.escape(r['text'])+'</div><details><summary>Code points</summary><code>'+cp+'</code></details></section>')
page='''<!doctype html><meta charset="utf-8"><title>Thai same-font reference</title><style>
@font-face{font-family:ProbeThai;src:url(data:font/ttf;base64,'''+base64.b64encode(font_data).decode()+''') format('truetype');font-weight:500}
body{font-family:Arial,sans-serif;margin:32px;background:#faf7ef;color:#111}section{border-top:1px solid #bbb;padding:14px 0}.sample{font-family:ProbeThai;font-weight:500;font-size:48px;line-height:2.2;font-feature-settings:"mark" 1,"mkmk" 1;white-space:pre-wrap;max-width:1000px}h2{font-size:16px}code{overflow-wrap:anywhere}
</style><h1>Same-font Thai shaping reference</h1><p>Local reference only. Confirm document.fonts.check and inspect screenshots. This browser output is a comparison target, not proof of Campus behavior. Corpus cases are synthetic; angle-bracket tags and placeholders below are intentionally literal. Not a game import.</p>'''+''.join(sections)
(out/'same-font-reference.html').write_text(page,encoding='utf-8')
print(json.dumps({'probe':'probe-003','feature_counts':m['feature_counts'],'unchanged_localisation':True,'installed':False,'reference_cases':len(cases)}))
