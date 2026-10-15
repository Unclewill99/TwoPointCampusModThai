"""Extract local-only source corpus with exact lossless delimiter round-trip checks."""
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
import UnityPy

ROOT = Path(__file__).resolve().parents[1]
UnityPy.config.FALLBACK_UNITY_VERSION = '2020.3.47f1'
bundle = ROOT.parent / 'TPC_Data/StreamingAssets/aa/StandaloneWindows64/localisation_assets_localisationenglish.bundle'
out = ROOT / 'local/source'
out.mkdir(parents=True, exist_ok=True)
records, stats = [], []
for obj in UnityPy.load(str(bundle)).objects:
    if obj.type.name != 'TextAsset':
        continue
    asset = obj.read()
    text = asset.m_Script
    if isinstance(text, bytes):
        text = text.decode('utf-8', errors='strict')
    parts = text.split('[i2t]')
    assert '[i2t]'.join(parts) == text
    count = 0
    for index, part in enumerate(parts):
        if not part:
            continue
        if '=' not in part:
            raise ValueError(f'Unexpected segment: {asset.m_Name}:{index}')
        key, value = part.split('=', 1)
        assert key + '=' + value == part
        records.append({'id': asset.m_Name + '::' + key + '::segment-' + str(index), 'key': key,
                        'asset': asset.m_Name, 'path_id': obj.path_id, 'segment_index': index,
                        'source': value, 'thai': '', 'context': {'key_path': key, 'screen': None},
                        'source_sha256': hashlib.sha256(value.encode('utf-8')).hexdigest(),
                        'candidate_tokens': re.findall(r'\{[^{}]+\}|<[^<>]+>', value),
                        'status': 'UNTRANSLATED'})
        count += 1
    (out / (asset.m_Name + '.txt')).write_text(text, encoding='utf-8', newline='')
    stats.append({'asset': asset.m_Name, 'records': count, 'sha256': hashlib.sha256(text.encode('utf-8')).hexdigest(), 'text_roundtrip': True})
counts = Counter((r['asset'],r['key']) for r in records)
duplicates = [k for k,v in counts.items() if v > 1]
assert len({r['id'] for r in records}) == len(records)
(out / 'all-english.json').write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding='utf-8')
# Deterministic representative pilot; source text is local-only, not committed.
pilot, seen = [], set()
def take(predicate, limit):
    selected = 0
    for r in records:
        if r['id'] not in seen and predicate(r):
            pilot.append(dict(r, batch='PILOT-001'))
            seen.add(r['id'])
            selected += 1
            if selected >= limit:
                break
take(lambda r: r['asset'] == 'I2LS_UI_Settings', 10)
take(lambda r: r['asset'] == 'I2LS_UI' and 0 < len(r['source']) < 25, 10)
take(lambda r: r['asset'] in ('I2LS_UI','I2LS_CodeRef') and bool(r['candidate_tokens']), 10)
take(lambda r: r['asset'] == 'I2LS_Courses', 10)
take(lambda r: r['asset'] == 'I2LS_Advisor', 10)
(out / 'PILOT-001.json').write_text(json.dumps(pilot, ensure_ascii=False, indent=2), encoding='utf-8')
report = {'bundle_sha256': hashlib.sha256(bundle.read_bytes()).hexdigest(),
          'records': len(records), 'assets': stats, 'duplicate_ids': duplicates,
          'pilot_records': len(pilot), 'pilot_ids': [r['id'] for r in pilot],
          'format_observed': 'TextAsset segments separated by [i2t]; first = separates key and value',
          'limits': 'Decoded-text roundtrip only; no bundle rebuild, runtime import or placeholder grammar verified.'}
(ROOT / 'reports/source-extraction.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'records': len(records), 'assets':len(stats),'pilot':len(pilot),'duplicate_ids':len(duplicates)}))
