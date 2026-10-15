"""Build LOCAL experimental bundles only. Never installs or edits game originals."""
import hashlib
import io
import json
from pathlib import Path
import UnityPy
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[1]
campus = ROOT.parent/'TPC_Data/StreamingAssets/aa/StandaloneWindows64'
museum = ROOT.parent.parent/'Two Point Museum/TPM_Data/StreamingAssets/aa/StandaloneWindows64'
out = ROOT/'local/prototype/probe-001'
out.mkdir(parents=True, exist_ok=True)
def digest(data): return hashlib.sha256(data).hexdigest()
research = {'museum_fonts':[], 'limits':'Serialized evidence, not proof of runtime shaping or bundle compatibility.'}
UnityPy.config.FALLBACK_UNITY_VERSION='6000.0.63f1'
font_env=UnityPy.load(str(museum/'fonts_assets_notosansthai-medium.bundle'))
font_obj=next(o for o in font_env.objects if o.type.name=='Font')
font_tree=font_obj.read_typetree()
font_bytes=bytes(font_tree['m_FontData'])
tt=TTFont(io.BytesIO(font_bytes)); cmap=tt.getBestCmap()
research['source_font']={'name':font_tree['m_Name'],'sha256':digest(font_bytes),'tables':list(tt.keys()),'thai_cmap_entries':sum(0xE00<=c<=0xE7F for c in cmap)}
for path in museum.glob('fonts_assets_notosans_thai*.bundle'):
    for o in UnityPy.load(str(path)).objects:
        if o.type.name!='MonoBehaviour': continue
        t=o.read_typetree()
        research['museum_fonts'].append({'bundle':path.name,'name':t.get('m_Name'),'path_id':o.path_id,
            'character_count':len(t.get('m_CharacterTable',[])),
            'atlas_population_mode_raw':t.get('m_AtlasPopulationMode'),'source_font_ref':t.get('m_SourceFontFile'),
            'fallbacks':t.get('m_FallbackFontAssetTable'),
            'feature_counts':{k:len(v) for k,v in t.get('m_FontFeatureTable',{}).items() if isinstance(v,list)}})
loc=UnityPy.load(str(museum/'localisation_assets_localisationthai.bundle'))
mapping=next(o.read().m_Script for o in loc.objects if o.type.name=='TextAsset' and o.read().m_Name=='I2LS_Fonts')
research['museum_font_mapping_values']=sorted(set(p.split('=',1)[1] for p in mapping.split('[i2t]') if '=' in p))
(ROOT/'reports/museum-thai-font-research.json').write_text(json.dumps(research,indent=2),encoding='utf-8')

UnityPy.config.FALLBACK_UNITY_VERSION='2020.3.47f1'
fonts_path=campus/'fonts_assets_all.bundle'
fonts=UnityPy.load(str(fonts_path))
arabic=next(o for o in fonts.objects if o.type.name=='Font' and o.read_typetree()['m_Name']=='NotoSansArabic-Regular')
t=arabic.read_typetree(); t['m_FontData']=list(font_bytes); arabic.save_typetree(t)
# Retain asset identities/GUID references; reuse existing dynamic slot experimentally.
font_output=out/fonts_path.name
font_output.write_bytes(next(iter(fonts.files.values())).save())
english_path=campus/'localisation_assets_localisationenglish.bundle'
english=UnityPy.load(str(english_path))
pilot=json.loads((ROOT/'local/translations/PILOT-001.th.r3.json').read_text(encoding='utf-8'))
by_position={(r['asset'],r['segment_index']):r for r in pilot}
changed=0
for o in english.objects:
    if o.type.name!='TextAsset': continue
    d=o.read(); parts=d.m_Script.split('[i2t]'); dirty=False
    for i,part in enumerate(parts):
        if '=' not in part: continue
        key,value=part.split('=',1)
        if d.m_Name=='I2LS_Fonts':
            parts[i]=key+'=NotoSans_Arabic_Dynamic'; dirty=True
        elif (d.m_Name,i) in by_position:
            r=by_position[d.m_Name,i]
            assert r['key']==key and r['source']==value
            parts[i]=key+'='+r['thai']; changed+=1; dirty=True
    if dirty:
        d.m_Script='[i2t]'.join(parts); d.save()
assert changed==50
english_output=out/english_path.name
english_output.write_bytes(next(iter(english.files.values())).save())
# Reload written bundles and verify all 50 exact translated segments and TTF bytes.
reloaded=UnityPy.load(str(font_output))
embedded=next(o.read_typetree()['m_FontData'] for o in reloaded.objects if o.type.name=='Font' and o.read_typetree()['m_Name']=='NotoSansArabic-Regular')
assert bytes(embedded)==font_bytes
checked=0
for o in UnityPy.load(str(english_output)).objects:
    if o.type.name!='TextAsset': continue
    d=o.read(); parts=d.m_Script.split('[i2t]')
    for (asset,i),r in by_position.items():
        if asset==d.m_Name:
            assert parts[i]==r['key']+'='+r['thai']; checked+=1
assert checked==50
chars=set(''.join(r['thai'] for r in pilot))
missing=sorted(ord(c) for c in chars if not c.isspace() and ord(c) not in cmap)
manifest={'probe':'probe-001','installed':False,'runtime_status':'NOT_RUN','translated_records_reloaded':checked,
 'strategy':'Replace embedded Arabic source-font bytes with Museum Thai TTF, retain identities, map English font terms to existing Arabic dynamic TMP slot. Experimental only.',
 'missing_pilot_cmap_codepoints':missing,'risks':['Addressables hash/CRC may reject modified bundles','Dynamic source font GUID resolution not runtime-verified','Campus mark positioning and Thai wrapping may be insufficient','Thai source font may lack Latin or symbol coverage; existing fallback behavior unverified'],
 'files':[{'name':p.name,'original_sha256':digest(p.read_bytes()),'probe_sha256':digest((out/p.name).read_bytes())} for p in [fonts_path,english_path]]}
(out/'manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
(ROOT/'reports/probe-001-build.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(json.dumps({'reloaded_translations':checked,'missing_cmap':missing,'runtime':'NOT_RUN','installed':False}))
