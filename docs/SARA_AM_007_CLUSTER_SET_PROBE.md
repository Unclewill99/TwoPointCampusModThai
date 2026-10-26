# WO-SARA-AM-007 —15-cluster diagnostic probe

2026-10-26 (Asia/Bangkok). ChatGPT engineering. **BUILD_READY — for PM acceptance only.** No blocked clusters. Probe `local/prototype/probe-sara-am-glyph-002`. BUG-THAI-003 remains OPEN; no production fix claim.

## Scope and source set

**VERIFIED:** read PM's GLYPH-001 acceptance and WO006 geometry/preservation evidence. Took frozen005 read-only as parent. Census JSON and WO list agree on15 clusters; no extra/generic clusters generated. Appended IDs459–473 deterministically in ascending atomic-codepoint order, giving459→474 glyphs. Added15 exact3-component ligatures,9→24 records. No game launch, install, runtime test/WO, commit or push.

## Base and conflict audit

**VERIFIED — static font data:** all12 selected bases have outline tops548–559, below the ring bottom608 by49–60units. No tall ascender intersects the stack's vertical band. Audit of GSUB direct substitution inputs and contextual coverage/classes found no selected base substitution/alternate or contextual mention. No original ligature starts with any selected base ID. New rules with shared bases differ at their second (tone) component; all are length3 and no component-prefix pair shadows another. Originals were not reordered.

**VERIFIED:** existing MarkToBase anchors for selected bases/tones/ring are recorded in `reports/sara-am-007-base-audit.json`, unchanged. They do not position the embedded outlines inside a full-cluster glyph. Source font mark substitutions/variants remain unchanged. **UNKNOWN:** variant selection in other shaping contexts/engines; no inference of complete shaping equivalence. No base-specific block was demonstrated. Full GSUB audit retained locally as `local/review/sara-am-007/gsub-audit.ttx`.

## Per-cluster geometry

**VERIFIED — derivation:** each composite uses its own base at(0,0), glyph82 at x=advance(base), and its own tone's outline-centred x. Ring59 bbox`[-279,608,-51,794]`; tone42 bbox`[-191,632,-89,847]`; tone47 bbox`[-374,631,-57,843]`. Set tone x to nearest integer (positive half ties up) of `A+(ring.xMin+ring.xMax-tone.xMin-tone.xMax)/2`, where A=base advance; y=`794+74-tone.yMin`. Thus42 uses y236 and47 uses237. This derives every x from the actual base advance/tone bbox, not copied ต่ำ offsets. Ring/tone clearance74units =4.736px at64px for all15. MaiEk centering is exact; MaiTho residual is+0.5unit (0.032px at64px) due integer component translation. Tone47 is wider than the ring, which is expected; centering is not a containment requirement.

| ID | Cluster | Components (base,am,tone) | am x / tone(x,y) | Bbox | Advance | Gap / top |
|---:|---|---|---|---|---:|---|
| 459 | ค่ำ | [26, 82, 42] | 623 / [598, 236] | [78, 0, 960, 1083] | 1038 | 74 / 1083 |
| 460 | ค้ำ | [26, 82, 47] | 623 / [674, 237] | [78, 0, 960, 1080] | 1038 | 74 / 1080 |
| 461 | ฉ่ำ | [8, 82, 42] | 610 / [585, 236] | [79, -10, 947, 1083] | 1025 | 74 / 1083 |
| 462 | ซ้ำ | [101, 82, 47] | 570 / [621, 237] | [43, -11, 907, 1080] | 985 | 74 / 1080 |
| 463 | ด่ำ | [12, 82, 42] | 621 / [596, 236] | [56, -10, 958, 1083] | 1036 | 74 / 1083 |
| 464 | ต่ำ | [118, 82, 42] | 641 / [616, 236] | [60, -10, 978, 1083] | 1056 | 74 / 1083 |
| 465 | ถ้ำ | [113, 82, 47] | 609 / [660, 237] | [63, -10, 946, 1080] | 1024 | 74 / 1080 |
| 466 | น่ำ | [63, 82, 42] | 623 / [598, 236] | [78, -10, 960, 1083] | 1038 | 74 / 1083 |
| 467 | น้ำ | [63, 82, 47] | 623 / [674, 237] | [78, -10, 960, 1080] | 1038 | 74 / 1080 |
| 468 | ม่ำ | [56, 82, 42] | 623 / [598, 236] | [86, -10, 960, 1083] | 1038 | 74 / 1083 |
| 469 | ย้ำ | [128, 82, 47] | 602 / [653, 237] | [64, -10, 939, 1080] | 1017 | 74 / 1080 |
| 470 | ร่ำ | [73, 82, 42] | 497 / [472, 236] | [38, -11, 834, 1083] | 912 | 74 / 1083 |
| 471 | ล่ำ | [33, 82, 42] | 579 / [554, 236] | [46, -10, 916, 1083] | 994 | 74 / 1083 |
| 472 | ล้ำ | [33, 82, 47] | 579 / [630, 237] | [46, -10, 916, 1080] | 994 | 74 / 1080 |
| 473 | ว่ำ | [126, 82, 42] | 498 / [473, 236] | [37, -11, 835, 1083] | 913 | 74 / 1083 |


**VERIFIED:** all advances=advance(base)+415; LSB and bbox derive from full actual composite. Every component/offset/bbox/advance checked after fontTools reopen. Maximum top1083 for mai-ek clusters,1080 for mai-tho. hhea/typo/win ascent remain1061: known excess22 or19units respectively. OS/2 bytes unchanged; no ascent/FaceInfo/atlas hint raised. **UNKNOWN:** clipping at runtime across15 items. Prior one-cluster result does not approve the set.

**VERIFIED — difference from previous probe:** ต่ำ is nowID464, tone offset(616,236), rather than glyph001's ID459/(612,236). WO007 explicitly asks outline centering; this accounts for the4-unit x difference. Glyph001 itself was not touched. Vertical geometry/gap for ต่ำ stays as accepted.

## Structural verification

**VERIFIED PASS:** fontTools reopen,474 glyphs; all459 old glyph raw slices, old loca prefix, hmtx records/values, glyph IDs/order and entire cmap byte-identical. No new cmap entry or GSUB change. Only glyf/loca/hmtx/maxp/hhea/head/post tables differ as required for appended glyphs/names and global bounds/limits/checksums; whole-font checksum0xB1B0AFBA and every table checksum pass. Existing glyphs/metrics unchanged, hhea ascent and all OS/2 values preserved.

**VERIFIED:** reloaded all3 output bundles. Fonts raw objects differ only at Font7716434233879021909 (embedded font bytes only) and TMP−1239755799206566947 (15 added ligatures only). TMP readback24 records; first9 equal originals, appended15 exact; removing them restores the full baseline TMP tree. No pair/anchor/MarkToMark/flags/atlas/glyph/character-table changes. Only I2LS_Levels533 differs in localisation, exact codepoints recorded; UI bundle byte-identical. No production text rewrite.

**VERIFIED size/hash:** embedded font increases904bytes, fonts bundle increases1200bytes. Baseline font SHA256`f9855a702e9899b9cfa1e8cb7cbf36c2c7bb6fe31ee0cd6860ae61ae012155d0`; new`49554400797971424cb9057481e2dd55744cec5fa603ee6b21ae24bcff3b2607`. Every bundle/object/font hash, raw object byte size/diff and source script hash is retained in `reports/sara-am-glyph-002-build.json` and candidate manifest.

## Diagnostic specimen and fit estimate

**VERIFIED:**5 Latin-labelled lines, all15 targets exactly once, plus one out-of-set negative and ordinary controls. Full line codepoints are in manifest/report.

```text
L1: น้ำ ซ้ำ ต่ำ ล้ำ
L2: ร่ำ ค่ำ ถ้ำ ด่ำ
L3: ฉ่ำ ล่ำ ค้ำ ย้ำ
L4: ว่ำ น่ำ ม่ำ ท่ำ
L5: ตา ถี่ ทำ นำ
```

**VERIFIED:** ท่ำ=`U+0E17 U+0E48 U+0E33` is not in census set and has no new ligature. **INFERRED:** it should stay crowded; ตา/ถี่/ทำ/นำ should stay ordinary. Using4 items per line keeps5 lines as in the accepted modal, rather than adding potentially clipped rows.

**INFERRED — width estimate:** sum actual composite/old-character advances at nominal36px, spaces and an80native-pixel conservative Latin-label allowance; then add50% uncertainty. Observed blue panel in previous native modal is1050px wide, not a freshly verified TMP inner-container width.

| Row | Nominal native width incl.80px label budget | +50% uncertainty margin |
|---|---:|---:|
| L1 | 264.07px | 396.10px |
| L2 | 261.80px | 392.70px |
| L3 | 264.10px | 396.16px |
| L4 | 262.27px | 393.40px |
| L5 | 251.97px | 377.96px |


**INFERRED:** largest margin width396.16px is well below the1050px blue panel. Height design keeps5 lines and no larger glyph top than the accepted glyph001; existing FaceInfo ascent exceeds these outlines. **UNKNOWN:** actual TMP inner bounds, kerning, fallback label metrics, per-line layout/wrapping/fit and atlas behavior. This is an offline budget, not a runtime fit PASS. No layout/Settings/prefab changes were made to force fit.

## 64px font-evidence sheet

**VERIFIED:** `local/review/sara-am-007/reference.png`,1400×1700, Chrome155.0.8059.86, CSS64px/device scale1; SHA256`64e74c67eabb210f3f81a8270eb7bbc129c22adee19fb8bea69a29b83a125994`. Baseline/probe font-ready checks true in retained DOM. All15 actual candidate outlines are drawn using SVGPathPen at64/1000 scale; adjacent original atomic words use baseline browser shaping. Original accepted Chrome155/64px atomic reference is embedded unchanged at1×CSS scale.

**VERIFIED — visual review:** each new glyph shows its base, ring then tone with clear separation, qualitatively consistent with the browser atomic samples/accepted reference. **UNKNOWN:** game raster/spacing/clipping. These are direct outline drawings; browser original text does not read TMP ligatures or select the new glyphs. Flex card baseline differences and shape variants are not a pixel-equivalence test. No cmap/browser-GSUB alias was introduced.

## Atlas estimate (not a packing guarantee)

**INFERRED:** at point30, each outline raster is estimated by ceil(extent×30/1000); add3px padding on all sides. Sum for15 new glyphs **19,110 pixels =7.290%** of512×512; allowing one additional pixel per allocation dimension gives **20,200 =7.706%**. Per-glyph raster/allocated dimensions and areas are in JSON. This estimates new glyphs only. **UNKNOWN:** existing allocations/free space, SDF/hinting, packing alignment/fragmentation, cache lifetime and actual texture occupancy. Multiatlas remains disabled; area ratio alone cannot establish successful packing.

## Expected observation matrix — runtime NOT_RUN

| Row | Exact specimen | Expected (INFERRED, runtime NOT_RUN) |
|---|---|---|
| L1 | L1: น้ำ ซ้ำ ต่ำ ล้ำ | All น้ำ, ซ้ำ, ต่ำ, ล้ำ show tone above ring, normal baseline/spacing; no missing/clipped/wrapped item. |
| L2 | L2: ร่ำ ค่ำ ถ้ำ ด่ำ | All ร่ำ, ค่ำ, ถ้ำ, ด่ำ show tone above ring, normal baseline/spacing; no missing/clipped/wrapped item. |
| L3 | L3: ฉ่ำ ล่ำ ค้ำ ย้ำ | All ฉ่ำ, ล่ำ, ค้ำ, ย้ำ show tone above ring, normal baseline/spacing; no missing/clipped/wrapped item. |
| L4 | L4: ว่ำ น่ำ ม่ำ ท่ำ | All ว่ำ, น่ำ, ม่ำ show tone above ring, normal baseline/spacing; ท่ำ remains old crowded negative. |
| L5 | L5: ตา ถี่ ทำ นำ | ordinary controls remain unchanged. |


**INFERRED — per-row classifications:** every target on L1–L4 must be inspected individually. Stacked: raised tone/gap with normal base/aa baseline. Flawed: any misstack, incorrect width, clipping or shifted line/control. Unchanged-crowded: new path not visibly applied, cause UNKNOWN (glyph loading/flags/fallback/lookup/cache). Blank/tofu/partial/missing row: failed/inconclusive; do not infer success from a readable body. L4's ท่ำ is intentionally *not* expected to improve. L5 has no target and must remain ordinary. The machine report supplies stacked/flawed/unchanged-crowded/blank-tofu expectations for each row.

## Preservation and stop boundary

**VERIFIED:** all25 protected hashes match before/after: required17 plus lig-001's4 files plus glyph-001's4 files. Frozen005,001a/b,lig-001,glyph-001, originals/binary/metadata unchanged. `reports/sara-am-007-preservation-{before,after}.json` records complete hashes. Added manager support only for new probe name; read-only check **original/original/original** passed. No install/restore operation executed.

**BUILD_READY:** all15 built, no blocked cluster. Stop for PM acceptance and its separate runtime WO. No release/global fix, automation, commit or push.
