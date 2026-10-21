"""Stage manually proposed word-break opportunities for the observed WO-016 defect."""
import hashlib
import json
from pathlib import Path
import UnityPy

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'local/prototype/probe-016'
OUT = ROOT / 'local/prototype/probe-017'
GAME = ROOT.parent / 'TPC_Data/StreamingAssets/aa/StandaloneWindows64'
sha = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
bm = json.loads((BASE / 'manifest.json').read_text())
am = json.loads((BASE / 'diagnostic-map.json').read_text(encoding='utf-8'))
for item in bm['files']:
    assert sha(BASE / item['name']) == item['probe_sha256']
    assert sha(GAME / item['name']) == item['original_sha256']
assert sha(BASE / 'diagnostic-map.json') == bm['diagnostic_map_sha256']
# Explicit Controller proposals, not an automatic segmenter or approved dictionary.
segments = ['เมื่อ', 'ถึง', 'เวลา', 'ทุกคน', 'ต้อง', 'เดินทาง', 'ไป', 'เรียน',
            'ที่', 'โรงอาหาร', 'และ', 'เตรียมตัว', 'เข้า', 'ห้องเรียน', 'วิชา', 'เคมี']
assert ''.join(segments) == am['paragraph']
text = '\u200b'.join(segments * 3)
assert text.replace('\u200b', '') == am['text']
assert not any(c in text for c in '\n\r\t <>')
cuts, position = [], 0
for segment in (segments * 3)[:-1]:
    position += len(segment)
    cuts.append(position)
assert len(cuts) == 47
assert not set([113, 172, 227]) & set(cuts)
UnityPy.config.FALLBACK_UNITY_VERSION = '2020.3.47f1'
name = 'localisation_assets_localisationenglish.bundle'
env = UnityPy.load(str(BASE / name))
def assets(e):
    return {o.read().m_Name: o.read().m_Script for o in e.objects if o.type.name == 'TextAsset'}
before = assets(env)
obj = next(o for o in env.objects if o.type.name == 'TextAsset' and o.read().m_Name == am['asset'])
data = obj.read()
parts = data.m_Script.split('[i2t]')
index = am['segment_index']
assert parts[index] == am['key'] + '=' + am['text']
parts[index] = am['key'] + '=' + text
data.m_Script = '[i2t]'.join(parts)
data.save()
OUT.mkdir(parents=True, exist_ok=True)
(OUT / name).write_bytes(next(iter(env.files.values())).save())
after = assets(UnityPy.load(str(OUT / name)))
assert before.keys() == after.keys()
for asset in before:
    if asset != am['asset']:
        assert before[asset] == after[asset]
old, new = before[am['asset']].split('[i2t]'), after[am['asset']].split('[i2t]')
assert len(old) == len(new)
assert [i for i, (a, b) in enumerate(zip(old, new)) if a != b] == [index]
assert new[index] == am['key'] + '=' + text
files = []
for item in bm['files']:
    if item['name'] != name:
        (OUT / item['name']).write_bytes((BASE / item['name']).read_bytes())
        assert sha(OUT / item['name']) == item['probe_sha256']
    files.append(dict(item, probe_sha256=sha(OUT / item['name'])))
mapping = {'probe': 'probe-017', 'baseline_probe': 'probe-016', 'key': am['key'], 'asset': am['asset'],
           'segment_index': index, 'text': text, 'underlying_text': am['text'], 'repeat_count': 3,
           'paragraph_segments': segments, 'underlying_codepoints': 237, 'zwsp_count': text.count('\u200b'),
           'zwsp_underlying_cut_offsets': cuts, 'zwsp_actual_indices': [i for i, c in enumerate(text) if c == '\u200b'],
           'manual_LF_count': 0, 'runtime_status': 'NOT_RUN',
           'limits': 'Manually proposed break opportunities for QA review, not a dictionary or production segmentation policy.'}
(OUT / 'diagnostic-map.json').write_text(json.dumps(mapping, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
manifest = {'probe': 'probe-017', 'installed': False, 'runtime_status': 'NOT_RUN', 'files': files,
            'baseline_probe': 'probe-016', 'baseline_manifest_sha256': sha(BASE / 'manifest.json'),
            'diagnostic_map_sha256': sha(OUT / 'diagnostic-map.json'), 'underlying_text_equal': True,
            'changed_segments': [index], 'font_UI_identical_to_baseline': True,
            'strategy': 'Only 47 proposed U+200B opportunities differ from WO-016 input; frozen font/UI/underlying text.',
            'limits': 'Runtime behavior unknown; no production invisible-character policy, linguistic approval or release.'}
(OUT / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
(ROOT / 'reports/probe-017-build.json').write_text(json.dumps(manifest, indent=2) + '\n')
print(json.dumps({'probe': 'probe-017', 'underlying_equal': True, 'ZWSP': 47, 'font_UI_identical': True, 'installed': False}))
