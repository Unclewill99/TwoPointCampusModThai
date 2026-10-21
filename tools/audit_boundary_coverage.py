"""Inventory reported runtime boundaries; source LF and repeats are not new coverage."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
clean = lambda value: ''.join(value.split())
mapping = {r['key'].rsplit('/', 1)[-1]: r['thai'] for r in json.loads((ROOT / 'local/prototype/probe-013/tooltip-map.json').read_text(encoding='utf-8'))}
observations = []
for relative in ['local/qa/WO-VISUAL-013/93-observed-rows.json', 'local/qa/WO-VISUAL-014/retry/2026-10-18/93-observed-rows.json', 'local/qa/WO-VISUAL-015/93-observed-text.json']:
    records = json.loads((ROOT / relative).read_text(encoding='utf-8'))
    if isinstance(records, dict):
        records = [records]
    for record in records:
        key = record['key'].rsplit('/', 1)[-1]
        rows = record['rows']
        source = mapping[key]
        assert clean(''.join(rows)) == clean(source), key
        lf_positions, position = set(), 0
        for segment in source.split('\n')[:-1]:
            position += len(clean(segment))
            lf_positions.add(position)
        position = 0
        for before, after in zip(rows, rows[1:]):
            position += len(clean(before))
            if position in lf_positions:
                continue
            observations.append({'key': key, 'evidence': relative, 'offset_ignoring_whitespace': position,
                                 'left': before[-18:], 'right': after[:18:]})
unique = {(row['key'], row['offset_ignoring_whitespace']): row for row in observations}
corpus = json.loads((ROOT / 'docs/qa/rendering-corpus.json').read_text(encoding='utf-8'))
paragraph = next(row['text'] for row in corpus['items'] if row['id'] == 'CRP-WRAP-03')
prior = json.loads((ROOT / 'local/prototype/probe-012a/diagnostic-map.json').read_text(encoding='utf-8'))['text']
assert paragraph not in prior
result = {'date': '2026-10-18', 'actual_tooltip_unique_runtime_boundaries': len(unique),
          'boundaries': list(unique.values()),
          'WO_012': {'reported_boundaries': 5, 'distinct_contexts': 2,
                     'offsets': [56, 108, 164, 216, 272],
                     'contexts': ['เข้าศึกษา / ในหลักสูตร', 'ประสิทธิภาพ / มหาวิทยาลัย']},
          'next_question': 'What runtime boundaries occur in CRP-WRAP-03 at the established bounded width, and do any observed breaks detach a leading vowel or combining sequence?',
          'new_probe': 'probe-016', 'runtime_status': 'NOT_RUN',
          'limits': 'Transcription/source accounting only, not fresh screenshot inspection or dictionary segmentation. Actual-tooltip offsets omit whitespace; WO-012 offsets count underlying codepoints. Repeated scales/paragraphs do not constitute distinct boundary contexts. New input does not force every target to an edge.'}
(ROOT / 'reports/line-boundary-coverage-audit.json').write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print(json.dumps({'actual_tooltip_unique_runtime_boundaries': len(unique), 'WO_012_distinct_contexts': 2, 'new_paragraph_in_prior_AB': False}))
