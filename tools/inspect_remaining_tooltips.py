"""Read-only serialized context search for tooltip coverage gaps."""
import hashlib
import json
from pathlib import Path
import UnityPy

ROOT = Path(__file__).resolve().parents[1]
KEYS = ('QualityPresets', 'AnimationSkinningQuality', 'RenderScale')
UnityPy.config.FALLBACK_UNITY_VERSION = '2020.3.47f1'

def strings(value, path=''):
    if isinstance(value, dict):
        for key, child in value.items():
            yield from strings(child, f'{path}/{key}')
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from strings(child, f'{path}/{index}')
    elif isinstance(value, str):
        yield path, value

result = {'scope': 'Original general UI prefab bundle; recursive serialized string search',
          'matches': [], 'read_errors': [],
          'limits': 'Static references do not prove runtime activation, visibility conditions or absence elsewhere. No game or asset writes.'}
bundle = ROOT.parent / 'TPC_Data/StreamingAssets/aa/StandaloneWindows64/ui-prefabs-general_assets_all.bundle'
result['sha256'] = hashlib.sha256(bundle.read_bytes()).hexdigest()
env = UnityPy.load(str(bundle))
objects = {obj.path_id: obj for obj in env.objects}
def read_tree(path_id):
    obj = objects.get(path_id)
    if obj is None:
        return {}
    try:
        return obj.read_typetree()
    except Exception as error:
        result['read_errors'].append({'path_id': path_id, 'error': str(error)})
        return {}

def hierarchy(owner_id):
    chain, visited = [], set()
    while owner_id and owner_id not in visited:
        visited.add(owner_id)
        owner = read_tree(owner_id)
        chain.append({'id': owner_id, 'name': owner.get('m_Name'), 'active': owner.get('m_IsActive')})
        components = [read_tree(c['component']['m_PathID']) for c in owner.get('m_Component', [])]
        transform = next((c for c in components if 'm_Father' in c), {})
        parent = read_tree(transform.get('m_Father', {}).get('m_PathID'))
        owner_id = parent.get('m_GameObject', {}).get('m_PathID')
    return chain

for obj in env.objects:
    if obj.type.name not in ('MonoBehaviour', 'GameObject'):
        continue
    try:
        tree = obj.read_typetree()
    except Exception as error:
        result['read_errors'].append({'path_id': obj.path_id, 'error': str(error)})
        continue
    matches = [{'field': path, 'value': value} for path, value in strings(tree)
               if any(key.casefold() in value.casefold() for key in KEYS)]
    if not matches:
        continue
    owner = tree.get('m_GameObject', {}).get('m_PathID')
    owner_obj = objects.get(owner)
    owner_name = owner_obj.read_typetree().get('m_Name') if owner_obj else tree.get('m_Name')
    owner_id = obj.path_id if obj.type.name == 'GameObject' else owner
    components = []
    for component in read_tree(owner_id).get('m_Component', []):
        component_id = component['component']['m_PathID']
        config = read_tree(component_id)
        components.append({'id': component_id, 'type': objects[component_id].type.name,
                           'script': config.get('m_Script'), 'fields': sorted(config)})
    result['matches'].append({'path_id': obj.path_id, 'type': obj.type.name,
                              'owner_name': owner_name, 'matches': matches,
                              'hierarchy': hierarchy(owner_id), 'owner_components': components})
(ROOT / 'reports/remaining-tooltip-context.json').write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print(json.dumps({'matches': len(result['matches']), 'read_errors': len(result['read_errors'])}))
