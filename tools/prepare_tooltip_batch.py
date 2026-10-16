"""Prepare actual Settings tooltip batch; no translation or game mutation."""
import copy,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
source=ROOT/'local/source/all-english.json'
rows=json.loads(source.read_text(encoding='utf-8'))
selected=[copy.deepcopy(r) for r in rows if r['asset']=='I2LS_UI_Settings' and r['key'].startswith('UI/Settings/Tooltips/')]
assert len(selected)==20 and len({r['id'] for r in selected})==20
for r in selected:
 assert hashlib.sha256(r['source'].encode()).hexdigest()==r['source_sha256']
 r['batch']='TOOLTIPS-001';r['thai']='';r['status']='UNTRANSLATED'
 r['context']={'key_path':r['key'],'screen_hint':'Settings > Video candidate tooltip; actual visibility varies; CharacterLimits may differ.',
               'observed_readable_original':r['key'].split('/')[-1] in ['Resolution','MaxFPS','AntialiasingMode'],
               'layout_note':'Experimental bounded arrowLeft text width requested 800 units; not universal runtime coverage or a character limit.'}
dest=ROOT/'local/source/TOOLTIPS-001.json'
if dest.exists():assert json.loads(dest.read_text(encoding='utf-8'))==selected,'Refusing to replace changed batch'
else:dest.write_text(json.dumps(selected,ensure_ascii=False,indent=2),encoding='utf-8')
report={'batch':'TOOLTIPS-001','records':20,'source_corpus_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'batch_sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'ids':[r['id'] for r in selected],
        'with_tokens':[r['id'] for r in selected if r['candidate_tokens']],
        'limits':'Source extraction only. Existence in corpus does not prove UI activation. No translation or build approved.'}
(ROOT/'reports/tooltips-001-preparation.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps({'records':20,'token_bearing_records':len(report['with_tokens']),'game_mutation':False}))
