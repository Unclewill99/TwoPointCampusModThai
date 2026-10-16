"""Fixed-width tooltip layout experiment; preserves TMP settings and English stimulus."""
import copy
import hashlib
import json
from pathlib import Path
import UnityPy
ROOT=Path(__file__).resolve().parents[1];game=ROOT.parent/'TPC_Data/StreamingAssets/aa/StandaloneWindows64'
base=ROOT/'local/prototype/probe-007-long';out=ROOT/'local/prototype/probe-008';out.mkdir(parents=True,exist_ok=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
bm=json.loads((base/'manifest.json').read_text())
for f in bm['files']:
    assert sha(base/f['name'])==f['probe_sha256'];assert sha(game/f['name'])==f['original_sha256']
UnityPy.config.FALLBACK_UNITY_VERSION='2020.3.47f1'
name='ui-prefabs-general_assets_all.bundle';env=UnityPy.load(str(game/name));by={o.path_id:o for o in env.objects}
provider=by[1244118214773079769].read_typetree()
assert provider['_prefab']=={'m_FileID':0,'m_PathID':5202969347434510902}
controller=by[5202969347434510902].read_typetree();layout=by[1537959580418341430].read_typetree()
assert controller['_layoutGroup']['m_PathID']==1537959580418341430
assert layout['_contentSizeFitter']['m_PathID']==-8613258678337963466
fitter=by[-8613258678337963466].read_typetree()
go=by[fitter['m_GameObject']['m_PathID']].read()
rect=next(c.component.deref() for c in go.m_Component if c.component.deref().type.name=='RectTransform')
before={o.path_id:o.get_raw_data() for o in env.objects}
t=rect.read_typetree();oldrect=copy.deepcopy(t)
t['m_SizeDelta']['x']=800.0;rect.save_typetree(t)
f=copy.deepcopy(fitter);f['m_HorizontalFit']=0;by[-8613258678337963466].save_typetree(f)
(out/name).write_bytes(next(iter(env.files.values())).save())
re=UnityPy.load(str(out/name));rb={o.path_id:o for o in re.objects}
changes=[i for i in before if rb[i].get_raw_data()!=before[i]]
assert set(changes)=={rect.path_id,-8613258678337963466}
assert rb[rect.path_id].read_typetree()==t
assert rb[-8613258678337963466].read_typetree()==f
files=[]
for item in bm['files']:
    (out/item['name']).write_bytes((base/item['name']).read_bytes());files.append(item)
files.append({'name':name,'original_sha256':sha(game/name),'probe_sha256':sha(out/name)})
evidence={'resolution_provider':provider,'tooltip_controller':controller,'layout_wrapper':layout,
 'fitter_before':fitter,'fitter_after':f,'rect_id':rect.path_id,'rect_before':oldrect,'rect_after':t,
 'changed_object_ids':changes,'limits':'Static references and serialized edits only; custom runtime layout may override width. TMP wrapping mode unchanged.'}
(ROOT/'reports/probe-008-layout-trace.json').write_text(json.dumps(evidence,indent=2),encoding='utf-8')
m={'probe':'probe-008','installed':False,'runtime_status':'NOT_RUN','files':files,
 'requested_content_width_unity_units':800,'changed_ui_objects':changes,
 'strategy':'probe-007-long stimulus unchanged; disable horizontal fit on traced arrowLeft content and request width 800. No TMP edits.',
 'limits':'Shared tooltip prefab affects other users too; width and wrapping must be observed, not inferred. Three bundles require restoration.'}
(out/'manifest.json').write_text(json.dumps(m,indent=2),encoding='utf-8')
(ROOT/'reports/probe-008-build.json').write_text(json.dumps(m,indent=2),encoding='utf-8')
print(json.dumps({'bundles':len(files),'ui_objects_changed':len(changes),'TMP_unchanged':True,'installed':False}))
