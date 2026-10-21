"""Apply observed overflow mitigation to Settings selected captions only; no installation."""
from pathlib import Path
import json,hashlib,shutil
import UnityPy
R=Path(__file__).resolve().parents[1];base=R/'local/prototype/community-merge-002';out=R/'local/prototype/community-merge-006';out.mkdir(exist_ok=True);assert not any(out.iterdir())
UnityPy.config.FALLBACK_UNITY_VERSION='2020.3.47f1';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((base/'manifest.json').read_text())
for f in m['files']:assert sha(base/f['name'])==f['probe_sha256']
name='ui-prefabs-general_assets_all.bundle';e=UnityPy.load(str(base/name));ob={o.path_id:o for o in e.objects};raw={o.path_id:o.get_raw_data() for o in e.objects};changes=[];expected={}
def rd(ref):return ob[ref['m_PathID']].read_typetree() if ref and ref['m_FileID']==0 and ref['m_PathID'] in ob else None
for obj in e.objects:
 if obj.type.name!='MonoBehaviour':continue
 try:t=obj.read_typetree()
 except:continue
 if 'm_CaptionText' not in t:continue
 g=rd(t['m_GameObject']);names=[g['m_Name']]
 tr=next((rd(c['component']) for c in g['m_Component'] if rd(c['component']) and 'm_Father' in rd(c['component'])),None)
 for i in range(12):
  if not tr:break
  tr=rd(tr.get('m_Father'))
  if tr:names.append(rd(tr['m_GameObject'])['m_Name'])
 assert 'GameplayContainer' in names or 'VideoContainer' in names
 pid=t['m_CaptionText']['m_PathID'];o=ob[pid];a=o.read_typetree();previous=a['m_overflowMode'];assert previous in [1,3]
 a['m_overflowMode']=0;o.save_typetree(a);expected[pid]=a;changes.append({'caption_id':pid,'control':names[2],'container':'GameplayContainer' if 'GameplayContainer' in names else 'VideoContainer','field':'m_overflowMode','before':previous,'after':0})
assert len(changes)==len(expected)==19
(out/name).write_bytes(next(iter(e.files.values())).save());reload=UnityPy.load(str(out/name));actual=[]
for o in reload.objects:
 if o.get_raw_data()!=raw[o.path_id]:actual.append(o.path_id);assert o.read_typetree()==expected[o.path_id]
assert set(actual)==set(expected)
files=[]
for f in m['files']:
 if f['name']!=name:shutil.copyfile(base/f['name'],out/f['name'])
 files.append(dict(name=f['name'],original_sha256=f['original_sha256'],probe_sha256=sha(out/f['name'])))
report=dict(probe='community-merge-006',files=files,installed=False,runtime_status='NOT_RUN',changes=changes,strategy='Settings selected-caption overflow mitigation only, based on accepted WO-DROPDOWN-003',limits='Only LogLevel Error tested previously. Other captions/long values and item lists unverified; possible overflow. Hidden rows not force-enabled. No release approval.')
(out/'manifest.json').write_text(json.dumps(report,indent=2));(R/'reports/community-merge-006-build.json').write_text(json.dumps(report,indent=2));print('19 Settings captions, one field each; all other objects/font/Thai text unchanged; reload passed.')
