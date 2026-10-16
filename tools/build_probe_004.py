"""Inject explicitly mapped synthetic diagnostics; preserve translation baselines."""
import hashlib
import json
from pathlib import Path
import UnityPy
ROOT=Path(__file__).resolve().parents[1]
base=ROOT/'local/prototype/probe-003'; out=ROOT/'local/prototype/probe-004'
out.mkdir(parents=True,exist_ok=True)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
bm=json.loads((base/'manifest.json').read_text())
for f in bm['files']:
    assert sha(base/f['name'])==f['probe_sha256']
    assert sha(ROOT.parent/'TPC_Data/StreamingAssets/aa/StandaloneWindows64'/f['name'])==f['original_sha256']
corpus=json.loads((ROOT/'docs/qa/rendering-corpus.json').read_text(encoding='utf-8'))
cases={r['id']:r for r in corpus['items']}
# Short subsets keep diagnostic labels usable; every exact input is in the map.
specs=[
 ('UI/Settings/CameraPanSensitivity','CRP-VOWEL-02','ปิ ปี ปึ ปื ฝี ฟิ ปั ฟั','Controls: camera pan'),
 ('UI/Settings/CameraPitchSensitivity','CRP-STACK-01','ที่นี่ ปิ้ง ฟื้น กลิ่น ขี้ ดื่ม','Controls: camera pitch'),
 ('UI/Settings/CameraRotateSensitivity','CRP-DESC-01',cases['CRP-DESC-01']['text'],'Controls: camera rotate'),
 ('UI/Settings/CameraZoomSensitivity','CRP-DESC-02',cases['CRP-DESC-02']['text'],'Controls: camera zoom'),
 ('UI/Settings/AudioLanuuage','CRP-AM-01','น้ำ ถ้ำ ต้มยำ ลำคลอง','Game: Audio Language label'),
 ('UI/Settings/GameAutosaveFreq','CRP-AM-02',cases['CRP-AM-02']['text'],'Game: Game Autosave label; malformed diagnostic'),
 ('UI/Settings/CareerAutosaveFreq','CRP-AM-03',cases['CRP-AM-03']['text'],'Game: Career Autosave label; decomposed diagnostic'),
 ('UI/Settings/Language','CRP-STACK-02','พ่อ แม่ ช้า น่า ป้า กู้','Game: Language label'),
 ('UI/Settings/Tooltips/Resolution','CRP-WRAP-01',cases['CRP-WRAP-01']['text'],'Video: hover Resolution'),
 ('UI/Settings/Tooltips/FullScreenMode','CRP-WRAP-02',cases['CRP-WRAP-02']['text'],'Video: hover Fullscreen Mode'),
 ('UI/Settings/Tooltips/Vsync','CRP-WRAP-03',cases['CRP-WRAP-03']['text'],'Video: hover VSync'),
 ('UI/Settings/Tooltips/AntialiasingMode','CRP-MIX-01',cases['CRP-MIX-01']['text'],'Video: hover Antialiasing Mode'),
]
UnityPy.config.FALLBACK_UNITY_VERSION='2020.3.47f1'
name='localisation_assets_localisationenglish.bundle'
env=UnityPy.load(str(base/name))
obj=next(o for o in env.objects if o.type.name=='TextAsset' and o.read().m_Name=='I2LS_UI_Settings')
d=obj.read(); parts=d.m_Script.split('[i2t]'); mapping=[]
for key,case,text,location in specs:
    matches=[i for i,p in enumerate(parts) if p.split('=',1)[0]==key]
    assert len(matches)==1,(key,matches)
    i=matches[0]; assert '[i2t]' not in text
    parts[i]=key+'='+text
    mapping.append({'key':key,'asset':'I2LS_UI_Settings','segment_index':i,'case_id':case,
      'text':text,'codepoints':['U+%04X'%ord(c) for c in text],
      'zwsp_offsets':[n for n,c in enumerate(text) if c=='\u200b'],
      'location_hint':location,'status':'NOT_RUN','synthetic':True,
      'scope':'Short subset' if text!=cases[case]['text'] else 'Exact corpus text'})
d.m_Script='[i2t]'.join(parts);d.save()
(out/name).write_bytes(next(iter(env.files.values())).save())
(out/'fonts_assets_all.bundle').write_bytes((base/'fonts_assets_all.bundle').read_bytes())
check=UnityPy.load(str(out/name))
text=next(o.read().m_Script for o in check.objects if o.type.name=='TextAsset' and o.read().m_Name=='I2LS_UI_Settings')
for r in mapping: assert text.split('[i2t]')[r['segment_index']]==r['key']+'='+r['text']
# Verify only the 12 intended segments changed; all other TextAssets match base.
def assets(e): return {o.read().m_Name:o.read().m_Script for o in e.objects if o.type.name=='TextAsset'}
a=assets(UnityPy.load(str(base/name))); b=assets(check)
assert set(a)==set(b)
for k in a:
    if k!='I2LS_UI_Settings': assert a[k]==b[k]
old=a['I2LS_UI_Settings'].split('[i2t]'); new=b['I2LS_UI_Settings'].split('[i2t]')
assert len(old)==len(new)
assert [i for i,(x,y) in enumerate(zip(old,new)) if x!=y]==sorted(r['segment_index'] for r in mapping)
(out/'diagnostic-map.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2),encoding='utf-8')
m={'probe':'probe-004','installed':False,'runtime_status':'NOT_RUN','synthetic_diagnostic_cases':len(mapping),
 'strategy':'probe-003 font bytes unchanged; replace 12 Settings label/tooltip segments with synthetic inputs.',
 'diagnostic_map_sha256':sha(out/'diagnostic-map.json'),
 'limits':['UI slots and tooltip activation must be verified in game','Narrow labels do not establish paragraph wrapping','Different tooltip containers confound strict ZWSP A/B comparisons','Malformed inputs are observational, not required to autocorrect'],
 'files':[{'name':f['name'],'original_sha256':f['original_sha256'],'probe_sha256':sha(out/f['name'])} for f in bm['files']]}
(out/'manifest.json').write_text(json.dumps(m,indent=2),encoding='utf-8')
(ROOT/'reports/probe-004-build.json').write_text(json.dumps(m,indent=2),encoding='utf-8')
print(json.dumps({'cases_reloaded':len(mapping),'font_identical_to_probe003':True,'only_intended_segments_changed':True,'installed':False}))
