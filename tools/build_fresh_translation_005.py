"""Apply the approved exact menu override to frozen 004; stage only."""
from pathlib import Path
import hashlib
import json
import shutil
import UnityPy

R = Path(__file__).resolve().parents[1]
base = R / 'local/prototype/fresh-translation-004'
out = R / 'local/prototype/fresh-translation-005'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
manifest = json.loads((base / 'manifest.json').read_text())
override_path = R / 'local/review/user-menu-corrections/mod-menu-override.json'
override = json.loads(override_path.read_text(encoding='utf-8'))
assert override['id'] == 'I2LS_UI::UI/Modding/Mods::segment-964'
assert override['before'] == 'ม็อด' and override['after'] == 'Mod'
for f in manifest['files']:
    assert sha(base / f['name']) == f['probe_sha256']
UnityPy.config.FALLBACK_UNITY_VERSION = '2020.3.47f1'
name = 'localisation_assets_localisationenglish.bundle'
env = UnityPy.load(str(base / name))
before = {}
changes = 0
for obj in env.objects:
    if obj.type.name != 'TextAsset':
        continue
    asset = obj.read()
    assert asset.m_Name not in before
    before[asset.m_Name] = asset.m_Script
    if asset.m_Name == 'I2LS_UI':
        parts = asset.m_Script.split('[i2t]')
        assert parts[964] == 'UI/Modding/Mods=' + override['before']
        parts[964] = 'UI/Modding/Mods=' + override['after']
        asset.m_Script = '[i2t]'.join(parts)
        asset.save()
        changes += 1
assert changes == 1
out.mkdir(exist_ok=False)
(out / name).write_bytes(next(iter(env.files.values())).save())
after_env = UnityPy.load(str(out / name))
after = {o.read().m_Name: o.read().m_Script for o in after_env.objects if o.type.name == 'TextAsset'}
assert before.keys() == after.keys()
diffs = []
for asset, script in before.items():
    old, new = script.split('[i2t]'), after[asset].split('[i2t]')
    assert len(old) == len(new)
    diffs.extend((asset, i, a, b) for i, (a, b) in enumerate(zip(old, new)) if a != b)
assert diffs == [('I2LS_UI', 964, 'UI/Modding/Mods=ม็อด', 'UI/Modding/Mods=Mod')]
rows = json.loads((R / 'local/translations/CLAUDE-FULL-RETRANSLATION-001/all-records-review-r5.json').read_text(encoding='utf-8'))
for row in rows:
    expected = 'Mod' if (row['asset'], row['segment_index']) == ('I2LS_UI', 964) else row['thai']
    assert after[row['asset']].split('[i2t]')[row['segment_index']] == row['key'] + '=' + expected
files = []
for f in manifest['files']:
    if f['name'] != name:
        shutil.copyfile(base / f['name'], out / f['name'])
    files.append(dict(name=f['name'], original_sha256=f['original_sha256'], probe_sha256=sha(out / f['name'])))
report = dict(probe='fresh-translation-005', parent='fresh-translation-004', files=files,
              installed=False, runtime_status='NOT_RUN', records_reloaded=len(rows),
              changed_records=diffs, override_sha256=sha(override_path),
              translated=12710, keep_as_source=2967, font_ui_identical_to='fresh-translation-004',
              language_review='PENDING',
              scope='One localization key only. All consumers of UI/Modding/Mods receive Mod; runtime consumer coverage not established. Mod.io and every other record unchanged.',
              limits='No runtime approval inherited. Known shaping, wrapping and terminology issues remain open.')
for f in manifest['files']:
    assert sha(base / f['name']) == f['probe_sha256']
(out / 'manifest.json').write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding='utf-8')
(R / 'reports/fresh-translation-005-build.json').write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding='utf-8')
print('15677 exact reload checks passed; exactly one segment changed to Mod; frozen 004 unchanged; staged only.')
