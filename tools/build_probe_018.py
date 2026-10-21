"""Stage a controlled two-width/two-input matrix. Never installs game files."""
import copy
import hashlib
import json
from pathlib import Path
import UnityPy
from prepare_segmentation_review import validate

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'local/prototype/probe-013'
GAME = ROOT.parent / 'TPC_Data/StreamingAssets/aa/StandaloneWindows64'
sha = lambda data: hashlib.sha256(data).hexdigest()
read_json = lambda path: json.loads(path.read_text(encoding='utf-8'))
bm = read_json(BASE / 'manifest.json')
package_path = ROOT / 'local/segmentation/SEGMENTATION-001/proposals.json'
review = read_json(ROOT / 'reports/segmentation-001-controller-review.json')
package = read_json(package_path)
assert review['decision'] == 'ACCEPT_EXPERIMENTAL_MAP_UNCHANGED'
assert sha(package_path.read_bytes()) == review['proposal_sha256']
assert sha((ROOT / 'docs/qa/SEGMENTATION_001_REVIEW.md').read_bytes()) == review['review_sha256']
assert sha((BASE / 'tooltip-map.json').read_bytes()) == package['source_map_sha256']
assert len(package['records']) == 2
original_bytes = {}
for f in bm['files']:
    original_bytes[f['name']] = (BASE / f['name']).read_bytes()
    assert sha(original_bytes[f['name']]) == f['probe_sha256']
    assert sha((GAME / f['name']).read_bytes()) == f['original_sha256']
for r in package['records']:
    assert validate(r['text'], r['cut_offsets_codepoints'], r['source_sha256']) == r['marked_text']
    assert r['marked_text'].replace('\u200b', '') == r['text']

UnityPy.config.FALLBACK_UNITY_VERSION = '2020.3.47f1'
loc_name = 'localisation_assets_localisationenglish.bundle'
ui_name = 'ui-prefabs-general_assets_all.bundle'
def text_assets(env):
    return {o.read().m_Name: o.read().m_Script for o in env.objects if o.type.name == 'TextAsset'}

env = UnityPy.load(str(BASE / loc_name))
before = text_assets(env)
obj = next(o for o in env.objects if o.type.name == 'TextAsset' and o.read().m_Name == 'I2LS_UI_Settings')
asset = obj.read()
parts = asset.m_Script.split('[i2t]')
indices = []
for r in package['records']:
    matches = [i for i, part in enumerate(parts) if part.split('=', 1)[0] == r['key']]
    assert len(matches) == 1
    i = matches[0]
    assert parts[i] == r['key'] + '=' + r['text']
    parts[i] = r['key'] + '=' + r['marked_text']
    indices.append(i)
asset.m_Script = '[i2t]'.join(parts)
asset.save()
marked_loc = next(iter(env.files.values())).save()
after = text_assets(UnityPy.load(marked_loc))
assert before.keys() == after.keys()
for name in before:
    if name != 'I2LS_UI_Settings':
        assert before[name] == after[name]
old, new = before['I2LS_UI_Settings'].split('[i2t]'), after['I2LS_UI_Settings'].split('[i2t]')
assert len(old) == len(new)
assert [i for i, (a, b) in enumerate(zip(old, new)) if a != b] == sorted(indices)

env = UnityPy.load(str(BASE / ui_name))
objects = {o.path_id: o for o in env.objects}
rect_id = 3218277146759428662
rect = objects[rect_id].read_typetree()
assert rect['m_SizeDelta']['x'] == 800.0
assert objects[2617668728378194486].read_typetree()['m_ChildControlWidth'] == 0
assert objects[2671690608638065206].read_typetree()['m_TextWrappingMode'] == 1
raw_before = {o.path_id: o.get_raw_data() for o in env.objects}
narrow_rect = copy.deepcopy(rect)
narrow_rect['m_SizeDelta']['x'] = 600.0
objects[rect_id].save_typetree(narrow_rect)
narrow_ui = next(iter(env.files.values())).save()
reloaded = {o.path_id: o for o in UnityPy.load(narrow_ui).objects}
assert set(reloaded) == set(raw_before)
assert [i for i in raw_before if raw_before[i] != reloaded[i].get_raw_data()] == [rect_id]
assert reloaded[rect_id].read_typetree() == narrow_rect

outputs = []
for width in [800, 600]:
    for variant in ['a', 'b']:
        probe = f'probe-018-{width}{variant}'
        out = ROOT / 'local/prototype' / probe
        out.mkdir(parents=True, exist_ok=False)
        files = []
        for f in bm['files']:
            name = f['name']
            payload = original_bytes[name]
            if name == loc_name and variant == 'b':
                payload = marked_loc
            if name == ui_name and width == 600:
                payload = narrow_ui
            (out / name).write_bytes(payload)
            assert sha((out / name).read_bytes()) == sha(payload)
            files.append(dict(f, probe_sha256=sha(payload)))
        mapping = {'probe': probe, 'width_units': width, 'variant': variant.upper(),
                   'proposal_sha256': review['proposal_sha256'], 'runtime_status': 'NOT_RUN',
                   'records': [{'key': r['key'], 'underlying_text': r['text'],
                                'text': r['marked_text'] if variant == 'b' else r['text'],
                                'source_sha256': r['source_sha256'],
                                'source_LF_offsets': [i for i, c in enumerate(r['text']) if c == '\n'],
                                'proposed_cut_offsets': r['cut_offsets_codepoints'] if variant == 'b' else []}
                               for r in package['records']]}
        map_path = out / 'diagnostic-map.json'
        map_path.write_text(json.dumps(mapping, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        result = {'probe': probe, 'installed': False, 'runtime_status': 'NOT_RUN',
                  'base_probe': 'probe-013', 'files': files, 'diagnostic_map_sha256': sha(map_path.read_bytes()),
                  'width_units': width, 'variant': variant.upper(),
                  'proposal_sha256': review['proposal_sha256'],
                  'changed_localisation_segments': sorted(indices) if variant == 'b' else [],
                  'changed_UI_objects_from_probe_013': [rect_id] if width == 600 else [],
                  'limits': 'Experimental matrix only. Actual effective widths, boundaries and benefit NOT_RUN; no production ZWSP or release approval.'}
        (out / 'manifest.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
        outputs.append(result)

for width in [800, 600]:
    a, b = [r for r in outputs if r['width_units'] == width]
    af, bf = {f['name']: f for f in a['files']}, {f['name']: f for f in b['files']}
    assert af[ui_name]['probe_sha256'] == bf[ui_name]['probe_sha256']
    assert af['fonts_assets_all.bundle']['probe_sha256'] == bf['fonts_assets_all.bundle']['probe_sha256']
for variant in ['A', 'B']:
    a, b = [r for r in outputs if r['variant'] == variant]
    assert next(f for f in a['files'] if f['name'] == loc_name)['probe_sha256'] == next(f for f in b['files'] if f['name'] == loc_name)['probe_sha256']
report = {'batch': 'probe-018', 'variants': outputs, 'matrix_cells_planned': 8,
          'selected_keys': [r['key'] for r in package['records']],
          'same_width_AB_font_UI_equal': True, 'same_variant_cross_width_localisation_equal': True,
          'runtime_status': 'NOT_RUN', 'installed': False}
(ROOT / 'reports/probe-018-build.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'variants': 4, 'planned_cells': 8, 'all_reload_isolation_checks': 'PASS', 'installed': False}))
