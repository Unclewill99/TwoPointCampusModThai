"""Same-slot Thai/ZWSP comparison with identical accepted English-control layout."""
import hashlib,json
from pathlib import Path
import UnityPy
ROOT=Path(__file__).resolve().parents[1];game=ROOT.parent/'TPC_Data/StreamingAssets/aa/StandaloneWindows64'
base=ROOT/'local/prototype/probe-011';bm=json.loads((base/'manifest.json').read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for f in bm['files']:
 assert sha(base/f['name'])==f['probe_sha256'];assert sha(game/f['name'])==f['original_sha256']
corpus={r['id']:r['text'] for r in json.loads((ROOT/'docs/qa/rendering-corpus.json').read_text(encoding='utf-8'))['items']}
plain=corpus['CRP-WRAP-01']*3
marked=('\u200b'.join([corpus['CRP-WRAP-02']]*3))
assert marked.replace('\u200b','')==plain
UnityPy.config.FALLBACK_UNITY_VERSION='2020.3.47f1';key='UI/Settings/Tooltips/Resolution';reports=[]
def assets(e):return {o.read().m_Name:o.read().m_Script for o in e.objects if o.type.name=='TextAsset'}
for rev,text in [('probe-012a',plain),('probe-012b',marked)]:
 out=ROOT/'local/prototype'/rev;out.mkdir(parents=True,exist_ok=True)
 name='localisation_assets_localisationenglish.bundle';env=UnityPy.load(str(base/name));before=assets(env)
 o=next(o for o in env.objects if o.type.name=='TextAsset' and o.read().m_Name=='I2LS_UI_Settings')
 d=o.read();parts=d.m_Script.split('[i2t]');ix=[i for i,p in enumerate(parts) if p.split('=',1)[0]==key];assert len(ix)==1
 assert '\n' not in text and '<' not in text and '[i2t]' not in text
 parts[ix[0]]=key+'='+text;d.m_Script='[i2t]'.join(parts);d.save()
 (out/name).write_bytes(next(iter(env.files.values())).save())
 after=assets(UnityPy.load(str(out/name)));assert set(before)==set(after)
 for a in before:
  if a!='I2LS_UI_Settings':assert before[a]==after[a]
 old=before['I2LS_UI_Settings'].split('[i2t]');new=after['I2LS_UI_Settings'].split('[i2t]')
 assert len(old)==len(new) and [i for i,(a,b) in enumerate(zip(old,new)) if a!=b]==ix
 diag={'key':key,'text':text,'synthetic':True,'repeat_count':3,'manual_LF_count':0,
 'codepoints':['U+%04X'%ord(c) for c in text],'zwsp_offsets':[i for i,c in enumerate(text) if c=='\u200b'],'status':'NOT_RUN'}
 (out/'diagnostic-map.json').write_text(json.dumps(diag,ensure_ascii=False,indent=2),encoding='utf-8')
 files=[]
 for f in bm['files']:
  if f['name']!=name:(out/f['name']).write_bytes((base/f['name']).read_bytes())
  files.append({'name':f['name'],'original_sha256':f['original_sha256'],'probe_sha256':sha(out/f['name'])})
 m={'probe':rev,'installed':False,'runtime_status':'NOT_RUN','files':files,'diagnostic_map_sha256':sha(out/'diagnostic-map.json'),
 'strategy':'Identical probe-011 font/UI bytes; same Resolution tooltip; A/B differ only in U+200B insertions.',
 'limits':'Actual bounds/font scale and line breaks must be inspected. ZWSP experiment only, no production policy.'}
 (out/'manifest.json').write_text(json.dumps(m,indent=2),encoding='utf-8');reports.append(m)
(ROOT/'reports/probe-012-build.json').write_text(json.dumps({'variants':reports,'underlying_text_equal':True,'font_UI_bytes_identical':True,'manual_LF_count':0},indent=2),encoding='utf-8')
print(json.dumps({'variants':2,'same_underlying_Thai':True,'same_font_UI':True,'installed':False}))
