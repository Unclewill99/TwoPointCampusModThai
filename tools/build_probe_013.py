"""Actual translated tooltip candidate; no synthetic bodies, no installation."""
import hashlib,json
from pathlib import Path
import UnityPy
ROOT=Path(__file__).resolve().parents[1];game=ROOT.parent/'TPC_Data/StreamingAssets/aa/StandaloneWindows64'
base=ROOT/'local/prototype/probe-011';pilotbase=ROOT/'local/prototype/probe-003';out=ROOT/'local/prototype/probe-013';out.mkdir(parents=True,exist_ok=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
bm=json.loads((base/'manifest.json').read_text())
for f in bm['files']:
 assert sha(base/f['name'])==f['probe_sha256'];assert sha(game/f['name'])==f['original_sha256']
rows=json.loads((ROOT/'local/translations/TOOLTIPS-001.th.r2.json').read_text(encoding='utf-8'))
validation=json.loads((ROOT/'reports/tooltips-001-r2-validation.json').read_text())
assert not validation['errors'] and sha(ROOT/'local/translations/TOOLTIPS-001.th.r2.json')==validation['translation_sha256']
UnityPy.config.FALLBACK_UNITY_VERSION='2020.3.47f1';name='localisation_assets_localisationenglish.bundle'
# Use actual pilot baseline, not English synthetic-control bundle.
env=UnityPy.load(str(pilotbase/name));positions={(r['asset'],r['segment_index']):r for r in rows};count=0
for o in env.objects:
 if o.type.name!='TextAsset':continue
 d=o.read();parts=d.m_Script.split('[i2t]');dirty=False
 for i,part in enumerate(parts):
  if (d.m_Name,i) not in positions:continue
  r=positions[d.m_Name,i];assert part==r['key']+'='+r['source']
  assert '\u200b' not in r['thai'];parts[i]=r['key']+'='+r['thai'];count+=1;dirty=True
 if dirty:d.m_Script='[i2t]'.join(parts);d.save()
assert count==20
(out/name).write_bytes(next(iter(env.files.values())).save())
check=UnityPy.load(str(out/name));assets={o.read().m_Name:o.read().m_Script for o in check.objects if o.type.name=='TextAsset'}
pilot=json.loads((ROOT/'local/translations/PILOT-001.th.r3.json').read_text(encoding='utf-8'))
for r in rows+pilot:assert assets[r['asset']].split('[i2t]')[r['segment_index']]==r['key']+'='+r['thai']
files=[]
for f in bm['files']:
 if f['name']!=name:(out/f['name']).write_bytes((base/f['name']).read_bytes())
 files.append({'name':f['name'],'original_sha256':f['original_sha256'],'probe_sha256':sha(out/f['name'])})
mapping=[{'id':r['id'],'key':r['key'],'thai':r['thai'],'source_sha256':r['source_sha256'],'flags':r['flags'],'runtime_status':'NOT_RUN'} for r in rows]
(out/'tooltip-map.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2),encoding='utf-8')
m={'probe':'probe-013','installed':False,'runtime_status':'NOT_RUN','files':files,'tooltip_records_reloaded':20,'pilot_records_reloaded':50,
 'translation_sha256':validation['translation_sha256'],'tooltip_map_sha256':sha(out/'tooltip-map.json'),
 'strategy':'Actual pilot r3 plus reviewed tooltip r2; probe-011 bounded experimental UI and probe-003 Thai feature fonts.',
 'limits':'All scales, shared width effects, tooltip activation and runtime token substitution need validation. No release approved.'}
(out/'manifest.json').write_text(json.dumps(m,indent=2),encoding='utf-8');(ROOT/'reports/probe-013-build.json').write_text(json.dumps(m,indent=2),encoding='utf-8')
print(json.dumps({'actual_tooltips_verified':20,'pilot_verified':50,'installed':False}))
