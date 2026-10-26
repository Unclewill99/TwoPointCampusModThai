"""WO007 final offline collation: new manifest/build report/preservation-after
and analysis Markdown, all exclusive create. Reads completed build/reference;
manager check only. No install/game/runtime WO/commit/push or protected edits.
"""
from pathlib import Path
import json,hashlib,subprocess,sys
R=Path(__file__).resolve().parents[1];D=R/'local/review/sara-am-007';OUT=R/'local/prototype/probe-sara-am-glyph-002'
targets=[OUT/'manifest.json',R/'reports/sara-am-glyph-002-build.json',R/'reports/sara-am-007-preservation-after.json',R/'docs/SARA_AM_007_CLUSTER_SET_PROBE.md'];assert not any(p.exists() for p in targets)
read=lambda p:json.loads(p.read_bytes());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
d=read(D/'structural-build.json');browser=read(D/'browser-reference.json');audit=read(R/'reports/sara-am-007-base-audit.json')
assert browser['new_glyph_svg_count']==15 and browser['baseline_loaded'] and browser['probe_loaded'] and sha(D/'reference.png')==browser['png_sha256']
before=d['protected_before'];after={p:{'size':(R.parent/p).stat().st_size,'sha256':sha(R.parent/p)} for p in before};assert after==before
assert all(sha(OUT/f['name'])==f['probe_sha256'] for f in d['files']);d['status']='BUILD_READY';d['protected_after']=after;d['protected_unchanged']=True;d['protected_files_count']=25
d['reference'].update({'status':'VERIFIED_BROWSER_RENDER_AND_VISUAL_REVIEW','browser':browser,'visual_review':{'label':'VERIFIED_VISUAL','result':'All15 appended outlines show base/ring/tone in separated order at64px. Each compared qualitatively with baseline browser atomic text, plus accepted Chrome155/64px atomic reference.','limits':'SVG direct drawing is not browser GSUB selection, FontEngine loading or game evidence. Card baselines are flex-layout displays; no pixel-identical/baseline equivalence claim.'}})
expected=[]
for i,line in enumerate(d['diagnostic_text'].splitlines(),1):
    words=line.split(': ',1)[1].split();targets_in=[x for x in words if x in {e['text'] for e in d['clusters']}]
    expected.append({'row':f'L{i}','text':line,'targets':targets_in,'label':'INFERRED_EXPECTATION','stacked':('All '+', '.join(targets_in)+' show tone above ring, normal baseline/spacing; ' if targets_in else '')+('ท่ำ remains old crowded negative.' if i==4 else 'ordinary controls remain unchanged.' if i==5 else 'no missing/clipped/wrapped item.'),'flawed':'Any target/control misstacked, shifted, wrong width/line height, clipped top or specificity change is a finding; do not edit/rebuild during QA.','unchanged_crowded':'Any listed target remains crowded: application/loading/lookup/cache unresolved; no unique cause inferred.' if targets_in else 'Not an intended outcome for ordinary controls.','blank_tofu':'Missing/blank/tofu/partial item or absent row is failed/inconclusive; assess each item, not readable body alone.'})
d['expected_outcomes_per_row']=expected;d['base_audit_summary']={'label':'VERIFIED_STATIC','base_count':12,'direct_base_GSUB_substitutions':0,'context_coverage_or_class_mentions':0,'minimum_base_to_ring_vertical_clearance':49,'maximum_base_to_ring_vertical_clearance':60,'existing_mark_to_base_anchors':'Recorded per base in base-audit JSON; preserved, not imported or used as intra-composite attachment.','runtime_alternate_selection':'UNKNOWN outside inspected font/source path; static audit gives no base-specific blocking variant.'}
d['geometry_explanation']={'label':'VERIFIED_DERIVATION','x':'round_half_up(advance(base)+(ring.xMin+ring.xMax-tone.xMin-tone.xMax)/2), independently using each tone outline.','y':'ring.yMax+74-tone.yMin','tone42_bbox':[-191,632,-89,847],'tone47_bbox':[-374,631,-57,843],'ring59_bbox':[-279,608,-51,794],'rounding':'MaiEk exact centering; MaiTho has+0.5unit residual after integer translation (0.032px at64px).','delta_from_glyph001':'ต่ำ nowID464 has tone x616 instead of612, because WO007 explicitly centres outline; y236 and gap74 unchanged. Old glyph001 unchanged.'}
d['source_scripts']=[{'path':'tools/'+n,'sha256':sha(R/'tools'/n)} for n in ['audit_sara_am_007.py','build_sara_am_glyph_002.py','render_sara_am_007_reference.py','finalize_sara_am_007.py']]
targets[0].open('x',encoding='utf-8').write(json.dumps(d,ensure_ascii=False,indent=2))
p=subprocess.run([sys.executable,str(R/'tools/manage_probe.py'),'check','--probe',OUT.name],cwd=R,capture_output=True,text=True,check=True);check=json.loads(p.stdout);assert len(check['files'])==3 and all(x['state']=='original' for x in check['files']) and check['action']=='check';d['manager_check']={'label':'VERIFIED','result':check}
targets[1].open('x',encoding='utf-8').write(json.dumps(d,ensure_ascii=False,indent=2));targets[2].open('x').write(json.dumps(after,indent=2))
geometry='| ID | Cluster | Components (base,am,tone) | am x / tone(x,y) | Bbox | Advance | Gap / top |\n|---:|---|---|---|---|---:|---|\n'
for x in d['clusters']:geometry+=f"| {x['gid']} | {x['text']} | {x['component_ids']} | {x['offsets'][1][0]} / {x['offsets'][2]} | {x['bbox']} | {x['advance']} | {x['gap_units']} / {x['top']} |\n"
rows='| Row | Exact specimen | Expected (INFERRED, runtime NOT_RUN) |\n|---|---|---|\n'
for x in expected:rows+=f"| {x['row']} | {x['text']} | {x['stacked']} |\n"
widths='| Row | Nominal native width incl.80px label budget | +50% uncertainty margin |\n|---|---:|---:|\n'
for i,x in enumerate(d['width_estimates'],1):widths+=f"| L{i} | {x['nominal_native_width_including_80px_label']:.2f}px | {x['with50percent_margin']:.2f}px |\n"
fontdelta=d['font_bytes_after']-d['font_bytes_before'];fb=next(x for x in d['files'] if x['name']=='fonts_assets_all.bundle');bundle_delta=fb['probe_bytes']-fb['parent_bytes']
doc=f'''# WO-SARA-AM-007 —15-cluster diagnostic probe

2026-10-26 (Asia/Bangkok). ChatGPT engineering. **BUILD_READY — for PM acceptance only.** No blocked clusters. Probe `local/prototype/probe-sara-am-glyph-002`. BUG-THAI-003 remains OPEN; no production fix claim.

## Scope and source set

**VERIFIED:** read PM's GLYPH-001 acceptance and WO006 geometry/preservation evidence. Took frozen005 read-only as parent. Census JSON and WO list agree on15 clusters; no extra/generic clusters generated. Appended IDs459–473 deterministically in ascending atomic-codepoint order, giving459→474 glyphs. Added15 exact3-component ligatures,9→24 records. No game launch, install, runtime test/WO, commit or push.

## Base and conflict audit

**VERIFIED — static font data:** all12 selected bases have outline tops548–559, below the ring bottom608 by49–60units. No tall ascender intersects the stack's vertical band. Audit of GSUB direct substitution inputs and contextual coverage/classes found no selected base substitution/alternate or contextual mention. No original ligature starts with any selected base ID. New rules with shared bases differ at their second (tone) component; all are length3 and no component-prefix pair shadows another. Originals were not reordered.

**VERIFIED:** existing MarkToBase anchors for selected bases/tones/ring are recorded in `reports/sara-am-007-base-audit.json`, unchanged. They do not position the embedded outlines inside a full-cluster glyph. Source font mark substitutions/variants remain unchanged. **UNKNOWN:** variant selection in other shaping contexts/engines; no inference of complete shaping equivalence. No base-specific block was demonstrated. Full GSUB audit retained locally as `local/review/sara-am-007/gsub-audit.ttx`.

## Per-cluster geometry

**VERIFIED — derivation:** each composite uses its own base at(0,0), glyph82 at x=advance(base), and its own tone's outline-centred x. Ring59 bbox`[-279,608,-51,794]`; tone42 bbox`[-191,632,-89,847]`; tone47 bbox`[-374,631,-57,843]`. Set tone x to nearest integer (positive half ties up) of `A+(ring.xMin+ring.xMax-tone.xMin-tone.xMax)/2`, where A=base advance; y=`794+74-tone.yMin`. Thus42 uses y236 and47 uses237. This derives every x from the actual base advance/tone bbox, not copied ต่ำ offsets. Ring/tone clearance74units =4.736px at64px for all15. MaiEk centering is exact; MaiTho residual is+0.5unit (0.032px at64px) due integer component translation. Tone47 is wider than the ring, which is expected; centering is not a containment requirement.

{geometry}

**VERIFIED:** all advances=advance(base)+415; LSB and bbox derive from full actual composite. Every component/offset/bbox/advance checked after fontTools reopen. Maximum top1083 for mai-ek clusters,1080 for mai-tho. hhea/typo/win ascent remain1061: known excess22 or19units respectively. OS/2 bytes unchanged; no ascent/FaceInfo/atlas hint raised. **UNKNOWN:** clipping at runtime across15 items. Prior one-cluster result does not approve the set.

**VERIFIED — difference from previous probe:** ต่ำ is nowID464, tone offset(616,236), rather than glyph001's ID459/(612,236). WO007 explicitly asks outline centering; this accounts for the4-unit x difference. Glyph001 itself was not touched. Vertical geometry/gap for ต่ำ stays as accepted.

## Structural verification

**VERIFIED PASS:** fontTools reopen,474 glyphs; all459 old glyph raw slices, old loca prefix, hmtx records/values, glyph IDs/order and entire cmap byte-identical. No new cmap entry or GSUB change. Only glyf/loca/hmtx/maxp/hhea/head/post tables differ as required for appended glyphs/names and global bounds/limits/checksums; whole-font checksum0xB1B0AFBA and every table checksum pass. Existing glyphs/metrics unchanged, hhea ascent and all OS/2 values preserved.

**VERIFIED:** reloaded all3 output bundles. Fonts raw objects differ only at Font7716434233879021909 (embedded font bytes only) and TMP−1239755799206566947 (15 added ligatures only). TMP readback24 records; first9 equal originals, appended15 exact; removing them restores the full baseline TMP tree. No pair/anchor/MarkToMark/flags/atlas/glyph/character-table changes. Only I2LS_Levels533 differs in localisation, exact codepoints recorded; UI bundle byte-identical. No production text rewrite.

**VERIFIED size/hash:** embedded font increases{fontdelta}bytes, fonts bundle increases{bundle_delta}bytes. Baseline font SHA256`{d['font_before_sha256']}`; new`{d['font_after_sha256']}`. Every bundle/object/font hash, raw object byte size/diff and source script hash is retained in `reports/sara-am-glyph-002-build.json` and candidate manifest.

## Diagnostic specimen and fit estimate

**VERIFIED:**5 Latin-labelled lines, all15 targets exactly once, plus one out-of-set negative and ordinary controls. Full line codepoints are in manifest/report.

```text
{d['diagnostic_text']}
```

**VERIFIED:** ท่ำ=`U+0E17 U+0E48 U+0E33` is not in census set and has no new ligature. **INFERRED:** it should stay crowded; ตา/ถี่/ทำ/นำ should stay ordinary. Using4 items per line keeps5 lines as in the accepted modal, rather than adding potentially clipped rows.

**INFERRED — width estimate:** sum actual composite/old-character advances at nominal36px, spaces and an80native-pixel conservative Latin-label allowance; then add50% uncertainty. Observed blue panel in previous native modal is1050px wide, not a freshly verified TMP inner-container width.

{widths}

**INFERRED:** largest margin width396.16px is well below the1050px blue panel. Height design keeps5 lines and no larger glyph top than the accepted glyph001; existing FaceInfo ascent exceeds these outlines. **UNKNOWN:** actual TMP inner bounds, kerning, fallback label metrics, per-line layout/wrapping/fit and atlas behavior. This is an offline budget, not a runtime fit PASS. No layout/Settings/prefab changes were made to force fit.

## 64px font-evidence sheet

**VERIFIED:** `local/review/sara-am-007/reference.png`,1400×1700, Chrome155.0.8059.86, CSS64px/device scale1; SHA256`{browser['png_sha256']}`. Baseline/probe font-ready checks true in retained DOM. All15 actual candidate outlines are drawn using SVGPathPen at64/1000 scale; adjacent original atomic words use baseline browser shaping. Original accepted Chrome155/64px atomic reference is embedded unchanged at1×CSS scale.

**VERIFIED — visual review:** each new glyph shows its base, ring then tone with clear separation, qualitatively consistent with the browser atomic samples/accepted reference. **UNKNOWN:** game raster/spacing/clipping. These are direct outline drawings; browser original text does not read TMP ligatures or select the new glyphs. Flex card baseline differences and shape variants are not a pixel-equivalence test. No cmap/browser-GSUB alias was introduced.

## Atlas estimate (not a packing guarantee)

**INFERRED:** at point30, each outline raster is estimated by ceil(extent×30/1000); add3px padding on all sides. Sum for15 new glyphs **19,110 pixels =7.290%** of512×512; allowing one additional pixel per allocation dimension gives **20,200 =7.706%**. Per-glyph raster/allocated dimensions and areas are in JSON. This estimates new glyphs only. **UNKNOWN:** existing allocations/free space, SDF/hinting, packing alignment/fragmentation, cache lifetime and actual texture occupancy. Multiatlas remains disabled; area ratio alone cannot establish successful packing.

## Expected observation matrix — runtime NOT_RUN

{rows}

**INFERRED — per-row classifications:** every target on L1–L4 must be inspected individually. Stacked: raised tone/gap with normal base/aa baseline. Flawed: any misstack, incorrect width, clipping or shifted line/control. Unchanged-crowded: new path not visibly applied, cause UNKNOWN (glyph loading/flags/fallback/lookup/cache). Blank/tofu/partial/missing row: failed/inconclusive; do not infer success from a readable body. L4's ท่ำ is intentionally *not* expected to improve. L5 has no target and must remain ordinary. The machine report supplies stacked/flawed/unchanged-crowded/blank-tofu expectations for each row.

## Preservation and stop boundary

**VERIFIED:** all25 protected hashes match before/after: required17 plus lig-001's4 files plus glyph-001's4 files. Frozen005,001a/b,lig-001,glyph-001, originals/binary/metadata unchanged. `reports/sara-am-007-preservation-{{before,after}}.json` records complete hashes. Added manager support only for new probe name; read-only check **original/original/original** passed. No install/restore operation executed.

**BUILD_READY:** all15 built, no blocked cluster. Stop for PM acceptance and its separate runtime WO. No release/global fix, automation, commit or push.
'''
targets[3].open('x',encoding='utf-8').write(doc)
assert all(sha(R.parent/p)==v['sha256'] for p,v in before.items())
print(json.dumps({'status':d['status'],'glyphs':474,'ligatures':24,'protected_unchanged':25,'manager':check,'font_growth':fontdelta,'font_bundle_growth':bundle_delta}))
