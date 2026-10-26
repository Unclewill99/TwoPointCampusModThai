"""WO-006 Q-A: read frozen005 localisation without changing text. Outputs NEW
reports/sara-am-006-census.json and preservation-before JSON (exclusive create).
Protected inputs: original17 plus lig-001 bundles/manifest. No builds/installation.
"""
from pathlib import Path
from collections import Counter,defaultdict
import hashlib,json,re,unicodedata
import UnityPy
R=Path(__file__).resolve().parents[1]
def sha(p):
    with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
out=R/'reports/sara-am-006-census.json';pres=R/'reports/sara-am-006-preservation-before.json'
assert not out.exists() and not pres.exists()
prior=json.loads((R/'reports/sara-am-lig-001-build.json').read_bytes())
paths=[R.parent/p for p in prior['verification']['protected_before']]
paths += sorted(p for p in (R/'local/prototype/probe-sara-am-lig-001').iterdir() if p.is_file())
protected={str(p.relative_to(R.parent)):{'size':p.stat().st_size,'sha256':sha(p)} for p in paths}
assert len(protected)==21
for p,v in prior['verification']['protected_before'].items():assert protected[p]['sha256']==v['sha256']
pres.open('x',encoding='utf-8').write(json.dumps(protected,indent=2))
p=R/'local/prototype/fresh-translation-005/localisation_assets_localisationenglish.bundle'
UnityPy.config.FALLBACK_UNITY_VERSION='2020.3.47f1'
records=[];assets=[]
for o in UnityPy.load(str(p)).objects:
    if o.type.name!='TextAsset':continue
    a=o.read();s=a.m_Script;assert isinstance(s,str)
    count=0
    for i,part in enumerate(s.split('[i2t]')):
        if not part:continue
        assert '=' in part
        key,text=part.split('=',1);count+=1
        records.append({'id':a.m_Name+'::'+key+'::segment-'+str(i),'asset':a.m_Name,'segment_index':i,'key':key,'text':text})
    assets.append({'asset':a.m_Name,'records':count})
assert len(records)==15677 and len({r['id'] for r in records})==15677
known=json.loads((R/'local/source/all-english.json').read_bytes());assert {r['id'] for r in records}=={r['id'] for r in known}
clusters=defaultdict(list);other=defaultdict(list);all_am=0;records_with_am=set();counts=Counter()
pattern=re.compile('[\u0e01-\u0e2e][\u0e48-\u0e4b]\u0e33')
def occurrence(row,start,end):
    s=row['text'];return {k:row[k] for k in ['id','asset','segment_index','key']}|{'offset':start,'line_index':s[:start].count('\n'),'column':len(s[:start].rsplit('\n',1)[-1]),'context':s[max(0,start-28):min(len(s),end+28)],'wrapping_context':{'explicit_lf_in_record':'\n' in s,'literal_backslash_n':'\\n' in s,'br_tag':bool(re.search(r'<br\s*/?>',s,re.I)),'nobr_tag':'<nobr' in s.lower(),'zwsp':'\u200b' in s,'word_joiner':'\u2060' in s,'record_characters':len(s),'actual_runtime_wrap':'UNKNOWN'}}
for row in records:
    s=row['text'];matched_am=set()
    for m in pattern.finditer(s):clusters[m.group()].append(occurrence(row,m.start(),m.end()));matched_am.add(m.end()-1)
    for i,c in enumerate(s):
        if c!='\u0e33':continue
        all_am+=1;records_with_am.add(row['id'])
        if i in matched_am:counts['direct_consonant_tone_am']+=1;continue
        j=i-1
        while j>=0 and unicodedata.category(s[j]).startswith('M'):j-=1
        if j<i-1:
            seq=s[j:i+1] if j>=0 else s[:i+1]
            other[seq].append(occurrence(row,max(j,0),i+1));counts['other_mark_preceded_am']+=1
        else:counts['not_directly_mark_preceded_am']+=1
def entry(seq,items):return {'text':seq,'codepoints':[f'U+{ord(c):04X}' for c in seq],'count':len(items),'distinct_records':len({x['id'] for x in items}),'segments':sorted({x['id'] for x in items}),'samples':items[:3],'occurrences':items}
report={'wo':'WO-SARA-AM-006','label':'VERIFIED','corpus':'actual frozen005 bundle values; record ID set matched extracted15677 inventory','bundle_sha256':sha(p),'records_scanned':len(records),'assets':assets,'atomic_sara_am_total':all_am,'records_with_sara_am':len(records_with_am),'classification_counts':dict(counts),'direct_base_tone_am_clusters':[entry(k,v) for k,v in sorted(clusters.items(),key=lambda x:(-len(x[1]),x[0]))],'other_mark_preceded_sara_am':[entry(k,v) for k,v in sorted(other.items(),key=lambda x:(-len(x[1]),x[0]))],'distinct_direct_clusters':len(clusters),'limits':{'VERIFIED':'Counts include repeated occurrences, not only unique strings. Zero normalization/text changes. Match operates on stored codepoints and values, not localization keys.','INFERRED':'Direct consonant-tone-am clusters share structural risk with accepted ต่ำ defect, but no defect claim for every cluster.','UNKNOWN':'Actual per-cluster visual defect severity, hidden contexts and runtime line wrapping. Mark runs split by rich-text tags are not treated as contiguous clusters.'}}
assert sum(counts.values())==all_am
out.open('x',encoding='utf-8').write(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({k:report[k] for k in ['records_scanned','atomic_sara_am_total','classification_counts','distinct_direct_clusters']}|{'clusters':[(x['text'],x['count']) for x in report['direct_base_tone_am_clusters']],'other':[(x['text'],x['count']) for x in report['other_mark_preceded_sara_am']]}))
