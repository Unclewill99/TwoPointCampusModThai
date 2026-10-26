"""WO-006 offline build/verify only. Inputs: frozen005, accepted font anchors,
official retained TMP source, WO006 census/preservation snapshot. Outputs NEW
probe-sara-am-glyph-001 and local/review/sara-am-006 (exclusive create).
No installation/game launch/text rewrite/cmap entry. Chrome headless renders a
local browser reference only; candidate font changes are solely appended glyph.
"""
from pathlib import Path
import copy,hashlib,io,json,base64,subprocess,struct
import UnityPy
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._g_l_y_f import Glyph,GlyphComponent
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib.sfnt import calcChecksum
R=Path(__file__).resolve().parents[1];BASE=R/'local/prototype/fresh-translation-005'
OUT=R/'local/prototype/probe-sara-am-glyph-001';REF=R/'local/review/sara-am-006'
assert not OUT.exists() and not REF.exists()
def digest(b):return hashlib.sha256(b).hexdigest()
def sha(p):return digest(p.read_bytes())
before=json.loads((R/'reports/sara-am-006-preservation-before.json').read_bytes())
def preserve():
    for p,v in before.items():assert sha(R.parent/p)==v['sha256'],p
preserve()
UnityPy.config.FALLBACK_UNITY_VERSION='2020.3.47f1'
manifest=json.loads((BASE/'manifest.json').read_bytes())
for f in manifest['files']:assert sha(BASE/f['name'])==f['probe_sha256']
fontname='fonts_assets_all.bundle';locname='localisation_assets_localisationenglish.bundle';fontid=7716434233879021909;tmpid=-1239755799206566947
env=UnityPy.load(str(BASE/fontname));fo=next(o for o in env.objects if o.path_id==fontid);to=next(o for o in env.objects if o.path_id==tmpid)
oldfonttree=fo.read_typetree();oldtmp=to.read_typetree();rawfont=bytes(oldfonttree['m_FontData'])
assert digest(rawfont)=='f9855a702e9899b9cfa1e8cb7cbf36c2c7bb6fe31ee0cd6860ae61ae012155d0'
font=TTFont(io.BytesIO(rawfont),recalcBBoxes=False,recalcTimestamp=False)
order=font.getGlyphOrder()[:];N=len(order);assert N==459
original_glyf=font.reader['glyf'];oldloca=list(font['loca'].locations);oldmetrics=dict(font['hmtx'].metrics);oldcmap=font.reader['cmap']
assert [font.getGlyphID(font.getBestCmap()[c]) for c in [0xe15,0xe48,0xe33]]==[118,42,82]
anchor=json.loads((R/'reports/sara-am-native-feature-audit.json').read_bytes())['gpos_mark_to_mark'][0]
assert anchor['base_mark']==59 and anchor['combining_mark']==42
am=font['glyf'][order[82]];assert [(c.glyphName,c.getComponentInfo()[1]) for c in am.components]==[(order[78],(1,0,0,1,0,0)),(order[59],(1,0,0,1,0,0))]
base_advance=oldmetrics[order[118]][0];am_advance=oldmetrics[order[82]][0]
tone_x=base_advance+anchor['font_units_base_anchor'][0]-anchor['font_units_mark_anchor'][0]
tone_y=anchor['font_units_base_anchor'][1]-anchor['font_units_mark_anchor'][1]
assert (base_advance,am_advance,tone_x,tone_y)==(641,415,612,236)
ring=font['glyf'][order[59]];tone=font['glyf'][order[42]]
ringbox=[ring.xMin+641,ring.yMin,ring.xMax+641,ring.yMax]
tonebox=[tone.xMin+tone_x,tone.yMin+tone_y,tone.xMax+tone_x,tone.yMax+tone_y]
gap=tonebox[1]-ringbox[3];assert gap==74 and ringbox[0]<=tonebox[0]<tonebox[2]<=ringbox[2]
newname='saraAm006_tomaiEkAm';g=Glyph();g.numberOfContours=-1;g.components=[]
components=[(order[118],0,0),(order[82],641,0),(order[42],tone_x,tone_y)]
for name,x,y in components:
    c=GlyphComponent();c.glyphName=name;c.x=x;c.y=y;c.flags=0x4;g.components.append(c)
g.recalcBounds(font['glyf']);coordinates,contours,_=g.getCoordinates(font['glyf'])
assert [g.xMin,g.yMin,g.xMax,g.yMax]==[60,-10,978,1083]
font.setGlyphOrder(order+[newname]);font['glyf'][newname]=g;font['hmtx'][newname]=(1056,60)
# Avoid automatic re-encoding of old composite flags. Update only limits needed
# by the appended composite; every original glyph slice is checked below.
m=font['maxp'];m.numGlyphs=N+1;m.maxCompositePoints=max(m.maxCompositePoints,len(coordinates));m.maxCompositeContours=max(m.maxCompositeContours,len(contours));m.maxComponentElements=max(m.maxComponentElements,3);m.maxComponentDepth=max(m.maxComponentDepth,2)
h=font['head'];h.xMin=min(h.xMin,g.xMin);h.yMin=min(h.yMin,g.yMin);h.xMax=max(h.xMax,g.xMax);h.yMax=max(h.yMax,g.yMax)
hh=font['hhea'];hh.advanceWidthMax=max(hh.advanceWidthMax,1056);hh.minLeftSideBearing=min(hh.minLeftSideBearing,60);hh.minRightSideBearing=min(hh.minRightSideBearing,1056-g.xMax);hh.xMaxExtent=max(hh.xMaxExtent,g.xMax)
buf=io.BytesIO();font.save(buf);newbytes=buf.getvalue();checked=TTFont(io.BytesIO(newbytes),checkChecksums=2,recalcBBoxes=False,recalcTimestamp=False)
assert checked.getGlyphOrder()[:N]==order and len(checked.getGlyphOrder())==N+1
newloca=list(checked['loca'].locations);newglyf=checked.reader['glyf']
assert newloca[:N+1]==oldloca
assert all(original_glyf[oldloca[i]:oldloca[i+1]]==newglyf[newloca[i]:newloca[i+1]] for i in range(N))
assert all(checked['hmtx'][name]==oldmetrics[name] for name in order)
assert checked.reader['hmtx'][:len(font.reader['hmtx'])]==font.reader['hmtx']
assert checked.reader['cmap']==oldcmap and all(gid<N for sub in checked['cmap'].tables for name in sub.cmap.values() for gid in [checked.getGlyphID(name)])
assert calcChecksum(newbytes)==0xB1B0AFBA
for tag,entry in checked.reader.tables.items():
    data=checked.reader[tag]
    if tag=='head':data=data[:8]+bytes(4)+data[12:]
    assert calcChecksum(data)==entry.checkSum,tag
changed_tables=[tag for tag in font.reader.keys() if font.reader[tag]!=checked.reader[tag]]
assert set(changed_tables)<={'glyf','loca','hmtx','maxp','hhea','head','post'}
assert [(c.glyphName,c.getComponentInfo()[1]) for c in checked['glyf'][newname].components]==[(n,(1,0,0,1,x,y)) for n,x,y in components]
assert checked['hmtx'][newname]==(1056,60)
records=oldtmp['m_FontFeatureTable']['m_LigatureSubstitutionRecords'];assert len(records)==9 and all(x['m_ComponentGlyphIDs'][0]!=118 for x in records)
assert not any('Lookup' in k for k in oldtmp['m_FontFeatureTable'])
assert oldtmp['m_GlyphTable']==[] and oldtmp['m_CharacterTable']==[] and oldtmp['m_AtlasPopulationMode']==1
atlas=next(o.read_typetree() for o in env.objects if o.path_id==oldtmp['m_AtlasTextures'][0]['m_PathID']);assert atlas['m_IsReadable']
source=(R/'local/review/sara-am-004/official-packages/3.2.0-pre.4/TMP_FontAsset.cs').read_text(encoding='utf-8-sig')
fn=source[source.index('internal bool TryAddGlyphInternal('):source.index('internal bool TryAddCharacterInternal(')]
assert 'TryAddGlyphToTexture(glyphIndex' in fn and 'm_GlyphTable.Add(glyph)' in fn
assert '//m_CharacterTable.Add(character);' in fn
record={'m_ComponentGlyphIDs':[118,42,82],'m_LigatureGlyphID':N}
newtmp=copy.deepcopy(oldtmp);newtmp['m_FontFeatureTable']['m_LigatureSubstitutionRecords'].append(record)
newfonttree=copy.deepcopy(oldfonttree);newfonttree['m_FontData']=list(newbytes)
fo.save_typetree(newfonttree);to.save_typetree(newtmp);bundlebytes=next(iter(env.files.values())).save()
diag='L1: ต่ำ\nL2: ต้ำ\nL3: ค่ำ\nL4: ตา ถี่\nL5: ทำ'
le=UnityPy.load(str(BASE/locname));texts=lambda e:{o.read().m_Name:o.read().m_Script for o in e.objects if o.type.name=='TextAsset'}
loc_before=texts(le);lo=next(o for o in le.objects if o.type.name=='TextAsset' and o.read().m_Name=='I2LS_Levels');locid=lo.path_id;lt=lo.read();parts=lt.m_Script.split('[i2t]');assert parts[533].startswith('Levels/Freshleigh/Level_Intro_Text=');parts[533]=parts[533].split('=',1)[0]+'='+diag;lt.m_Script='[i2t]'.join(parts);lt.save();locbytes=next(iter(le.files.values())).save()
OUT.mkdir(exist_ok=False);REF.mkdir(exist_ok=False)
for f in manifest['files']:
    n=f['name'];data=bundlebytes if n==fontname else locbytes if n==locname else (BASE/n).read_bytes();(OUT/n).open('xb').write(data)
def objects(e):return {(o.assets_file.name,str(o.path_id),o.type.name):o.get_raw_data() for o in e.objects}
diffs={}
for f in manifest['files']:
    n=f['name'];a=objects(UnityPy.load(str(BASE/n)));b=objects(UnityPy.load(str(OUT/n)));assert a.keys()==b.keys();changed=[k for k in a if a[k]!=b[k]];expected=[fontid,tmpid] if n==fontname else [locid] if n==locname else [];assert sorted(int(k[1]) for k in changed)==sorted(expected)
    diffs[n]=[{'asset':k[0],'id':int(k[1]),'type':k[2],'before_sha256':digest(a[k]),'after_sha256':digest(b[k])} for k in changed]
    if not expected:assert sha(BASE/n)==sha(OUT/n)
re=UnityPy.load(str(OUT/fontname));rt=next(o.read_typetree() for o in re.objects if o.path_id==tmpid);rf=next(o.read_typetree() for o in re.objects if o.path_id==fontid);undo=copy.deepcopy(rt);assert undo['m_FontFeatureTable']['m_LigatureSubstitutionRecords'].pop()==record;assert undo==oldtmp
assert rt['m_FontFeatureTable']['m_LigatureSubstitutionRecords'][:9]==records
assert bytes(rf['m_FontData'])==newbytes;undo=copy.deepcopy(rf);undo['m_FontData']=oldfonttree['m_FontData'];assert undo==oldfonttree
loc_after=texts(UnityPy.load(str(OUT/locname)));assert loc_after.keys()==loc_before.keys();changes=[]
for name in loc_before:
    a,b=loc_before[name].split('[i2t]'),loc_after[name].split('[i2t]');assert len(a)==len(b);changes.extend([name,i] for i,(x,y) in enumerate(zip(a,b)) if x!=y)
assert changes==[['I2LS_Levels',533]] and loc_after['I2LS_Levels'].split('[i2t]')[533].split('=',1)[1]==diag
# SVG faithfully decomposes the actual appended glyph for browser inspection;
# it does not make a cmap/GSUB alias. Browser text samples use unchanged old cmap.
pen=SVGPathPen(checked.getGlyphSet());checked.getGlyphSet()[newname].draw(pen);svgpath=pen.getCommands()
svg=f'<svg width="74" height="110" viewBox="0 0 74 110" role="img" aria-label="actual appended glyph459 outline at64px"><g transform="translate(0,90) scale(.064,-.064)"><path d="{svgpath}"/></g></svg>'
enc=lambda b:base64.b64encode(b).decode('ascii')
accepted=R/'local/qa/WO-SARA-AM-001-REFERENCE/01-reference-page.png';assert accepted.exists()
html=f'''<!doctype html><meta charset="utf-8"><title>WO006 glyph459 offline font reference</title>
<style>@font-face{{font-family:Base;src:url(data:font/ttf;base64,{enc(rawfont)})}}@font-face{{font-family:Probe;src:url(data:font/ttf;base64,{enc(newbytes)})}}body{{font:16px Arial;margin:28px;color:#111;background:white}}.sample{{font-family:Base;font-size:64px;line-height:110px}}.probe{{font-family:Probe}}.row{{display:flex;align-items:center;gap:28px;border-top:1px solid #aaa;height:144px}}label{{width:380px;line-height:1.4}}code{{font-size:12px}}svg{{vertical-align:baseline}}.old{{height:210px;overflow:hidden}}.old img{{width:1400px;max-width:none;margin-top:-155px}}</style>
<h1>WO006 — new composite glyph459, offline only</h1><p>Chrome155 / CSS64px / 1x. Browser font evidence, never game TMP evidence. No cmap/GSUB alias was added.</p><p id="ready">Font loading...</p>
<div class="row"><label>Appended glyph459<br>Actual candidate outline via SVG, scale64/1000<br>Direct glyph drawing, NOT browser GSUB selection</label>{svg}<code>base118@(0,0), am82@(641,0), tone42@(612,236)<br>gap74 units =4.736 CSSpx; advance1056 =67.584px</code></div>
<div class="row"><label>Surrounding original text — baseline font<br>Browser shaping at64px</label><span class="sample">ถี่ ต่ำ ทำ</span></div>
<div class="row"><label>Surrounding original text — candidate font<br>Existing cmap/GSUB unchanged; browser does not read TMP ligatures</label><span class="sample probe">ถี่ ต่ำ ทำ</span></div>
<div class="row"><label>Mixed reference context<br>Baseline shaped ถี่ / direct appended glyph / baseline shaped ทำ</label><span class="sample">ถี่</span>{svg}<span class="sample">ทำ</span></div>
<h2>Accepted Chrome155 /64px atomic reference (original PNG, native1x CSS crop)</h2><div class="old"><img src="data:image/png;base64,{enc(accepted.read_bytes())}"></div><p>Qualitative stack order/separation only; no pixel identity claim.</p>
<script>Promise.all([document.fonts.load('64px Base','ถี่ ต่ำ ทำ'),document.fonts.load('64px Probe','ถี่ ต่ำ ทำ')]).then(()=>{{document.getElementById('ready').textContent='Font loaded: baseline='+document.fonts.check('64px Base','ต่ำ')+', probe='+document.fonts.check('64px Probe','ต่ำ')+'; CSS64px; baseline SHA256 {digest(rawfont)}; new font {digest(newbytes)}';document.title='WO006_REFERENCE_READY';}})</script>'''
(REF/'reference.html').open('x',encoding='utf-8').write(html)
files=[{'name':f['name'],'original_sha256':f['original_sha256'],'parent_sha256':sha(BASE/f['name']),'probe_sha256':sha(OUT/f['name']),'parent_bytes':(BASE/f['name']).stat().st_size,'probe_bytes':(OUT/f['name']).stat().st_size} for f in manifest['files']]
geometry={'units_per_em':1000,'base_advance':641,'am_advance':415,'new_advance':1056,'component_glyph_ids':[118,82,42],'component_translations':[[0,0],[641,0],[612,236]],'source_anchor':anchor,'ring_bbox_translated':ringbox,'tone_bbox_translated':tonebox,'vertical_gap_units':gap,'vertical_gap_at_64px':gap*.064,'ring_center_x':(ringbox[0]+ringbox[2])/2,'tone_center_x':(tonebox[0]+tonebox[2])/2,'new_bbox':[g.xMin,g.yMin,g.xMax,g.yMax],'new_lsb':60,'flattened_points':len(coordinates),'flattened_contours':len(contours),'composite_depth':2}
report={'wo':'WO-SARA-AM-006','probe':OUT.name,'status':'STRUCTURAL_READY_PENDING_REFERENCE','label':'VERIFIED','parent':BASE.name,'installed':False,'runtime_status':'NOT_RUN','files':files,'added_record':record,'new_glyph':{'id':N,'name':newname,'glyph_count_before':N,'glyph_count_after':N+1},'font_before_sha256':digest(rawfont),'font_after_sha256':digest(newbytes),'font_bytes_before':len(rawfont),'font_bytes_after':len(newbytes),'geometry':geometry,'diagnostic_text':diag,'diagnostic_codepoints':[[f'U+{ord(c):04X}' for c in line] for line in diag.splitlines()],'control_choice':{'text':'ทำ','reason':'Unmarked sara-am control isolates baseline ring/base/aa behavior; L2 and L3 already cover marked sara-am. No sentinel/L6.'},'checks':{'font_reopen':True,'whole_sfnt_checksum':hex(calcChecksum(newbytes)),'every_table_checksum':True,'all_459_old_raw_glyph_slices_identical':True,'old_loca_prefix_identical':True,'old_metric_records_byte_identical':True,'old_metric_values_identical':True,'cmap_table_byte_identical':True,'new_glyph_absent_from_all_cmaps':True,'old_glyph_order_preserved':True,'changed_font_tables':changed_tables,'unchanged_font_tables':[t for t in font.reader.keys() if t not in changed_tables],'raw_object_diffs':diffs,'tmp_only_one_added_ligature':True,'previous_nine_records_unchanged':True,'font_object_only_embedded_bytes_changed':True,'changed_localization':changes,'ui_bundle_identical':True,'all_bundles_reloaded':True,'serialized_glyph_and_character_tables_unchanged_empty':True,'atlas_readable':True},'dynamic_glyph_gate':{'VERIFIED':'Source TryAddGlyphInternal receives glyph ID, loads font, tries packing glyph ID into readable atlas, populates runtime glyph table; no required cmap or serialized character entry. Target serialized mode1/empty tables/readable atlas confirmed.','INFERRED':'No extra serialized entry/hint is required by inspected source; hence no such field is added and no STOP condition demonstrated.','UNKNOWN':'Exact game fork new-glyph import/loading, atlas capacity, font cache and final raster/clipping. WO-LIG-001 verifies existing glyph only.'},'reference':{'html':str((REF/'reference.html').relative_to(R)),'html_sha256':sha(REF/'reference.html'),'new_glyph_render_mode':'Actual candidate glyf outline decomposed via fontTools SVGPathPen; Chrome SVG at64/1000 scale; not browser GSUB selection','text_render_mode':'Browser shapes original Unicode using baseline and candidate fonts atCSS64px; cannot consume TMP ligature record','accepted_png':str(accepted.relative_to(R)),'accepted_png_sha256':sha(accepted),'status':'PENDING_BROWSER_RENDER'},'protected_before':before,'limitations':'Diagnostic one cluster only; no production fix/runtime claim. No cmap/GSUB entry added; all existing glyphs/metrics preserved byte-for-byte.'}
preserve();(REF/'structural-build.json').open('x',encoding='utf-8').write(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({'probe':OUT.name,'new_glyph_id':N,'font_bytes_delta':len(newbytes)-len(rawfont),'new_bbox':geometry['new_bbox'],'gap_at64px':geometry['vertical_gap_at_64px'],'changed_tables':changed_tables,'next':'Render reference then finalize report/manifest; no install.'}))
