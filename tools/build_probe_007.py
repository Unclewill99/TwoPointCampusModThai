"""Tag-free English length controls; serialized scan with explicit read errors."""
import hashlib
import json
from pathlib import Path
import UnityPy
ROOT=Path(__file__).resolve().parents[1]
game=ROOT.parent/'TPC_Data/StreamingAssets/aa/StandaloneWindows64'
base=ROOT/'local/prototype/probe-003'
UnityPy.config.FALLBACK_UNITY_VERSION='2020.3.47f1'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
scan={'matches':[],'read_errors':[],'limits':'Only direct string-valued fields searched in two bundles; absence is not proof of missing runtime binding.'}
for name in ['ui-frontend-prefabs_assets_all.bundle','ui-prefabs-general_assets_all.bundle']:
    for o in UnityPy.load(str(game/name)).objects:
        if o.type.name!='MonoBehaviour':continue
        try:t=o.read_typetree()
        except Exception as exc:
            scan['read_errors'].append({'bundle':name,'path_id':o.path_id,'error':str(exc)});continue
        hits={k:v for k,v in t.items() if isinstance(v,str) and 'resolution' in v.lower()}
        if hits:scan['matches'].append({'bundle':name,'path_id':o.path_id,'matching_fields':hits})
(ROOT/'reports/settings-tooltip-binding-scan.json').write_text(json.dumps(scan,indent=2),encoding='utf-8')
bm=json.loads((base/'manifest.json').read_text())
source=json.loads((ROOT/'local/source/all-english.json').read_text(encoding='utf-8'))
key='UI/Settings/Tooltips/Resolution'
original=next(r['source'] for r in source if r['asset']=='I2LS_UI_Settings' and r['key']==key)
lines=original.split('\n');assert len(lines)==3
variants={'probe-007-short':original,'probe-007-long':'\n'.join([lines[0],('This is a readable English sentence with ordinary spaces. '*12).strip(),lines[2]])}
reports=[]
for rev,text in variants.items():
    out=ROOT/'local/prototype'/rev;out.mkdir(parents=True,exist_ok=True)
    for f in bm['files']:
        assert sha(base/f['name'])==f['probe_sha256'];assert sha(game/f['name'])==f['original_sha256']
    name='localisation_assets_localisationenglish.bundle';env=UnityPy.load(str(base/name))
    def assets(e):return {o.read().m_Name:o.read().m_Script for o in e.objects if o.type.name=='TextAsset'}
    before=assets(env)
    o=next(o for o in env.objects if o.type.name=='TextAsset' and o.read().m_Name=='I2LS_UI_Settings')
    d=o.read();parts=d.m_Script.split('[i2t]');idx=[i for i,p in enumerate(parts) if p.split('=',1)[0]==key];assert len(idx)==1
    parts[idx[0]]=key+'='+text;d.m_Script='[i2t]'.join(parts);d.save()
    (out/name).write_bytes(next(iter(env.files.values())).save());(out/'fonts_assets_all.bundle').write_bytes((base/'fonts_assets_all.bundle').read_bytes())
    after=assets(UnityPy.load(str(out/name)))
    for a in before:
        if a!='I2LS_UI_Settings':assert before[a]==after[a]
    old=before['I2LS_UI_Settings'].split('[i2t]');new=after['I2LS_UI_Settings'].split('[i2t]')
    assert len(old)==len(new)
    changed=[i for i,(a,b) in enumerate(zip(old,new)) if a!=b]
    assert changed==([] if rev.endswith('short') else idx)
    assert text.count('\n')==2 and '<' not in text and '[i2t]' not in text
    diag={'key':key,'text':text,'lines':text.split('\n'),'LF_indexes':[i for i,c in enumerate(text) if c=='\n'],'status':'NOT_RUN'}
    (out/'diagnostic-map.json').write_text(json.dumps(diag,indent=2),encoding='utf-8')
    m={'probe':rev,'installed':False,'runtime_status':'NOT_RUN','changed_segments':len(changed),'diagnostic_map_sha256':sha(out/'diagnostic-map.json'),'limits':'English-only control; runtime bounds and automatic wrapping unverified.',
       'files':[{'name':f['name'],'original_sha256':f['original_sha256'],'probe_sha256':sha(out/f['name'])} for f in bm['files']]}
    (out/'manifest.json').write_text(json.dumps(m,indent=2),encoding='utf-8');reports.append(m)
(ROOT/'reports/probe-007-build.json').write_text(json.dumps({'variants':reports,'binding_matches':len(scan['matches']),'scan_read_errors':len(scan['read_errors'])},indent=2),encoding='utf-8')
print(json.dumps({'built':list(variants),'binding_matches':len(scan['matches']),'read_errors':len(scan['read_errors']),'installed':False}))
