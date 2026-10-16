"""Stage a visible TMP colour marker, not a layout fix. No installation."""
import copy
import hashlib
import json
from pathlib import Path
import UnityPy
ROOT=Path(__file__).resolve().parents[1]; game=ROOT.parent/'TPC_Data/StreamingAssets/aa/StandaloneWindows64'
base=ROOT/'local/prototype/probe-007-short';out=ROOT/'local/prototype/probe-009';out.mkdir(parents=True,exist_ok=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
bm=json.loads((base/'manifest.json').read_text())
for f in bm['files']:
    assert sha(base/f['name'])==f['probe_sha256'];assert sha(game/f['name'])==f['original_sha256']
UnityPy.config.FALLBACK_UNITY_VERSION='2020.3.47f1'
name='ui-prefabs-general_assets_all.bundle';env=UnityPy.load(str(game/name));by={o.path_id:o for o in env.objects}
provider=by[1244118214773079769].read_typetree();assert provider['_prefab']['m_PathID']==5202969347434510902
controller=by[5202969347434510902].read_typetree();assert controller['_text']['m_PathID']==2671690608638065206
obj=by[2671690608638065206];before=obj.read_typetree();after=copy.deepcopy(before)
after['m_fontColor']={'r':1.0,'g':0.0,'b':1.0,'a':1.0}
after['m_fontColor32']={'rgba':0xFFFF00FF}
assert before['m_enableVertexGradient']==0
raw={o.path_id:o.get_raw_data() for o in env.objects}
obj.save_typetree(after);(out/name).write_bytes(next(iter(env.files.values())).save())
check=UnityPy.load(str(out/name));rb={o.path_id:o for o in check.objects}
assert [i for i in raw if rb[i].get_raw_data()!=raw[i]]==[obj.path_id]
assert rb[obj.path_id].read_typetree()==after
files=[]
for f in bm['files']:
    (out/f['name']).write_bytes((base/f['name']).read_bytes());files.append(f)
files.append({'name':name,'original_sha256':sha(game/name),'probe_sha256':sha(out/name)})
m={'probe':'probe-009','installed':False,'runtime_status':'NOT_RUN','files':files,
   'marker':{'TMP_path_id':obj.path_id,'colour':'magenta RGB 1,0,1 alpha 1','changed_fields':['m_fontColor','m_fontColor32']},
   'limits':'Positive marker supports this serialized TMP path being consumed. Absence is inconclusive: colour may be overwritten or another prefab used. No width/wrapping conclusion.'}
(out/'manifest.json').write_text(json.dumps(m,indent=2),encoding='utf-8')
(ROOT/'reports/probe-009-build.json').write_text(json.dumps(m,indent=2),encoding='utf-8')
print(json.dumps({'UI_objects_changed':1,'layout_unchanged':True,'original_English_tooltip':True,'installed':False}))
