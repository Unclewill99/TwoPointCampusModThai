"""Validate Claude output as untrusted data against frozen handoff; never install."""
from pathlib import Path,PurePosixPath
from zipfile import ZipFile
from collections import Counter
import json,re,hashlib
R=Path(__file__).resolve().parents[1];archive=Path(r'C:/Users/udomp/Downloads/CLAUDE-FULL-RETRANSLATION-001-output.zip')
handoff=R/'local/handoffs/CLAUDE-FULL-RETRANSLATION-001';manifest=json.loads((handoff/'manifest.json').read_text());out=R/'local/translations/CLAUDE-FULL-RETRANSLATION-001';out.mkdir(parents=True,exist_ok=True)
errors=[];warnings=[];allrows=[];counts=Counter();flags=Counter();seen=set()
immutable=['id','key','asset','segment_index','source','source_sha256','context','candidate_tokens','batch']
pattern=re.compile(r'\{[^{}]+\}|<[^<>]+>|\[[^\[\]]+\]|%(?:\d+\$)?[-+#0]*\d*(?:\.\d+)?[sdifouxXeEgGcpaA%]')
with ZipFile(archive) as z:
 names=z.namelist();assert len(names)==len(set(names))
 for i in z.infolist():
  p=PurePosixPath(i.filename)
  assert not p.is_absolute() and '..' not in p.parts and '\\' not in i.filename
  if i.is_dir():continue
  assert i.file_size<25_000_000 and p.suffix=='.json'
  target=out.joinpath(*p.parts);target.parent.mkdir(parents=True,exist_ok=True);data=z.read(i)
  if target.exists():assert target.read_bytes()==data
  else:target.write_bytes(data)
 for b in manifest['batches']:
  input_path=handoff/b['file'];assert hashlib.sha256(input_path.read_bytes()).hexdigest()==b['sha256']
  source=json.loads(input_path.read_text(encoding='utf-8'));path=out/'output'/(b['batch']+'.th.json')
  if not path.is_file():errors.append({'batch':b['batch'],'error':'MISSING_BATCH'});continue
  rows=json.loads(path.read_text(encoding='utf-8'))
  if len(rows)!=len(source):errors.append({'batch':b['batch'],'error':'COUNT_MISMATCH'});continue
  for i,(s,t) in enumerate(zip(source,rows)):
   rid=t.get('id');tag={'id':rid,'batch':b['batch'],'index':i}
   for k in immutable:
    if t.get(k)!=s.get(k):errors.append(dict(tag,error='IMMUTABLE_FIELD',field=k))
   if rid in seen:errors.append(dict(tag,error='DUPLICATE_ID'))
   seen.add(rid);thai=t.get('thai');original=s['source']
   if not isinstance(thai,str):errors.append(dict(tag,error='NON_STRING'));continue
   if original.strip() and not thai.strip():errors.append(dict(tag,error='EMPTY'))
   if Counter(pattern.findall(original))!=Counter(pattern.findall(thai)):errors.append(dict(tag,error='TOKEN_MULTISET'))
   elif pattern.findall(original)!=pattern.findall(thai):warnings.append(dict(tag,warning='TOKEN_ORDER'))
   for literal,label in [('\n','LF'),('\r','CR'),('\t','TAB'),('\\n','LITERAL_BACKSLASH_N'),('%','PERCENT')]:
    if original.count(literal)!=thai.count(literal):errors.append(dict(tag,error=label+'_COUNT'))
   if '[i2t]' in thai:errors.append(dict(tag,error='DELIMITER'))
   if any(x in thai for x in ['ไม่เมาไม่แปล','จัดทำและแจกฟรีโดย','โรมานอฟสกี้']):errors.append(dict(tag,error='PROMO_MARKER'))
   if '\ufffd' in thai and '\ufffd' not in original:errors.append(dict(tag,error='NEW_REPLACEMENT_CHARACTER'))
   if any(c in thai for c in ['\u200b','\u200c','\u200d','\ufeff']):warnings.append(dict(tag,warning='INVISIBLE_CONTROL'))
   if t.get('status') not in ['TRANSLATED_PENDING_REVIEW','KEEP_AS_SOURCE_PENDING_REVIEW']:errors.append(dict(tag,error='STATUS',value=t.get('status')))
   if t.get('status')=='KEEP_AS_SOURCE_PENDING_REVIEW' and (thai!=original or not t.get('translator_note')):errors.append(dict(tag,error='INVALID_KEEP_AS_SOURCE'))
   counts[t.get('status')]+=1;flags.update(t.get('flags',[]));allrows.append(t)
 if len([n for n in names if re.fullmatch(r'output/FRESH-\d{3}\.th\.json',n)])!=171:errors.append({'error':'BATCH_FILE_COUNT'})
 if len(allrows)!=15677:errors.append({'error':'TOTAL_COUNT','actual':len(allrows)})
 progress=json.loads((out/'output/PROGRESS.json').read_text(encoding='utf-8'));glossary=json.loads((out/'output/GLOSSARY_FRESH_v1.json').read_text(encoding='utf-8'));uncertain=json.loads((out/'output/UNCERTAIN_ITEMS.json').read_text(encoding='utf-8'))
 for g in glossary:
  missing=[x for x in g.get('evidence_ids',[]) if x not in seen]
  if missing:warnings.append({'warning':'GLOSSARY_UNKNOWN_EVIDENCE','term':g.get('source_term'),'ids':missing})
 for u in uncertain:
  if u.get('id') not in seen:errors.append({'error':'UNCERTAIN_UNKNOWN_ID','id':u.get('id')})
(out/'all-records.json').write_text(json.dumps(allrows,ensure_ascii=False,indent=2),encoding='utf-8')
report={'archive_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'records':len(allrows),'unique_ids':len(seen),'batches':len(manifest['batches']),'counts':dict(counts),'flags':dict(flags),'glossary_entries':len(glossary),'uncertain_entries':len(uncertain),'word_tam_records':sum('ต่ำ' in t['thai'] for t in allrows),'errors':errors,'warnings':warnings,'installed':False,'language_review':'NOT_DONE','runtime':'NOT_RUN','limits':'Heuristic token/markup checks do not prove grammar, semantic fidelity, font behavior, plural routing or human review.'}
(R/'reports/claude-full-retranslation-001-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps({k:report[k] for k in ['records','unique_ids','batches','counts','glossary_entries','uncertain_entries','word_tam_records']},ensure_ascii=True));print('errors',len(errors),'warnings',len(warnings));print(json.dumps(errors[:12],ensure_ascii=True));print(json.dumps(warnings[:8],ensure_ascii=True))
