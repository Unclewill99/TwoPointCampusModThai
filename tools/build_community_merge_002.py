"""Build corrected community draft; local only, no installation."""
from pathlib import Path
from zipfile import ZipFile
from collections import Counter
import json,hashlib,re,shutil
import UnityPy
ROOT=Path(__file__).resolve().parents[1]
UnityPy.config.FALLBACK_UNITY_VERSION='2020.3.47f1'
rows=json.loads((ROOT/'local/imports/community-ai-v1/merged-draft.json').read_text(encoding='utf-8'))
with ZipFile(r'C:/Users/udomp/Downloads/Two Point Campus MOD Thai AI-1-MODV1-0-1742896937.zip') as z:
 env=UnityPy.load(z.read(next(n for n in z.namelist() if n.endswith('/localisation_assets_localisationenglish.bundle'))))
 assets={o.read().m_Name:o.read().m_Script.split('[i2t]') for o in env.objects if o.type.name=='TextAsset'}
fixes=[]
for row in rows:
 if 'FALLBACK' not in row['status']:continue
 k,v=assets[row['asset']][row['segment_index']].split('=',1)
 assert k==row['key']
 if 'QUARANTINED' in row['status']:
  assert '<color=สีเขียว>' in v
  v=v.replace('<color=สีเขียว>','<color=green>')
 else:
  same=[p.split('=',1)[1] for p in assets[row['asset']] if p.startswith(k+'=')]
  assert len(same)==2 and len(set(same))==1
 assert Counter(re.findall(r'\{[^{}]+\}|<[^<>]+>',v))==Counter(re.findall(r'\{[^{}]+\}|<[^<>]+>',row['source']))
 row.update(thai=v,status='IMPORTED_STRUCTURAL_FIX_UNREVIEWED',provenance='community-ai-v1-corrected')
 fixes.append({'id':row['id'],'resolution':'Restore original color attribute' if 'DamageMultiplier' in k else 'Duplicate positions verified; both imported values identical'})
assert len(fixes)==5
out=ROOT/'local/prototype/community-merge-002';out.mkdir(exist_ok=False)
base=ROOT/'local/prototype/probe-013';name='localisation_assets_localisationenglish.bundle'
env=UnityPy.load(str(base/name));positions={(r['asset'],r['segment_index']):r for r in rows};count=0
for o in env.objects:
 if o.type.name!='TextAsset':continue
 a=o.read();parts=a.m_Script.split('[i2t]');dirty=False
 for i,p in enumerate(parts):
  row=positions.get((a.m_Name,i))
  if row is None:continue
  assert p.split('=',1)[0]==row['key']
  parts[i]=row['key']+'='+row['thai'];count+=1;dirty=True
 if dirty:a.m_Script='[i2t]'.join(parts);a.save()
assert count==15677
(out/name).write_bytes(next(iter(env.files.values())).save())
check=UnityPy.load(str(out/name));loaded={o.read().m_Name:o.read().m_Script.split('[i2t]') for o in check.objects if o.type.name=='TextAsset'}
for row in rows:assert loaded[row['asset']][row['segment_index']]==row['key']+'='+row['thai']
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
files=[]
for f in json.loads((base/'manifest.json').read_text())['files']:
 if f['name']!=name:shutil.copyfile(base/f['name'],out/f['name'])
 files.append(dict(name=f['name'],original_sha256=f['original_sha256'],probe_sha256=sha(out/f['name'])))
(ROOT/'local/imports/community-ai-v1/merged-r2.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
m=dict(probe='community-merge-002',files=files,records_reloaded=count,fixes=fixes,installed=False,runtime_status='NOT_RUN',font_ui_baseline='probe-013 byte identical',limits='Imported language unreviewed; experimental UI/shaping limitations remain; no release approval')
(out/'manifest.json').write_text(json.dumps(m,indent=2),encoding='utf-8')
(ROOT/'reports/community-merge-002-build.json').write_text(json.dumps(m,indent=2),encoding='utf-8')
print('Five fallbacks resolved; 15677 reload comparisons passed; candidate not installed.')
