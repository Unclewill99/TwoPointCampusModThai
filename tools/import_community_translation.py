"""Import third-party translations locally; preserve reviewed project rows; never install."""
from pathlib import Path
from zipfile import ZipFile
from collections import Counter,defaultdict
import hashlib,json,re
import UnityPy
ROOT=Path(__file__).resolve().parents[1]
archive=Path(r'C:/Users/udomp/Downloads/Two Point Campus MOD Thai AI-1-MODV1-0-1742896937.zip')
out=ROOT/'local/imports/community-ai-v1';out.mkdir(parents=True,exist_ok=True)
UnityPy.config.FALLBACK_UNITY_VERSION='2020.3.47f1'
with ZipFile(archive) as z:
 name=next(n for n in z.namelist() if n.endswith('/localisation_assets_localisationenglish.bundle'))
 data=z.read(name)
 imported=defaultdict(list)
 for obj in UnityPy.load(data).objects:
  if obj.type.name!='TextAsset':continue
  a=obj.read();t=a.m_Script
  if isinstance(t,bytes):t=t.decode('utf-8')
  for i,part in enumerate(t.split('[i2t]')):
   if not part:continue
   if '=' not in part:raise ValueError('Malformed imported segment')
   k,v=part.split('=',1);imported[(a.m_Name,k)].append({'thai':v,'segment_index':i})
source=json.loads((ROOT/'local/source/all-english.json').read_text(encoding='utf-8'))
counts=Counter((r['asset'],r['key']) for r in source)
own={}
for f in ['PILOT-001.th.r3.json','TOOLTIPS-001.th.r2.json']:
 for r in json.loads((ROOT/'local/translations'/f).read_text(encoding='utf-8')):own[r['id']]=r
pattern=r'\{[^{}]+\}|<[^<>]+>'
merged=[];issues=[];stats=Counter()
for r in source:
 row=dict(r);key=(r['asset'],r['key']);matches=imported.get(key,[])
 if r['id'] in own:
  row.update(thai=own[r['id']]['thai'],status='PROJECT_REVIEWED_BASELINE',provenance='project');stats['project_preserved']+=1
 elif len(matches)!=1 or counts[key]!=1:
  row.update(thai=r['source'],status='ENGLISH_FALLBACK',provenance='source');stats['missing_or_ambiguous']+=1
 else:
  v=matches[0]['thai'];flags=[]
  if Counter(re.findall(pattern,v))!=Counter(re.findall(pattern,r['source'])):flags.append('TOKEN_OR_TAG_MISMATCH')
  if r['source'].strip() and not v.strip():flags.append('EMPTY_TRANSLATION')
  if '\ufffd' in v:flags.append('REPLACEMENT_CHARACTER')
  if flags:
   row.update(thai=r['source'],status='QUARANTINED_ENGLISH_FALLBACK',provenance='source');issues.append({'id':r['id'],'flags':flags,'imported_thai':v});stats['quarantined']+=1
  else:
   row.update(thai=v,status='IMPORTED_UNREVIEWED',provenance='community-ai-v1');stats['imported']+=1
   if re.search('[\u0e00-\u0e7f]',v):stats['imported_with_thai']+=1
   if v==r['source']:stats['imported_unchanged_english']+=1
 merged.append(row)
extra=set(imported)-set(counts)
(out/'merged-draft.json').write_text(json.dumps(merged,ensure_ascii=False,indent=2),encoding='utf-8')
(out/'quarantine.json').write_text(json.dumps(issues,ensure_ascii=False,indent=2),encoding='utf-8')
report={'archive_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'localisation_sha256':hashlib.sha256(data).hexdigest(),'source_records':len(source),'imported_records':sum(map(len,imported.values())),'extra_asset_keys':len(extra),'counts':dict(stats),'installed':False,'limits':'Draft only. Token/tag comparison is heuristic. No language/runtime approval. Imported font not used. Redistribution permission not established; keep imported text local.'}
(ROOT/'reports/community-import-audit.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))
