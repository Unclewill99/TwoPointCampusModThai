"""Trace original prefab providers and build metadata without modifying game assets."""
import hashlib
import json
import struct
from pathlib import Path
import UnityPy

ROOT = Path(__file__).resolve().parents[1]
GAME = ROOT.parent / 'TPC_Data'
UnityPy.config.FALLBACK_UNITY_VERSION = '2020.3.47f1'
bundles = GAME / 'StreamingAssets/aa/StandaloneWindows64'
ui_path = bundles / 'ui-prefabs-general_assets_all.bundle'
script_path = bundles / '041ed57f62d7d6540bf750de21a4130d_monoscripts.bundle'
env = UnityPy.load(str(ui_path))
objects = {obj.path_id: obj for obj in env.objects}
scripts_env = UnityPy.load(str(script_path))
script_assets = {asset.name for asset in scripts_env.assets}
ui_asset = next(iter(env.assets))
assert Path(str(ui_asset.externals[0].path)).name in script_assets
scripts = {obj.path_id: obj.read_typetree() for obj in scripts_env.objects if obj.type.name == 'MonoScript'}
errors = []
trees = {}
for obj in env.objects:
    if obj.type.name not in ('GameObject', 'RectTransform', 'Transform', 'MonoBehaviour'):
        continue
    try:
        trees[obj.path_id] = obj.read_typetree()
    except Exception as error:
        errors.append({'path_id': obj.path_id, 'error': str(error)})

def script_name(tree):
    ref = tree.get('m_Script', {})
    if ref.get('m_FileID') != 1:
        return None
    script = scripts.get(ref.get('m_PathID'), {})
    return '.'.join(filter(None, [script.get('m_Namespace'), script.get('m_ClassName')]))

def descendants(go_id):
    pending, seen = [go_id], set()
    while pending:
        current = pending.pop()
        if current in seen:
            continue
        seen.add(current)
        yield current
        for component in trees.get(current, {}).get('m_Component', []):
            tree = trees.get(component['component']['m_PathID'], {})
            for child in tree.get('m_Children', []):
                pending.append(trees.get(child['m_PathID'], {}).get('m_GameObject', {}).get('m_PathID'))

def references(value, path=''):
    if isinstance(value, dict):
        if value.get('m_FileID') == 0 and value.get('m_PathID'):
            yield path, value['m_PathID']
        else:
            for key, child in value.items():
                yield from references(child, f'{path}/{key}')
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from references(child, f'{path}/{index}')

targets = {'QualityPresets': -2354921750532096295,
           'RenderScale': -5379194925153222951,
           'AnimationSkinningQuality': -2261707471542190375}
rows = []
related_classes = set()
for key, go_id in targets.items():
    subtree = set(descendants(go_id))
    component_ids = {c['component']['m_PathID'] for node in subtree
                     for c in trees.get(node, {}).get('m_Component', [])}
    providers, components, incoming = [], [], []
    for component_id in sorted(component_ids):
        tree = trees.get(component_id, {})
        name = script_name(tree)
        if name:
            related_classes.add(name)
            components.append({'id': component_id, 'class': name,
                               'owner': trees.get(tree.get('m_GameObject', {}).get('m_PathID'), {}).get('m_Name'),
                               'raycast_target': tree.get('m_RaycastTarget')})
        if '_tooltip' in tree:
            owner_id = tree.get('m_GameObject', {}).get('m_PathID')
            owner_tree = trees.get(owner_id, {})
            owner_components = [trees.get(c['component']['m_PathID'], {}) for c in owner_tree.get('m_Component', [])]
            rect = next((c for c in owner_components if 'm_SizeDelta' in c), {})
            providers.append({'id': component_id, 'class': name, 'enabled': tree.get('m_Enabled'),
                              'owner_id': owner_id, 'owner_name': owner_tree.get('m_Name'),
                              'owner_raycast_graphics': [{'class': script_name(c), 'enabled': c.get('m_Enabled'),
                                                          'raycast_target': c['m_RaycastTarget']}
                                                         for c in owner_components if 'm_RaycastTarget' in c],
                              'owner_rect': {k: rect[k] for k in ('m_AnchorMin', 'm_AnchorMax', 'm_SizeDelta', 'm_AnchoredPosition') if k in rect},
                              'tooltip': tree['_tooltip'], 'hover_time': tree.get('_hoverTime'),
                              'prefab': tree.get('_prefab'), 'anchor': tree.get('_anchorTransform')})
    for object_id, tree in trees.items():
        if object_id in subtree or object_id in component_ids or objects[object_id].type.name != 'MonoBehaviour':
            continue
        refs = [{'field': path, 'target': target} for path, target in references(tree)
                if target in subtree or target in component_ids]
        if refs:
            name = script_name(tree)
            if name:
                related_classes.add(name)
            incoming.append({'id': object_id, 'class': name, 'references': refs})
    rows.append({'key': key, 'go_id': go_id, 'serialized_active': trees[go_id]['m_IsActive'],
                 'subtree_gameobjects': len(subtree), 'components': components,
                 'providers': providers, 'incoming_component_references': incoming})

metadata_path = GAME / 'il2cpp_data/Metadata/global-metadata.dat'
data = metadata_path.read_bytes()
assert struct.unpack_from('<II', data) == (0xFAB11BAF, 27)
def table(word):
    offset, size = struct.unpack_from('<II', data, word * 4)
    assert 0 <= offset <= offset + size <= len(data)
    return offset, size
strings_offset, strings_size = table(6)
types_offset, types_size = table(40)
fields_offset, fields_size = table(24)
methods_offset, methods_size = table(12)
assert types_size % 88 == fields_size % 12 == methods_size % 32 == 0
def string(index):
    assert 0 <= index < strings_size
    end = data.index(b'\0', strings_offset + index, strings_offset + strings_size)
    return data[strings_offset + index:end].decode('utf-8')
metadata_types = []
for index in range(types_size // 88):
    offset = types_offset + index * 88
    name, namespace = struct.unpack_from('<ii', data, offset)
    fullname = '.'.join(filter(None, [string(namespace), string(name)]))
    field_start, method_start = struct.unpack_from('<ii', data, offset + 32)
    method_count = struct.unpack_from('<H', data, offset + 64)[0]
    field_count = struct.unpack_from('<H', data, offset + 68)[0]
    fields = [string(struct.unpack_from('<i', data, fields_offset + i * 12)[0])
              for i in range(field_start, field_start + field_count)]
    if fullname not in related_classes and not any(any(k.lower() in f.lower() for k in targets) for f in fields):
        continue
    methods = []
    for method in range(method_start, method_start + method_count):
        pos = methods_offset + method * 32
        ni, declaring = struct.unpack_from('<ii', data, pos)
        assert declaring == index
        methods.append({'name': string(ni), 'token': hex(struct.unpack_from('<I', data, pos + 20)[0])})
    metadata_types.append({'name': fullname, 'type_index': index, 'fields': fields, 'methods': methods})
result = {'targets': rows, 'metadata_types': metadata_types, 'read_errors': errors,
          'hashes': {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in (ui_path, script_path, metadata_path)},
          'limits': 'Serialized graph plus metadata names/tokens only; no native method bodies or runtime activation examined. Provider absence applies only to decoded subtree components. No asset writes.'}
(ROOT / 'reports/tooltip-gap-binding-trace.json').write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print(json.dumps({'targets': [{'key': row['key'], 'providers': row['providers'], 'incoming': row['incoming_component_references']} for row in rows],
                  'metadata_types': [row['name'] for row in metadata_types], 'errors': errors}))
