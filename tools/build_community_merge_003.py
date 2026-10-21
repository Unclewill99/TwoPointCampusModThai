"""One-caption Thai primary-font diagnostic; never installs."""
from pathlib import Path
import json,hashlib,shutil,copy
import UnityPy
R=Path(__file__).resolve().parents[1];base=R/'local/prototype/community-merge-002';out=R/'local/prototype/community-merge-003';out.mkdir(exist_ok=False)
UnityPy.config.FALLBACK_UNITY_VERSION='2020.3.47f1'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((base/'manifest.json').read_text())
for f in m['files']:assert sha(base/f['name'])==f['probe_sha256']
name='ui-prefabs-general_assets_all.bundle';e=UnityPy.load(str(base/name));ob={o.path_id:o for o in e.objects}
d=ob[-6663759905669087527].read_typetree();pid=d['m_CaptionText']['m_PathID'];o=ob[pid];before=o.read_typetree();after=copy.deepcopy(before)
assert before['m_fontAsset']=={'m_FileID':2,'m_PathID':1456777345258535221}
after['m_fontAsset']={'m_FileID':2,'m_PathID':-1239755799206566947}
after['m_sharedMaterial']={'m_FileID':2,'m_PathID':-4811687150972509219}
fontenv=UnityPy.load(str(base/'fonts_assets_all.bundle'));fo={x.path_id:x for x in fontenv.objects}
assert fo[-1239755799206566947].read_typetree()['m_Name']=='NotoSans_Arabic_Dynamic'
assert fo[-1239755799206566947].read_typetree()['m_Material']['m_PathID']==-4811687150972509219
assert fo[-4811687150972509219].type.name=='Material'
raw={x.path_id:x.get_raw_data() for x in e.objects};o.save_typetree(after)
(out/name).write_bytes(next(iter(e.files.values())).save())
re=UnityPy.load(str(out/name));changed=[]
for x in re.objects:
 if x.get_raw_data()!=raw[x.path_id]:changed.append(x.path_id)
assert changed==[pid]
verified=next(x.read_typetree() for x in re.objects if x.path_id==pid);assert verified==after
assert {k:v for k,v in before.items() if k not in ['m_fontAsset','m_sharedMaterial']}=={k:v for k,v in after.items() if k not in ['m_fontAsset','m_sharedMaterial']}
files=[]
for f in m['files']:
 if f['name']!=name:shutil.copyfile(base/f['name'],out/f['name'])
 files.append(dict(name=f['name'],original_sha256=f['original_sha256'],probe_sha256=sha(out/f['name'])))
report=dict(probe='community-merge-003',files=files,installed=False,runtime_status='NOT_RUN',strategy='LogLevel selected caption only: direct existing Thai dynamic font and matching material',changed_ui_object=pid,changed_fields=['m_fontAsset','m_sharedMaterial'],localisation_font_identical_to='community-merge-002',limits='Diagnostic only. Other dropdowns intentionally unchanged. Runtime cause and fix not yet established.')
(out/'manifest.json').write_text(json.dumps(report,indent=2));(R/'reports/community-merge-003-build.json').write_text(json.dumps(report,indent=2))
print('Verified one changed UI object, two fields; all other objects and font/localisation unchanged.')
