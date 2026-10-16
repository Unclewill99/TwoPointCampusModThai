"""Independent structural checks for TOOLTIPS-001; no runtime/semantic approval."""
import hashlib,json,re,unicodedata,argparse
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser();parser.add_argument('--target',default='local/translations/TOOLTIPS-001.th.json');parser.add_argument('--report',default='reports/tooltips-001-validation.json');args=parser.parse_args()
src=ROOT/'local/source/TOOLTIPS-001.json';dst=ROOT/args.target
a=json.loads(src.read_text(encoding='utf-8'));b=json.loads(dst.read_text(encoding='utf-8'));errors=[]
if len(a)!=len(b):errors.append('record count mismatch')
token=re.compile(r'\{[^{}]+\}|<[^<>]+>|\[i2[^\]]*\]')
for n,(s,t) in enumerate(zip(a,b),1):
 for k,v in s.items():
  if k not in ['thai','status'] and t.get(k)!=v:errors.append(f'{n}: changed {k}')
 text=t.get('thai','')
 if not isinstance(text,str) or not text:errors.append(f'{n}: empty/nonstring Thai');continue
 if t.get('status')!='TRANSLATED_PENDING_REVIEW':errors.append(f'{n}: status')
 if hashlib.sha256(s['source'].encode()).hexdigest()!=s['source_sha256']:errors.append(f'{n}: source hash')
 if token.findall(text)!=token.findall(s['source']):errors.append(f'{n}: token sequence')
 if text.count('\n')!=s['source'].count('\n'):errors.append(f'{n}: LF count')
 for sl,tl in zip(s['source'].split('\n'),text.split('\n')):
  if re.search(r'[\t ]*$',sl).group()!=re.search(r'[\t ]*$',tl).group():errors.append(f'{n}: trailing whitespace')
  if sl.count('\t')!=tl.count('\t') or (not sl.strip())!=(not tl.strip()):errors.append(f'{n}: blank/tab line')
 if '[i2t]' in text or any(c in text for c in ['\u200b','\u00a0','\ufffd']):errors.append(f'{n}: delimiter/invisible/replacement')
 if any(unicodedata.category(c).startswith('C') and c not in '\n\t\r' for c in text):errors.append(f'{n}: control')
 if t.get('flags') and not t.get('translator_note'):errors.append(f'{n}: flags without note')
if len({r['id'] for r in b})!=len(b):errors.append('duplicate IDs')
r={'records':len(b),'errors':errors,'source_batch_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
 'translation_sha256':hashlib.sha256(dst.read_bytes()).hexdigest(),'flags':dict(Counter(f for r in b for f in r.get('flags',[]))),
 'limits':'Heuristic token and structural checks only; no runtime substitution, semantic or rendering approval.'}
(ROOT/args.report).write_text(json.dumps(r,indent=2),encoding='utf-8');print(json.dumps(r,indent=2));raise SystemExit(bool(errors))
