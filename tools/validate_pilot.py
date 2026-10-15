"""Independent structural checks, not a runtime parser or translation approval."""
import hashlib
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
source = json.loads((ROOT/'local/source/PILOT-001.json').read_text(encoding='utf-8'))
target_path = ROOT/'local/translations/PILOT-001.th.json'
target = json.loads(target_path.read_text(encoding='utf-8'))
errors = []
pattern = re.compile(r'\{[^{}]+\}|<[^<>]+>|\[i2[^\]]*\]|%(?:\d+\$)?[-+#0 ]*\d*(?:\.\d+)?[sdif]')
immutable = ['id','key','asset','path_id','segment_index','source','source_sha256','context','candidate_tokens','batch']
if len(target)!=len(source): errors.append('Record count mismatch')
for n,(s,t) in enumerate(zip(source,target),1):
    for key in immutable:
        if t.get(key)!=s.get(key): errors.append(f'{n}: modified {key}')
    th=t.get('thai')
    if not isinstance(th,str) or not th: errors.append(f'{n}: empty/non-string thai'); continue
    if hashlib.sha256(s['source'].encode()).hexdigest()!=s['source_sha256']: errors.append(f'{n}: source hash mismatch')
    if pattern.findall(th)!=pattern.findall(s['source']): errors.append(f'{n}: token order/count/syntax mismatch')
    if th.count('\n')!=s['source'].count('\n'): errors.append(f'{n}: newline mismatch')
    if '[i2t]' in th: errors.append(f'{n}: record delimiter inserted')
    if any(c=='\ufffd' or (unicodedata.category(c).startswith('C') and c not in '\n\r\t') for c in th): errors.append(f'{n}: unexpected control/replacement')
    if '\u0e4d\u0e32' in th: errors.append(f'{n}: decomposed sara am')
    if t.get('status')!='TRANSLATED_PENDING_REVIEW': errors.append(f'{n}: unexpected status')
    if t.get('flags') and not t.get('translator_note'): errors.append(f'{n}: flags without note')
ids=[r['id'] for r in target]
if len(set(ids))!=len(ids): errors.append('Duplicate output IDs')
report={'records':len(target),'errors':errors,'input_sha256':hashlib.sha256(target_path.read_bytes()).hexdigest(),
        'flag_counts':dict(Counter(f for r in target for f in r.get('flags',[]))),
        'unique_codepoints':len(set(''.join(r['thai'] for r in target))),
        'token_detection':'Heuristic source/target syntax check, including observed [i2p_One]; not verified runtime grammar.',
        'limits':'No runtime argument semantics, font coverage, bundle rebuild/load or visual rendering validated.'}
(ROOT/'reports/pilot-001-validation.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
raise SystemExit(bool(errors))
