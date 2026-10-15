"""Stage fallback-only comparison probe; keep English font mapping/material identities."""
import hashlib
import json
from pathlib import Path
import UnityPy
ROOT=Path(__file__).resolve().parents[1]
UnityPy.config.FALLBACK_UNITY_VERSION='2020.3.47f1'
base=ROOT/'local/prototype/probe-001'
out=ROOT/'local/prototype/probe-002'
out.mkdir(parents=True,exist_ok=True)
game=ROOT.parent/'TPC_Data/StreamingAssets/aa/StandaloneWindows64'
manifest=json.loads((base/'manifest.json').read_text())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
for f in manifest['files']:
    assert sha(game/f['name'])==f['original_sha256'], 'Restore originals before building'
    assert sha(base/f['name'])==f['probe_sha256'], 'Base probe has changed'
name='fonts_assets_all.bundle'
env=UnityPy.load(str(base/name))
dynamic=next(o for o in env.objects if o.type.name=='MonoBehaviour' and o.read_typetree().get('m_Name')=='NotoSans_Arabic_Dynamic')
modified=[]
for o in env.objects:
    if o.type.name!='MonoBehaviour' or o.path_id==dynamic.path_id: continue
    t=o.read_typetree()
    if 'm_CharacterTable' not in t: continue
    assert o.assets_file is dynamic.assets_file
    refs=t.setdefault('m_FallbackFontAssetTable',[])
    ref={'m_FileID':0,'m_PathID':dynamic.path_id}
    if ref not in refs: refs.append(ref)
    o.save_typetree(t); modified.append(t['m_Name'])
(out/name).write_bytes(next(iter(env.files.values())).save())
name='localisation_assets_localisationenglish.bundle'
original=UnityPy.load(str(game/name))
font_map=next(o.read().m_Script for o in original.objects if o.type.name=='TextAsset' and o.read().m_Name=='I2LS_Fonts')
env=UnityPy.load(str(base/name))
obj=next(o for o in env.objects if o.type.name=='TextAsset' and o.read().m_Name=='I2LS_Fonts')
d=obj.read();d.m_Script=font_map;d.save()
(out/name).write_bytes(next(iter(env.files.values())).save())
# Verify exact map and all 50 translations after reload; no render claim.
env=UnityPy.load(str(out/name))
assets={o.read().m_Name:o.read().m_Script for o in env.objects if o.type.name=='TextAsset'}
assert assets['I2LS_Fonts']==font_map
rows=json.loads((ROOT/'local/translations/PILOT-001.th.r3.json').read_text(encoding='utf-8'))
for r in rows: assert assets[r['asset']].split('[i2t]')[r['segment_index']]==r['key']+'='+r['thai']
fonts=UnityPy.load(str(out/'fonts_assets_all.bundle'))
verified=0
for o in fonts.objects:
    if o.type.name=='MonoBehaviour':
        t=o.read_typetree()
        if t.get('m_Name') in modified:
            assert {'m_FileID':0,'m_PathID':dynamic.path_id} in t['m_FallbackFontAssetTable'];verified+=1
assert verified==len(modified)
m={'probe':'probe-002','installed':False,'runtime_status':'NOT_RUN',
   'strategy':'Keep original English font mappings and materials; append reused Thai dynamic slot as last TMP fallback.',
   'modified_fallback_assets':modified,'translations_reloaded':len(rows),'original_font_mapping_reloaded':True,
   'limits':'Dropdown cause unconfirmed: comparison probe tests primary-font remapping hypothesis. No original Settings A/B evidence yet.',
   'files':[{'name':f['name'],'original_sha256':f['original_sha256'],'probe_sha256':sha(out/f['name'])} for f in manifest['files']]}
(out/'manifest.json').write_text(json.dumps(m,indent=2),encoding='utf-8')
(ROOT/'reports/probe-002-build.json').write_text(json.dumps(m,indent=2),encoding='utf-8')
print(json.dumps({'fallback_assets_verified':verified,'translations_verified':len(rows),'installed':False}))
