"""SEGMENTATION-002: propose corpus-wide U+200B break opportunities for fresh-translation-006 text.

Offline only (needs PyThaiNLP). Reads the r5 review corpus plus the single approved 005 override
(I2LS_UI segment 964 -> "Mod"), tokenizes the Thai runs with PyThaiNLP newmm, keeps only token
boundaries that pass segmentation_guard_002, and writes an opt-in cut map keyed by
(asset, segment_index) with the exact source SHA-256. No translation text is changed; the map
is a derived experimental value for tools/build_fresh_translation_007.py.

usage: python -I segment_corpus_002.py <all-records-review-r5.json> <out_dir>
"""
import json
import sys
from collections import Counter
from pathlib import Path

from pythainlp.corpus import thai_words
from pythainlp.tokenize import Tokenizer
from segmentation_guard_002 import PROTECTED, ZWSP, cut_reason, self_test, sha, validate

src_path, out_dir = Path(sys.argv[1]), Path(sys.argv[2])
extra_path = out_dir / 'extra-words.txt'
extra_words = [w.strip() for w in extra_path.read_text(encoding='utf-8').splitlines() if w.strip() and not w.startswith('#')]
tokenizer = Tokenizer(custom_dict=set(thai_words()) | set(extra_words), engine='newmm', keep_whitespace=True)
word_tokenize = tokenizer.word_tokenize
rows = json.loads(src_path.read_text(encoding='utf-8'))
assert len(rows) == 15677
OVERRIDE = ('I2LS_UI', 964)


def effective_text(row):
    if (row['asset'], row['segment_index']) == OVERRIDE:
        assert row['thai'] == 'ม็อด'
        return 'Mod'
    return row['thai']


def propose(text):
    """Token boundaries from newmm inside free (non-protected) spans, filtered by the guard."""
    cuts, rejected = [], Counter()
    spans = [(m.start(), m.end()) for m in PROTECTED.finditer(text)]
    free, pos = [], 0
    for s, e in spans:
        if s > pos:
            free.append((pos, s))
        pos = e
    if pos < len(text):
        free.append((pos, len(text)))
    for s, e in free:
        chunk = text[s:e]
        if not any('\u0e01' <= c <= '\u0e5b' for c in chunk):
            continue
        offset = s
        tokens = word_tokenize(chunk)
        assert ''.join(tokens) == chunk
        for tok in tokens[:-1]:
            offset += len(tok)
            reason = cut_reason(text, offset)
            if reason:
                rejected[reason] += 1
            else:
                cuts.append(offset)
    return sorted(set(cuts)), rejected


negative = self_test()
records, stats, rejected_total = [], Counter(), Counter()
examples = {}
for row in rows:
    text = effective_text(row)
    assert ZWSP not in text
    cuts, rejected = propose(text)
    rejected_total.update(rejected)
    source_hash = sha(text.encode('utf-8'))
    marked = validate(text, cuts, source_hash)
    assert marked.replace(ZWSP, '') == text
    stats['records'] += 1
    stats['records_with_cuts'] += bool(cuts)
    stats['cuts'] += len(cuts)
    records.append({'id': row['id'], 'asset': row['asset'], 'segment_index': row['segment_index'], 'key': row['key'],
                    'source_sha256': source_hash, 'cut_offsets_codepoints': cuts, 'marked_sha256': sha(marked.encode('utf-8'))})
    if row['key'] in ('Meta/LoadingScreen/Tips_LS_Paths_Text', 'Levels/Freshleigh/Level_Description',
                      'UI/Settings/Tooltips/MSAASamples', 'UI/Settings/Tooltips/WorldDetail'):
        examples[row['key']] = marked.replace(ZWSP, '|')

out_dir.mkdir(parents=True, exist_ok=True)
package = {'batch': 'SEGMENTATION-002', 'parent_text': 'fresh-translation-006 (r5 corpus + I2LS_UI segment 964 override = Mod)',
           'source_corpus_sha256': sha(src_path.read_bytes()), 'tokenizer': 'PyThaiNLP 5.4.0 newmm, dictionary = thai_words() + extra-words.txt (%d words, sha256 %s), keep_whitespace=True' % (len(extra_words), sha(extra_path.read_bytes())),
           'guard': 'segmentation_guard_002.cut_reason', 'status': 'PROPOSAL_STAGED_NOT_BUILT',
           'stats': dict(stats), 'guard_rejections': dict(rejected_total), 'negative_controls_rejected': negative,
           'records': records,
           'limits': 'Automatic dictionary segmentation; structural guard only. Experimental candidate input, not production approval. '
                     'Strip U+200B to recover the exact 006 text.'}
map_path = out_dir / 'cut-map.json'
map_path.write_text(json.dumps(package, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
# Human review view: every marked record with | at proposed cuts (Thai-bearing records only).
with (out_dir / 'review-marked.tsv').open('w', encoding='utf-8') as f:
    f.write('id\tcuts\tmarked_with_pipes\n')
    for row, rec in zip(rows, records):
        if rec['cut_offsets_codepoints']:
            text = effective_text(row)
            cs = set(rec['cut_offsets_codepoints'])
            f.write('%s\t%d\t%s\n' % (rec['id'], len(cs), ''.join(('|' if i in cs else '') + c for i, c in enumerate(text)).replace('\n', '\\n').replace('\t', '\\t')))
summary = {k: v for k, v in package.items() if k != 'records'} | {'cut_map_sha256': sha(map_path.read_bytes()), 'examples': examples}
(out_dir / 'preparation.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(summary, ensure_ascii=False, indent=2))
