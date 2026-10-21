"""Stage an unchanged-corpus paragraph in the accepted bounded tooltip; never installs."""
import hashlib
import json
from pathlib import Path
import unicodedata
import UnityPy

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'local/prototype/probe-013'
OUT = ROOT / 'local/prototype/probe-016'
GAME = ROOT.parent / 'TPC_Data/StreamingAssets/aa/StandaloneWindows64'
sha = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
manifest = json.loads((BASE / 'manifest.json').read_text(encoding='utf-8'))
for item in manifest['files']:
    assert sha(BASE / item['name']) == item['probe_sha256']
    assert sha(GAME / item['name']) == item['original_sha256']
corpus_path = ROOT / 'docs/qa/rendering-corpus.json'
corpus = json.loads(corpus_path.read_text(encoding='utf-8'))
case = next(row for row in corpus['items'] if row['id'] == 'CRP-WRAP-03')
paragraph = case['text']
text = paragraph * 3
assert len(paragraph) == 79 and len(text) == 237
assert not any(c in text for c in '\n\r\t\u200b\u00a0<>')
assert '[i2t]' not in text
UnityPy.config.FALLBACK_UNITY_VERSION = '2020.3.47f1'
name = 'localisation_assets_localisationenglish.bundle'
key = 'UI/Settings/Tooltips/Resolution'
def texts(env):
    return {obj.read().m_Name: obj.read().m_Script for obj in env.objects if obj.type.name == 'TextAsset'}
env = UnityPy.load(str(BASE / name))
before = texts(env)
obj = next(obj for obj in env.objects if obj.type.name == 'TextAsset' and obj.read().m_Name == 'I2LS_UI_Settings')
asset = obj.read()
parts = asset.m_Script.split('[i2t]')
indices = [index for index, part in enumerate(parts) if part.split('=', 1)[0] == key]
assert len(indices) == 1
index = indices[0]
parts[index] = key + '=' + text
asset.m_Script = '[i2t]'.join(parts)
asset.save()
OUT.mkdir(parents=True, exist_ok=True)
(OUT / name).write_bytes(next(iter(env.files.values())).save())
after = texts(UnityPy.load(str(OUT / name)))
assert set(before) == set(after)
for asset_name in before:
    if asset_name != 'I2LS_UI_Settings':
        assert before[asset_name] == after[asset_name]
old, new = before['I2LS_UI_Settings'].split('[i2t]'), after['I2LS_UI_Settings'].split('[i2t]')
assert len(old) == len(new)
assert [i for i, (a, b) in enumerate(zip(old, new)) if a != b] == [index]
assert new[index] == key + '=' + text
files = []
for item in manifest['files']:
    if item['name'] != name:
        (OUT / item['name']).write_bytes((BASE / item['name']).read_bytes())
        assert sha(OUT / item['name']) == item['probe_sha256']
    files.append({'name': item['name'], 'original_sha256': item['original_sha256'], 'probe_sha256': sha(OUT / item['name'])})
mapping = {'probe': 'probe-016', 'case': case['id'], 'key': key, 'asset': 'I2LS_UI_Settings',
           'segment_index': index, 'paragraph': paragraph, 'text': text, 'repeat_count': 3,
           'paragraph_length_codepoints': len(paragraph), 'total_codepoints': len(text),
           'source_corpus_sha256': sha(corpus_path), 'paragraph_sha256': hashlib.sha256(paragraph.encode()).hexdigest(),
           'leading_vowel_counts': {v: text.count(v) for v in 'เแโใไ'},
           'combining_mark_count': sum(unicodedata.category(c).startswith('M') for c in text),
           'manual_LF_count': 0, 'zwsp_offsets': [], 'runtime_status': 'NOT_RUN',
           'limits': 'Three copies without separators; paragraph unchanged. Not a claim that every vowel or cluster is forced to a runtime boundary. No ใ in this paragraph.'}
(OUT / 'diagnostic-map.json').write_text(json.dumps(mapping, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
result = {'probe': 'probe-016', 'installed': False, 'runtime_status': 'NOT_RUN', 'files': files,
          'base_probe': 'probe-013', 'diagnostic_map_sha256': sha(OUT / 'diagnostic-map.json'),
          'changed_text_assets': ['I2LS_UI_Settings'], 'changed_segments': [index],
          'strategy': 'Only Resolution tooltip replaced with three exact CRP-WRAP-03 copies; font/UI bytes identical to probe-013.',
          'limits': 'Synthetic boundary diagnostic, not production translation. Runtime wrapping/containment and actual boundary coverage unverified. No new rendering or release approval.'}
(OUT / 'manifest.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
(ROOT / 'reports/probe-016-build.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'probe': 'probe-016', 'codepoints': len(text), 'changed_segments': 1, 'font_UI_unchanged': True, 'installed': False}))
