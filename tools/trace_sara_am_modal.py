"""Read-only message popup hierarchy and font references; retain read errors."""
from pathlib import Path
import json, hashlib
import UnityPy
R=Path(__file__).resolve().parents[1]
P=R.parent/'TPC_Data/StreamingAssets/aa/StandaloneWindows64'
UnityPy.config.FALLBACK_UNITY_VERSION='2020.3.47f1'
name='ui-level_assets_all.bundle'; path=P/name
env=UnityPy.load(str(path)); objects={o.path_id:o for o in env.objects}
trees={};errors=[]
for o in env.objects:
    if o.type.name not in ['GameObject','Transform','RectTransform','MonoBehaviour']:continue
    try:trees[o.path_id]=o.read_typetree()
    except Exception as ex:errors.append(dict(id=o.path_id,error=str(ex)))
def hierarchy(root):
    todo=[root];seen=set()
    while todo:
        go=todo.pop()
        if go in seen:continue
        seen.add(go)
        t=trees.get(go,{})
        for c in t.get('m_Component',[]):
            ref=c['component'];child=trees.get(ref['m_PathID'],{})
            for x in child.get('m_Children',[]):
                if x['m_FileID']==0:todo.append(trees.get(x['m_PathID'],{}).get('m_GameObject',{}).get('m_PathID'))
        yield go
roots=[]
for key, ptr in env.container.items():
    if '/Messages/' not in key or 'Popup' not in key:continue
    nodes=[]
    for go in hierarchy(ptr.path_id):
        tree=trees.get(go,{})
        comps=[]
        for c in tree.get('m_Component',[]):
            cid=c['component']['m_PathID'];t=trees.get(cid)
            if not t:comps.append(dict(id=cid,unread=True));continue
            if 'm_text' in t or objects[cid].type.name=='MonoBehaviour':
                comps.append(dict(id=cid,fields=t))
        if comps:nodes.append(dict(id=go,name=tree.get('m_Name'),components=comps))
    roots.append(dict(container=key,root=ptr.path_id,nodes=nodes))
report=dict(bundle=name,sha256=hashlib.sha256(path.read_bytes()).hexdigest(),externals=[str(x.path) for x in next(iter(env.assets)).externals],roots=roots,errors=errors,limits='Candidate popup hierarchies, not proven runtime binding. Unread objects excluded, not patched.')
(R/'reports/sara-am-popup-trace.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(dict(roots=[dict(name=x['container'],nodes=len(x['nodes'])) for x in roots],errors=len(errors))))
