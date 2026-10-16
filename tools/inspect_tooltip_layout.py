"""Read tooltip prefab components and local references without editing assets."""
import hashlib
import json
from pathlib import Path
import UnityPy
ROOT=Path(__file__).resolve().parents[1]
UnityPy.config.FALLBACK_UNITY_VERSION='2020.3.47f1'
p=ROOT.parent/'TPC_Data/StreamingAssets/aa/StandaloneWindows64/ui-prefabs-general_assets_all.bundle'
env=UnityPy.load(str(p)); objects={o.path_id:o for o in env.objects}
rows=[]
def readref(ref):
    if not ref or ref.get('m_FileID')!=0 or not ref.get('m_PathID'):return None
    o=objects.get(ref['m_PathID'])
    return o.read_typetree() if o else None
for o in env.objects:
    if o.type.name!='GameObject':continue
    g=o.read()
    if not g.m_Name.startswith('UI_General_P_Tooltip_Main_PC_arrow'):continue
    entry={'name':g.m_Name,'root_id':o.path_id,'components':[]}
    for c in g.m_Component:
        obj=c.component.deref(); t=obj.read_typetree()
        if obj.type.name=='RectTransform':entry['root_rect']={k:t[k] for k in ['m_SizeDelta','m_AnchorMin','m_AnchorMax','m_Pivot']}
        if '_text' not in t:continue
        item={'controller_id':obj.path_id,'text_ref':t['_text'],'layout_ref':t.get('_layoutGroup')}
        text=readref(t['_text']); layout=readref(t.get('_layoutGroup'))
        if text:
            item['text_config']={k:v for k,v in text.items() if k in ['m_text','m_fontSize','m_fontSizeBase','m_enableAutoSizing','m_TextWrappingMode','m_enableWordWrapping','m_overflowMode','m_isRichText','m_margin']}
            go=readref(text.get('m_GameObject'))
            if go:
                for comp in go.get('m_Component',[]):
                    ref=comp.get('component',comp);child=readref(ref)
                    if child and 'm_SizeDelta' in child:item['text_rect']={k:child[k] for k in ['m_SizeDelta','m_AnchorMin','m_AnchorMax','m_Pivot']}
        if layout:
            item['layout_config']={k:v for k,v in layout.items() if k!='m_GameObject' and k!='m_Script'}
            fitter=readref(layout.get('_contentSizeFitter'))
            if fitter:item['fitter_config']={k:v for k,v in fitter.items() if k not in ['m_GameObject','m_Script']}
        entry['components'].append(item)
    rows.append(entry)
report={'bundle':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'prefabs':rows,
 'limits':'Serialized raw settings only. Numeric enums and custom resize modes not interpreted. Runtime prefab binding and overrides unverified.'}
(ROOT/'reports/tooltip-layout-audit.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps({'prefabs':len(rows),'names':[r['name'] for r in rows]}))
