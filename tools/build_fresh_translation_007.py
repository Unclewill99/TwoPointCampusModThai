"""Build fresh-translation-007 = fresh-translation-006 text + SEGMENTATION-002 U+200B break opportunities.

Stage only; never touches game files. Fonts/UI bundles are byte-identical to 006; only the
localisation bundle changes. Every segment's marked text minus U+200B must equal the 006 text.
Run on Windows from the mod root:  python tools/build_fresh_translation_007.py
"""
from pathlib import Path
import hashlib
import json
import shutil
import sys
import UnityPy

R = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(R / 'tools'))
from segmentation_guard_002 import ZWSP, sha as sha_bytes, validate  # noqa: E402

base = R / 'local/prototype/fresh-translation-006'
out = R / 'local/prototype/fresh-translation-007'
seg = R / 'local/segmentation/SEGMENTATION-002'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
manifest = json.loads((base / 'manifest.json').read_text(encoding='utf-8'))
for f in manifest['files']:
    assert sha(base / f['name']) == f['probe_sha256'], 'frozen 006 changed: ' + f['name']
package = json.loads((seg / 'cut-map.json').read_text(encoding='utf-8'))
prep = json.loads((seg / 'preparation.json').read_text(encoding='utf-8'))
assert package['batch'] == 'SEGMENTATION-002' and prep['cut_map_sha256'] == sha(seg / 'cut-map.json')
cuts = {(r['asset'], r['segment_index']): r for r in package['records']}
assert len(cuts) == 15677
assert not out.exists(), 'fresh-translation-007 already staged; remove it first'

UnityPy.config.FALLBACK_UNITY_VERSION = '2020.3.47f1'
name = 'localisation_assets_localisationenglish.bundle'
env = UnityPy.load(str(base / name))
before, used, changed, inserted = {}, set(), 0, 0
for obj in env.objects:
    if obj.type.name != 'TextAsset':
        continue
    asset = obj.read()
    assert asset.m_Name not in before
    before[asset.m_Name] = asset.m_Script
    parts = asset.m_Script.split('[i2t]')
    touched = False
    for i, part in enumerate(parts):
        rec = cuts.get((asset.m_Name, i))
        if rec is None:
            continue
        used.add((asset.m_Name, i))
        key, text = part.split('=', 1)
        assert key == rec['key'], (asset.m_Name, i)
        assert ZWSP not in part
        marked = validate(text, rec['cut_offsets_codepoints'], rec['source_sha256'])
        assert sha_bytes(marked.encode('utf-8')) == rec['marked_sha256']
        if marked != text:
            parts[i] = key + '=' + marked
            touched = True
            changed += 1
            inserted += len(rec['cut_offsets_codepoints'])
    if touched:
        asset.m_Script = '[i2t]'.join(parts)
        asset.save()
assert used == set(cuts), 'map records not found in bundle: %d' % len(set(cuts) - used)
assert changed == package['stats']['records_with_cuts'] and inserted == package['stats']['cuts']

out.mkdir(exist_ok=False)
(out / name).write_bytes(next(iter(env.files.values())).save())
after_env = UnityPy.load(str(out / name))
after = {o.read().m_Name: o.read().m_Script for o in after_env.objects if o.type.name == 'TextAsset'}
assert before.keys() == after.keys()
for a, script in before.items():
    old, new = script.split('[i2t]'), after[a].split('[i2t]')
    assert len(old) == len(new)
    for i, (x, y) in enumerate(zip(old, new)):
        assert y.replace(ZWSP, '') == x, (a, i)
        assert ZWSP not in x
        if (a, i) in cuts:
            assert y.count(ZWSP) == len(cuts[(a, i)]['cut_offsets_codepoints'])
        else:
            assert x == y
files = []
for f in manifest['files']:
    if f['name'] != name:
        shutil.copyfile(base / f['name'], out / f['name'])
        assert sha(out / f['name']) == f['probe_sha256']
    files.append(dict(name=f['name'], original_sha256=f['original_sha256'], probe_sha256=sha(out / f['name']),
                      parent_sha256=f['probe_sha256']))
report = dict(wo='WO-SEGMENTATION-002', probe='fresh-translation-007', parent='fresh-translation-006', files=files,
              installed=False, runtime_status='NOT_RUN', records_reloaded=15677,
              records_marked=changed, zwsp_inserted=inserted, cut_map_sha256=prep['cut_map_sha256'],
              tokenizer=package['tokenizer'], font_ui_byte_identical_to='fresh-translation-006',
              text_minus_zwsp_identical_to='fresh-translation-006', clusters=manifest.get('clusters'),
              scope='Only U+200B inserted at guarded dictionary word boundaries; no translation, font, UI, LF, token or tag change.',
              limits='Experimental candidate for BUG-THAI-002. Not a production approval; runtime regression pending.')
for f in manifest['files']:
    assert sha(base / f['name']) == f['probe_sha256']
(out / 'manifest.json').write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding='utf-8')
(R / 'reports/fresh-translation-007-build.json').write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding='utf-8')
print('15677 segments reloaded; %d records marked with %d U+200B; strip-check identical to 006; staged only.' % (changed, inserted))
