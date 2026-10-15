"""Inventory serialized TMP character tables; does not assert dynamic runtime coverage."""
import json
from pathlib import Path
import UnityPy
ROOT = Path(__file__).resolve().parents[1]
UnityPy.config.FALLBACK_UNITY_VERSION = '2020.3.47f1'
env = UnityPy.load(str(ROOT.parent / 'TPC_Data/StreamingAssets/aa/StandaloneWindows64/fonts_assets_all.bundle'))
fonts, errors = [], []
for obj in env.objects:
    if obj.type.name != 'MonoBehaviour':
        continue
    try:
        t = obj.read_typetree()
        if 'm_CharacterTable' not in t:
            continue
        chars = [c.get('m_Unicode') for c in t['m_CharacterTable']]
        fonts.append({'name':t.get('m_Name'), 'path_id':obj.path_id,
                      'characters':len(chars), 'thai_codepoints':[c for c in chars if isinstance(c,int) and 0x0E00<=c<=0x0E7F],
                      'atlas_population_mode_raw':t.get('m_AtlasPopulationMode'),
                      'source_font':t.get('m_SourceFontFile'),
                      'fallbacks':t.get('m_FallbackFontAssetTable'),
                      'multi_atlas':t.get('m_IsMultiAtlasTexturesEnabled')})
    except Exception as exc:
        errors.append({'path_id':obj.path_id,'error':str(exc)})
r={'fonts':fonts,'errors':errors,'limits':'Serialized TMP character tables in Campus fonts bundle only. No dynamic source-font cmap or runtime coverage proof.'}
(ROOT/'reports/campus-font-audit.json').write_text(json.dumps(r,indent=2),encoding='utf-8')
print(json.dumps({'TMP_assets':len(fonts),'assets_with_serialized_thai':sum(bool(f['thai_codepoints']) for f in fonts),'errors':len(errors)}))
