"""Integrate fresh translations over retained trial baseline; not a fully retranslated build."""
from pathlib import Path
from collections import Counter
import json,hashlib,shutil,re
import UnityPy
R=Path(__file__).resolve().parents[1];base=R/'local/prototype/community-merge-006';out=R/'local/prototype/fresh-translation-001';out.mkdir(exist_ok=False)
UnityPy.config.FALLBACK_UNITY_VERSION='2020.3.47f1';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rows=json.loads((R/'local/retranslation/master.json').read_text(encoding='utf-8'));fresh=[x for x in rows if x['status']=='FRESH_TRANSLATED_DRAFT'];assert len(fresh)==190
positions={(x['asset'],x['segment_index']):x for x in fresh};name='localisation_assets_localisationenglish.bundle';env=UnityPy.load(str(base/name));before={o.path_id:o.get_raw_data() for o in env.objects};n=0
for o in env.objects:
 if o.type.name!='TextAsset':continue
 a=o.read();parts=a.m_Script.split('[i2t]');dirty=False
 for i,p in enumerate(parts):
  row=positions.get((a.m_Name,i))
  if row is None:continue
  assert p.split('=',1)[0]==row['key'];parts[i]=row['key']+'='+row['thai'];dirty=True;n+=1
 if dirty:a.m_Script='[i2t]'.join(parts);a.save()
assert n==190
(out/name).write_bytes(next(iter(env.files.values())).save());reload=UnityPy.load(str(out/name));assets={o.read().m_Name:o.read().m_Script.split('[i2t]') for o in reload.objects if o.type.name=='TextAsset'}
for row in fresh:assert assets[row['asset']][row['segment_index']]==row['key']+'='+row['thai']
for values in assets.values():
 for value in values:assert not any(s in value for s in ['ไม่เมาไม่แปล','โรมานอฟสกี้','จัดทำและแจกฟรีโดย'])
# Verify all non-fresh source positions are preserved from the previous trial.
bassets={o.read().m_Name:o.read().m_Script.split('[i2t]') for o in UnityPy.load(str(base/name)).objects if o.type.name=='TextAsset'}
for row in rows:
 if (row['asset'],row['segment_index']) not in positions:assert assets[row['asset']][row['segment_index']]==bassets[row['asset']][row['segment_index']]
m=json.loads((base/'manifest.json').read_text());files=[]
for f in m['files']:
 assert sha(base/f['name'])==f['probe_sha256']
 if f['name']!=name:shutil.copyfile(base/f['name'],out/f['name'])
 files.append(dict(name=f['name'],original_sha256=f['original_sha256'],probe_sha256=sha(out/f['name'])))
report=dict(probe='fresh-translation-001',files=files,installed=False,runtime_status='NOT_RUN',fresh_records=190,pending_fresh_records=len(rows)-190,remaining_text='Previous imported trial translations retained temporarily; not freshly translated or approved',font_ui_identical_to='community-merge-006',promo_records_replaced=3,limits='Fresh draft, no independent linguistic/runtime approval. BUG-THAI-002/003 remain OPEN. Not fully retranslated; no release approval.')
(out/'manifest.json').write_text(json.dumps(report,indent=2));(R/'reports/fresh-translation-001-build.json').write_text(json.dumps(report,indent=2))
(R/'reports/fresh-retranslation-progress.json').write_text(json.dumps({'total':len(rows),'fresh_draft':190,'pending':len(rows)-190,'runtime_tested_fresh':0,'independently_reviewed_fresh':0,'scope':'Full fresh translation authorized, including previous project70; machine/font identifiers retain exact technical values as appropriate','candidate':'fresh-translation-001','promo_replaced':3},indent=2))
print('Integrated190 fresh records;15487 await fresh translation. UI/fonts and all other values preserved. Promo scan passed.')
