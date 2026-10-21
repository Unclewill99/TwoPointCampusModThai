"""Validate sparse round5 changes against preserved round1-4 baseline."""
from pathlib import Path
from collections import Counter
import json,re,hashlib
R=Path(__file__).resolve().parents[1];P=R/'local/translations/CLAUDE-FULL-RETRANSLATION-001';handoff=R/'local/handoffs/CLAUDE-FULL-RETRANSLATION-001';manifest=json.loads((handoff/'manifest.json').read_text());fixes=json.loads((P/'review-round5/corrections.json').read_text(encoding='utf-8'));fixmap={x['id']:x for x in fixes};assert len(fixes)==len(fixmap)==321
baseflat={x['id']:x for x in json.loads((P/'all-records-review-r1-4.json').read_text(encoding='utf-8'))};errors=[];rows=[];changed=[];added=Counter();seen=set();patched_batches=[]
pattern=re.compile(r'\{[^{}]+\}|<[^<>]+>|\[[^\[\]]+\]|%(?:\d+\$)?[-+#0]*\d*(?:\.\d+)?[sdifouxXeEgGcpaA%]')
for batch in manifest['batches']:
 bid=batch['batch'];filename=bid+'.th.json';base=json.loads((P/'output-merged-review-r1-4'/filename).read_text(encoding='utf-8'));patch=P/'output-review-r5'/filename;after=json.loads(patch.read_text(encoding='utf-8')) if patch.is_file() else base;src=json.loads((handoff/batch['file']).read_text(encoding='utf-8'));assert len(base)==len(after)==len(src)
 if patch.is_file():patched_batches.append(bid)
 for a,b,s in zip(base,after,src):
  assert a==baseflat[a['id']], 'Round1-4 baseline changed'
  if b['id'] in seen:errors.append({'id':b['id'],'error':'DUPLICATE'})
  seen.add(b['id'])
  for k in ['id','key','asset','segment_index','source','source_sha256','context','candidate_tokens','batch']:
   if b.get(k)!=s.get(k):errors.append({'id':s['id'],'error':'IMMUTABLE','field':k})
  if pattern.findall(b['thai'])!=pattern.findall(s['source']):errors.append({'id':s['id'],'error':'TOKEN_SEQUENCE'})
  for c in ['\n','\r','\t','\\n','%']:
   if b['thai'].count(c)!=s['source'].count(c):errors.append({'id':s['id'],'error':'CONTROL_COUNT','control':repr(c)})
  if set(a['flags'])-set(b['flags']):errors.append({'id':s['id'],'error':'FLAGS_REMOVED'})
  added.update(set(b['flags'])-set(a['flags']))
  if any(c in b['thai'] for c in ['\u200b','\u200c','\u200d','\ufeff','\ufffd']) and not any(c in s['source'] for c in ['\u200b','\u200c','\u200d','\ufeff','\ufffd']):errors.append({'id':s['id'],'error':'NEW_INVISIBLE_OR_REPLACEMENT'})
  if b['status'] not in ['TRANSLATED_PENDING_REVIEW','KEEP_AS_SOURCE_PENDING_REVIEW']:errors.append({'id':s['id'],'error':'STATUS'})
  if b['status']=='KEEP_AS_SOURCE_PENDING_REVIEW' and b['thai']!=b['source']:errors.append({'id':s['id'],'error':'FALSE_IDENTITY'})
  if a['thai']!=b['thai']:
   changed.append(b['id']);f=fixmap.get(b['id']);assert f and f['before']==a['thai'] and f['after']==b['thai']
   assert f['batch']==bid and f['source']==s['source']
   assert f['status_before']==a['status'] and f['status_after']==b['status']
   assert f['flags_before']==a['flags'] and f['flags_after']==b['flags']
  elif a!=b:errors.append({'id':s['id'],'error':'UNREPORTED_METADATA_ONLY_CHANGE'})
  rows.append(b)
assert set(changed)==set(fixmap) and len(patched_batches)==62
assert len(list((P/'output-review-r5').glob('FRESH-*.th.json')))==62
assert len(rows)==len(seen)==15677
report={'records':len(rows),'batches':171,'changed_rows':len(changed),'changed_batches':len(patched_batches),'status_counts':dict(Counter(x['status'] for x in rows)),'added_flags':dict(added),'errors':errors,'baseline_unchanged':True,'word_tam_records':sum('ต่ำ' in x['thai'] for x in rows),'runtime':'NOT_RUN','full_language_review':False}
(R/'reports/claude-review-r5-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
if not errors:(P/'all-records-review-r5.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=True))
