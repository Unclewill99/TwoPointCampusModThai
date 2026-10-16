"""One-field raw wrapping-mode experiment. Enum mapping remains a hypothesis."""
import copy,hashlib,json
from pathlib import Path
import UnityPy
ROOT=Path(__file__).resolve().parents[1];game=ROOT.parent/'TPC_Data/StreamingAssets/aa/StandaloneWindows64'
base=ROOT/'local/prototype/probe-007-long';out=ROOT/'local/prototype/probe-010';out.mkdir(parents=True,exist_ok=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
bm=json.loads((base/'manifest.json').read_text())
for f in bm['files']:
 assert sha(base/f['name'])==f['probe_sha256'];assert sha(game/f['name'])==f['original_sha256']
UnityPy.config.FALLBACK_UNITY_VERSION='2020.3.47f1';name='ui-prefabs-general_assets_all.bundle'
env=UnityPy.load(str(game/name));by={o.path_id:o for o in env.objects};obj=by[2671690608638065206]
before=obj.read_typetree();assert before['m_TextWrappingMode']==1
after=copy.deepcopy(before);after['m_TextWrappingMode']=0
raw={o.path_id:o.get_raw_data() for o in env.objects};obj.save_typetree(after)
(out/name).write_bytes(next(iter(env.files.values())).save())
re={o.path_id:o for o in UnityPy.load(str(out/name)).objects}
assert [i for i in raw if re[i].get_raw_data()!=raw[i]]==[obj.path_id]
assert re[obj.path_id].read_typetree()==after
files=[]
for f in bm['files']:(out/f['name']).write_bytes((base/f['name']).read_bytes());files.append(f)
files.append({'name':name,'original_sha256':sha(game/name),'probe_sha256':sha(out/name)})
m={'probe':'probe-010','installed':False,'runtime_status':'NOT_RUN','files':files,'changed_field':'m_TextWrappingMode','from_raw':1,'to_raw':0,'TMP_path_id':obj.path_id,
 'limits':'Local metadata includes TextWrappingModes and NoWrap names, but numeric mapping and precise package version not decoded. Raw 0 is an experimental candidate, not verified Normal. Original width/fitter/colour retained; long English stimulus identical to probe-007-long.'}
(out/'manifest.json').write_text(json.dumps(m,indent=2),encoding='utf-8');(ROOT/'reports/probe-010-build.json').write_text(json.dumps(m,indent=2),encoding='utf-8')
print(json.dumps({'changed_fields':1,'raw_wrapping_mode':'1 -> 0','installed':False}))
