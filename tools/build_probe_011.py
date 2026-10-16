"""Test child text width ownership, preserving Normal wrapping and content fitter."""
import copy,hashlib,json
from pathlib import Path
import UnityPy
ROOT=Path(__file__).resolve().parents[1];game=ROOT.parent/'TPC_Data/StreamingAssets/aa/StandaloneWindows64'
base=ROOT/'local/prototype/probe-007-long';out=ROOT/'local/prototype/probe-011';out.mkdir(parents=True,exist_ok=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
bm=json.loads((base/'manifest.json').read_text())
for f in bm['files']:
 assert sha(base/f['name'])==f['probe_sha256'];assert sha(game/f['name'])==f['original_sha256']
UnityPy.config.FALLBACK_UNITY_VERSION='2020.3.47f1';name='ui-prefabs-general_assets_all.bundle'
env=UnityPy.load(str(game/name));by={o.path_id:o for o in env.objects}
tmp=by[2671690608638065206].read_typetree();assert tmp['m_TextWrappingMode']==1
rect=by[3218277146759428662].read_typetree();group=by[2617668728378194486].read_typetree()
assert rect['m_GameObject']==tmp['m_GameObject']
assert group['m_ChildControlWidth']==1
raw={o.path_id:o.get_raw_data() for o in env.objects}
r=copy.deepcopy(rect);r['m_SizeDelta']['x']=800.0
g=copy.deepcopy(group);g['m_ChildControlWidth']=0
by[3218277146759428662].save_typetree(r);by[2617668728378194486].save_typetree(g)
(out/name).write_bytes(next(iter(env.files.values())).save())
rb={o.path_id:o for o in UnityPy.load(str(out/name)).objects}
assert {i for i in raw if rb[i].get_raw_data()!=raw[i]}=={3218277146759428662,2617668728378194486}
assert rb[3218277146759428662].read_typetree()==r and rb[2617668728378194486].read_typetree()==g
files=[]
for f in bm['files']:(out/f['name']).write_bytes((base/f['name']).read_bytes());files.append(f)
files.append({'name':name,'original_sha256':sha(game/name),'probe_sha256':sha(out/name)})
m={'probe':'probe-011','installed':False,'runtime_status':'NOT_RUN','files':files,
 'strategy':'Text child rect width 800 plus parent layout ChildControlWidth=0. Original Normal mode, fitter, custom wrapper and other fields unchanged.',
 'requested_text_width_units':800,'changes':[{'id':3218277146759428662,'field':'m_SizeDelta.x','before':rect['m_SizeDelta']['x'],'after':800},{'id':2617668728378194486,'field':'m_ChildControlWidth','before':1,'after':0}],
 'limits':'Paired constraint hypothesis, not single-factor enum trial. Runtime custom logic may override either property. Shared tooltip affects other users.'}
(out/'manifest.json').write_text(json.dumps(m,indent=2),encoding='utf-8');(ROOT/'reports/probe-011-build.json').write_text(json.dumps(m,indent=2),encoding='utf-8')
print(json.dumps({'UI_objects_changed':2,'wrapping_Normal_preserved':True,'installed':False}))
