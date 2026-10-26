# WO-SARA-AM-006 — Census and appended-glyph probe

2026-10-26 (Asia/Bangkok). ChatGPT engineering. **BUILD_READY — for PM acceptance only.** BUG-THAI-003 remains OPEN. Offline build/reference/verification only; no installation, game launch, runtime test/WO, commit or push.

## Q-A: current005 corpus census

**VERIFIED:** scanned actual frozen005 localisation values (not keys/drafts), all25 TextAssets /15,677 records; record ID set equals the extracted15677 inventory. U+0E33 occurs3,763 times in total. Direct `[U+0E01–U+0E2E][U+0E48–U+0E4B]U+0E33` occurs440 times across15 distinct clusters. Other directly mark-preceded atomic sara-am runs: **0**. Remaining3,323 occurrences are not immediately preceded by a combining mark. ต่ำ occurs51 times in50 records.

| Cluster | Codepoints | Occurrences | Distinct records | Example asset/segment |
|---|---|---:|---:|---|
| น้ำ | U+0E19 U+0E49 U+0E33 | 250 | 239 | I2LS_UI:26 |
| ซ้ำ | U+0E0B U+0E49 U+0E33 | 55 | 48 | I2LS_UI:245 |
| ต่ำ | U+0E15 U+0E48 U+0E33 | 51 | 50 | I2LS_UI:67 |
| ล้ำ | U+0E25 U+0E49 U+0E33 | 36 | 36 | I2LS_Items:224 |
| ร่ำ | U+0E23 U+0E48 U+0E33 | 13 | 13 | I2LS_Items:819 |
| ค่ำ | U+0E04 U+0E48 U+0E33 | 10 | 10 | I2LS_Items:244 |
| ถ้ำ | U+0E16 U+0E49 U+0E33 | 6 | 6 | I2LS_Items:762 |
| ด่ำ | U+0E14 U+0E48 U+0E33 | 5 | 5 | I2LS_Items:1927 |
| ฉ่ำ | U+0E09 U+0E48 U+0E33 | 3 | 3 | I2LS_VO_Radio:175 |
| ล่ำ | U+0E25 U+0E48 U+0E33 | 3 | 3 | I2LS_Characters:907 |
| ค้ำ | U+0E04 U+0E49 U+0E33 | 2 | 2 | I2LS_VO_Radio:188 |
| ย้ำ | U+0E22 U+0E49 U+0E33 | 2 | 2 | I2LS_VO_Radio:159 |
| ว่ำ | U+0E27 U+0E48 U+0E33 | 2 | 2 | I2LS_Items:338 |
| น่ำ | U+0E19 U+0E48 U+0E33 | 1 | 1 | I2LS_Levels:297 |
| ม่ำ | U+0E21 U+0E48 U+0E33 | 1 | 1 | I2LS_VO_Radio:23 |


**VERIFIED:** full segment IDs, offsets, line/column indices, counts and context samples are in `reports/sara-am-006-census.json`. Of440 direct-cluster occurrences,32 are in records containing explicit LF. Census records explicit LF, literal backslash-n, br/nobr tags, ZWSP, word joiner and record lengths. **UNKNOWN:** actual runtime wrapping widths/breaks; markup-separated runs are not treated as contiguous Unicode clusters. **INFERRED:** these15 patterns share structural risk with ต่ำ; the census is not visual proof that every pattern fails. No text was normalized or altered by census.

## Q-B: one appended composite

**VERIFIED:** new exclusive directory `local/prototype/probe-sara-am-glyph-001`, base frozen005. Font object7716434233879021909 gains exactly one glyph, ID459 (`saraAm006_tomaiEkAm`),459→460 glyphs. No cmap alias or GSUB change; reachable by the new TMP ligature only. Existing IDs0–458 stay intact. TMP−1239755799206566947 gains only `[118,42,82] → 459`; previous9 ligatures unchanged, none starts118. No MarkToMark/pair/anchor, flags, glyph-table, character-table or atlas-setting change.

**VERIFIED — geometry from actual font:** ต118 advance641; sara-am82 advance415, components78+59 at their original coordinates. Ring59 translated to x641 has bbox`[362,608,590,794]`. Existing GPOS59→42 anchors are base`(-115,772)`, mark`(-86,536)` from the accepted audit of the same baseline hash. Thus tone offset x=`641−115−(−86)=612`, y=`772−536=236`. Tone42 outline bbox becomes`[421,868,523,1083]`, fully within the ring's x range, centers472 versus476 (4-unit difference). Vertical outline gap=`868−794=74` font units =4.736 CSSpx at64px; no guessed pixel shift. New components:118@(0,0),82@(641,0),42@(612,236). New bbox`[60,−10,978,1083]`, advance`641+415=1056` (67.584px at64px), LSB60. Flattened geometry90 points/5 contours, composite depth2.

**INFERRED:** using the existing pair's anchors plus actual outline clearance is a bounded geometry choice for this one cluster. Those offsets must not be copied globally to other bases/tones. No new anchor record is added; the source anchor numbers define the new composite offsets only.

**VERIFIED — preserved bytes:** fontTools reopened the new font; glyph count+1; old loca offsets/prefix, every old glyph's raw glyf slice, every old metric record/value, old glyph order and entire cmap table byte-identical. All other font tables byte-identical except glyf/loca/hmtx/maxp/hhea/head/post. Post changes only support the appended glyph name/count; existing glyph names remain. Required global bounds/limit/checksum updates do not change old glyph advances or outlines. Whole-font checksum0xB1B0AFBA and every table checksum verified. Automatic bbox recomputation initially re-encoded some old composite flags in memory; that output was never emitted. Final build disables that rewrite, explicitly updates required global limits, and asserts original459 glyph slices byte-equal.

**VERIFIED — font hashes/size:** baseline`f9855a702e9899b9cfa1e8cb7cbf36c2c7bb6fe31ee0cd6860ae61ae012155d0`; new`bcf8e1263daa9cbbf874348f2c5874983352e141a9a484b7ae3b55bdeac06c49`. Font47,544→47,608 bytes (**+64**). Font bundle68,187,625→68,187,705 bytes (**+80**). Full bundle/object hashes and raw object diffs are in `reports/sara-am-glyph-001-build.json` and candidate manifest.

## Dynamic loading / STOP gate

**VERIFIED — inspected source/layout:** retained official pre4 `TMP_FontAsset.cs:TryAddGlyphInternal` takes a glyph index, checks existing lookup, rejects static mode, loads the font face, and calls TryAddGlyphToTexture by glyph index; it then adds the runtime glyph entry without requiring a character/cmap entry. Target serialized mode1 has empty glyph/character tables and a readable atlas,512×512, multiatlas disabled. Source ligature path calls this function for its replacement. No lookup dictionary is serialized in the TMP tree; scalar FeatureLookupFlags are not dictionaries. The previous accepted lig-001 proved a three-component ligature executes here with an existing glyph.

**INFERRED:** inspected source requires no extra serialized TMP glyph/character entry or atlas hint for a dynamic glyph-ID target, so the specified STOP condition has not been demonstrated. None was added. **UNKNOWN:** exact game fork's new-glyph/font-face/cache behavior and atlas capacity. This probe exists to test those gates later; a browser parse/reference cannot close them. Runtime package provenance remains UNKNOWN. No guessed binary patch or additional field was used.

## Specimens and isolated diffs

**VERIFIED:** only `I2LS_Levels533` changes, with exact Latin-labelled five lines:

```text
L1: ต่ำ
L2: ต้ำ
L3: ค่ำ
L4: ตา ถี่
L5: ทำ
```

**INFERRED — L5 choice:** ทำ supplies sara-am without a tone, isolating the unligated base/ring/aa control; L2/L3 already cover marked sara-am. No sentinel or L6. Exact complete line codepoints are in manifest/build JSON. All localisation assets/segments were compared to005; only533 differs. Reloaded every output bundle: font raw object diff is exactly Font7716434233879021909 + TMP−1239755799206566947; Font tree differs only embedded bytes and TMP tree only the appended ligature. UI bundle byte-identical. Removing the new record restores the complete TMP tree; previous9 preserved.

## Browser reference at64px

**VERIFIED:** `local/review/sara-am-006/reference.png` rendered in isolated headless **Chrome155.0.8059.86**, CSS64px, device scale1,1400×1250. SHA256`8465a42d5d3dc57e00bd27aa76014f09649f79d07e8c3fce05b14beff9e9248d`. DOM confirms baseline/probe fonts loaded=true; metadata/command in `browser-reference.json`, DOM and stderr retained. Original accepted Chrome155/CSS64px screenshot is embedded at native1× CSS scale for comparison, unchanged.

**VERIFIED — method/visual result:** actual new glyph459 outline is decomposed from the candidate glyf using SVGPathPen and drawn by Chrome SVG at64/1000 scale; it has separate base/ring/tone layers and visible gap, matching the accepted atomic reference qualitatively. Surrounding `ถี่ ต่ำ ทำ` is browser-shaped twice using baseline and candidate fonts; both remain clean. Direct glyph drawing avoids adding a forbidden cmap/browser-GSUB alias. Browser original-text shaping does **not** consume TMP ligature records, so these text samples do not select459. The mixed row is a visual context, not a baseline-alignment acceptance test. **UNKNOWN:** actual game glyph459 loading/raster/clipping. No pixel equivalence or runtime fix claim.

## Proposed outcome interpretation — no runtime executed

| Observable outcome | Interpretation (runtime NOT_RUN) |
|---|---|
| Correctly stacked new glyph | INFERRED: L1 ต่ำ with ring below tone and clear gap; base/aa normal baseline. L2/L3 retain old crowded forms, L4/L5 unchanged. Supports this one appended glyph in this context only. |
| Glyph renders, mis-stacked/clipped/width wrong | INFERRED: New target loading may work, but geometry/metrics/raster/layout fails; no fix acceptance. |
| Blank/tofu/partial glyph/crash | UNKNOWN: Failure path unresolved (font import/cache/atlas/new glyph); no global conclusion. Runtime tester must close/restore per a later PM WO. |
| Unchanged crowded atomic ต่ำ | UNKNOWN: Ligature not visibly applied, compatible with unavailable new glyph or flags/fallback/lookup/cache changes. Do not uniquely diagnose availability from unchanged text. |
| Controls changed, rows absent or other outcome | UNKNOWN: Specificity/binding/layout/setup inconclusive; record actual screen, do not advance or silently rebuild. |


**UNKNOWN — negative-result causes:** unchanged/crowded L1 can mean new glyph unavailable, cached old font, failed atlas packing, flag/fallback/lookup/override/binding differences. Blank/tofu/crash also needs direct observation; do not diagnose a unique mechanism from one symptom. L2/L3 are expected to retain their previous crowded form because only ต่ำ is targeted. L4/L5 should retain normal baselines/spacing. Future QA must inspect glyph height, aa/base baseline, width, wrapping, clipping and controls in the actual modal.

**VERIFIED — ascent risk:** unchanged font hhea ascent, OS/2 typo ascender and WinAscent are1061 units; new top1083 exceeds them by22 units (1.408px at64px). Existing TMP FaceInfo ascent41.22 at point30 is greater than the new outline top32.49 at point30. **UNKNOWN:** which bounds the game's glyph import/layout/clipping use. SVG outline drawing deliberately does not test font-engine clipping against ascent. No ascent/OS/2/TMP metric was raised to hide this risk. PM must consider it before runtime acceptance. Exact measurements are retained in `reports/sara-am-006-verification.json`.

## Scaling estimate

**INFERRED:** covering this corpus's15 direct clusters would require15 appended composites +15 exact ligatures (14 more beyond this probe), bringing459→474 glyphs. Each cluster must derive its own base/tone IDs, component transforms, bounds and advances from outlines/anchors, with special narrow/small/tall-base considerations and individual readback/regression. The measured one-cluster font growth is64 bytes; a rough similarly named/composed15-cluster font increase is~960 bytes plus~300 bytes of serialized ligature payload (20 bytes per three-component entry), with alignment/compression giving roughly1–2KiB bundle growth, **not measured** for the full set. The more material UNKNOWN is dynamic512×512 single-atlas packing/cache and layout across consumers; corpus counts alone cannot approve scaling.

## Preservation, manager and status

**VERIFIED:** hashes before/after match for all21 protected files: the required original17 plus lig-001's3 bundles/manifest. Frozen005,001a/b,lig-001 and installed originals unchanged. Full records: `reports/sara-am-006-preservation-{before,after}.json`. Added manager choice `probe-sara-am-glyph-001`; read-only manager check passes **original/original/original**. No install/restore action was issued. Candidate/artifact outputs use exclusive-create. Census output succeeded on first run; only its terminal summary hit a console encoding error, so completed census was read/validated instead of regenerated.

**BUILD_READY:** build, font/browser reference and offline checks complete for PM acceptance. Runtime remains NOT_RUN; BUG-THAI-003 remains OPEN. Stop here. PM issues any runtime WO. No production corpus rewrite, global shift, automation, commit or push.
