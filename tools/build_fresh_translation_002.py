"""Build full Claude draft on accepted rendering baseline; no installation."""
from pathlib import Path
import json,hashlib,shutil
import UnityPy
R=Path(__file__).resolve().parents[1];base=R/'local/prototype/community-merge-006';out=R/'local/prototype/fresh-translation-002';out.mkdir(exist_ok=False)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
validation=R/'reports/claude-full-retranslation-001-validation.json';v=json.loads(validation.read_text(encoding='utf-8'));assert not v['errors'] and v['records']==15677
path=R/'local/translations/CLAUDE-FULL-RETRANSLATION-001/all-records.json';rows=json.loads(path.read_text(encoding='utf-8'));positions={(x['asset'],x['segment_index']):x for x in rows};assert len(positions)==15677
m=json.loads((base/'manifest.json').read_text())
for f in m['files']:assert sha(base/f['name'])==f['probe_sha256']
UnityPy.config.FALLBACK_UNITY_VERSION='2020.3.47f1';name='localisation_assets_localisationenglish.bundle';e=UnityPy.load(str(base/name));n=0
for o in e.objects:
 if o.type.name!='TextAsset':continue
 a=o.read();parts=a.m_Script.split('[i2t]');dirty=False
 for i,p in enumerate(parts):
  row=positions.get((a.m_Name,i))
  if row is None:continue
  assert p.split('=',1)[0]==row['key'];parts[i]=row['key']+'='+row['thai'];dirty=True;n+=1
 if dirty:a.m_Script='[i2t]'.join(parts);a.save()
assert n==15677
(out/name).write_bytes(next(iter(e.files.values())).save());reload=UnityPy.load(str(out/name));assets={o.read().m_Name:o.read().m_Script.split('[i2t]') for o in reload.objects if o.type.name=='TextAsset'}
for row in rows:assert assets[row['asset']][row['segment_index']]==row['key']+'='+row['thai']
for row in rows:
 if row['asset']=='I2LS_Fonts':assert row['thai']==row['source']
files=[]
for f in m['files']:
 if f['name']!=name:shutil.copyfile(base/f['name'],out/f['name'])
 files.append(dict(name=f['name'],original_sha256=f['original_sha256'],probe_sha256=sha(out/f['name'])))
report=dict(probe='fresh-translation-002',files=files,installed=False,runtime_status='NOT_RUN',records_reloaded=15677,translated=12716,keep_as_source=2961,translation_sha256=sha(path),validation_sha256=sha(validation),archive_sha256=v['archive_sha256'],font_ui_identical_to='community-merge-006',language_review='PENDING',limits='Full newly submitted corpus integrated, not linguistically approved. Glossary212 pending, inconsistent terminology, plural/source anomalies, wrapping and BUG-THAI-003 remain. No release approval.')
(out/'manifest.json').write_text(json.dumps(report,indent=2));(R/'reports/fresh-translation-002-build.json').write_text(json.dumps(report,indent=2));print('15677 exact reload checks passed; font/UI identical to merge-006. NOT_RUN.')
