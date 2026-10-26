"""WO-004 read-only targeted asset inspection. Inputs: frozen005 font bundle and
existing full feature audit. Outputs: NEW reports/sara-am-004-asset-evidence.json.
No game launch, candidate build, source-font export, asset writes or normalization.
"""
from pathlib import Path
import json,hashlib,io
import UnityPy
from fontTools.ttLib import TTFont
R=Path(__file__).resolve().parents[1]
UnityPy.config.FALLBACK_UNITY_VERSION='2020.3.47f1'
p=R/'local/prototype/fresh-translation-005/fonts_assets_all.bundle'
env=UnityPy.load(str(p));report={'label':'VERIFIED','input':str(p.relative_to(R)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
for o in env.objects:
    if o.path_id==-1239755799206566947:
        t=o.read_typetree()
        report['tmp']={'path_id':o.path_id,'configuration':{k:t.get(k) for k in ['m_AtlasPopulationMode','m_AtlasWidth','m_AtlasHeight','m_AtlasPadding','m_AtlasRenderMode','m_IsMultiAtlasTexturesEnabled','m_SourceFontFile','m_fontFile','m_FaceInfo','m_ShouldReimportFontFeatures']},'glyph_count':len(t.get('m_GlyphTable',[])),'character_count':len(t.get('m_CharacterTable',[]))}
        ft=t['m_FontFeatureTable']
        report['pairs_42_82']=[x for x in ft['m_GlyphPairAdjustmentRecords'] if x['m_FirstAdjustmentRecord']['m_GlyphIndex']==42 and x['m_SecondAdjustmentRecord']['m_GlyphIndex']==82]
        report['mark_to_base_118_42']=[x for x in ft['m_MarkToBaseAdjustmentRecords'] if x['m_BaseGlyphID']==118 and x['m_MarkGlyphID']==42]
        report['mark_to_mark_82_42']=[x for x in ft['m_MarkToMarkAdjustmentRecords'] if x['m_BaseMarkGlyphID']==82 and x['m_CombiningMarkGlyphID']==42]
    if o.path_id==7716434233879021909:
        data=bytes(o.read_typetree()['m_FontData']);font=TTFont(io.BytesIO(data));order=font.getGlyphOrder();cmap=font.getBestCmap()
        glyphs={}
        for cp in [0xe15,0xe16,0xe17,0xe1b,0xe1d,0xe1f,0xe33,0xe48,0xe49,0xe4a,0xe4b]:
            name=cmap[cp];g=font['glyf'][name]
            glyphs[f'U+{cp:04X}']={'gid':font.getGlyphID(name),'name':name,'bounds':[getattr(g,k,None) for k in ['xMin','yMin','xMax','yMax']],'advance':font['hmtx'][name][0],'components':[x.glyphName for x in g.components] if g.isComposite() else []}
        report['font']={'sha256':hashlib.sha256(data).hexdigest(),'units_per_em':font['head'].unitsPerEm,'glyph_count':len(order),'glyphs':glyphs,'sara_am_is_composite':font['glyf'][order[82]].isComposite()}
assert 'tmp' in report and 'font' in report
(R/'reports/sara-am-004-asset-evidence.json').open('x',encoding='utf-8').write(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
