"""One-field LogLevel overflow control; Thai text and font unchanged."""
from pathlib import Path
import UnityPy,json,hashlib,shutil
R=Path(__file__).resolve().parents[1];b=R/'local/prototype/community-merge-002';out=R/'local/prototype/community-merge-005';out.mkdir(exist_ok=False)
UnityPy.config.FALLBACK_UNITY_VERSION='2020.3.47f1';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((b/'manifest.json').read_text())
for f in m['files']:assert sha(b/f['name'])==f['probe_sha256']
name='ui-prefabs-general_assets_all.bundle';e=UnityPy.load(str(b/name));objects={o.path_id:o for o in e.objects};pid=295032210435112665;obj=objects[pid];before=obj.read_typetree();after=dict(before)
assert before['m_overflowMode']==1
after['m_overflowMode']=0
raw={o.path_id:o.get_raw_data() for o in e.objects};obj.save_typetree(after)
(out/name).write_bytes(next(iter(e.files.values())).save());reload=UnityPy.load(str(out/name));changed=[o.path_id for o in reload.objects if o.get_raw_data()!=raw[o.path_id]];assert changed==[pid]
assert next(o.read_typetree() for o in reload.objects if o.path_id==pid)==after
files=[]
for f in m['files']:
 if f['name']!=name:shutil.copyfile(b/f['name'],out/f['name'])
 files.append(dict(name=f['name'],original_sha256=f['original_sha256'],probe_sha256=sha(out/f['name'])))
report=dict(probe='community-merge-005',files=files,installed=False,runtime_status='NOT_RUN',changed_ui_object=pid,changed_fields={'m_overflowMode':{'before':1,'after':0}},strategy='Match working-label overflow mode on LogLevel caption only; retain original Thai Error option, font/material/rect/size',limits='Unverified layout hypothesis; could allow spill outside box. Other dropdowns intentionally unchanged; not release ready.')
(out/'manifest.json').write_text(json.dumps(report,indent=2));(R/'reports/community-merge-005-build.json').write_text(json.dumps(report,indent=2));print('One field / one object reload verified; font and Thai localisation preserved.')
