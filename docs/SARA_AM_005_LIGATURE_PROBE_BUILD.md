# WO-SARA-AM-005 — Ligature executor probe build

2026-10-26 (Asia/Bangkok). **BUILD_READY — ready for PM acceptance only.**

**VERIFIED:** built `local/prototype/probe-sara-am-lig-001` from frozen `fresh-translation-005` using exclusive creation. No install, game launch, screen operation, runtime WO, dispatch, commit or push. BUG-THAI-003 remains OPEN; this is a deliberately wrong sentinel substitution, not a fix.

## Specification and checks

**VERIFIED:** only `I2LS_Levels` segment533 (`Levels/Freshleigh/Level_Intro_Text`) changes in localisation, reusing the accepted001a diagnostic binding. Exact labelled specimen text and Unicode values are in the manifest/report. Five lines:

```text
L1: ต่ำ
L2: ต้ำ
L3: ค่ำ
L4: ตา ถี่
L5: ก
```

**VERIFIED:** target TMP−1239755799206566947 gains exactly one `m_LigatureSubstitutionRecords` entry, `m_ComponentGlyphIDs=[118,42,82]`, `m_LigatureGlyphID=29`. Existing font cmap maps ก/U+0E01 to29, different-tone ต้ำ to[118,47,82], and ค has a different base ID (full mapping recorded by build checks). ก is a distinct existing consonant; no glyph artwork/metrics/cmap/atlas edit. **INFERRED:** L5 makes the same glyph an explicit ordinary-text loading/reference control. **UNKNOWN:** actual atlas population/visibility until runtime; L5 is evidence only if QA sees it.

**VERIFIED — conflicts/order:** all nine original ligatures retained exactly, none starts118; consequently there is no matching first-glyph bucket/prefix that can shadow this new record. Official pre4 source `TMP_FontAsset.cs:InitializeLigatureSubstitutionLookupDictionary` clears/creates a nonserialized dictionary then adds list records to buckets keyed by first component. `TMPro_UGUI_Private.cs:LIGATURES` traverses records in order, first successful match wins; no automatic longest-match sorting. No competing118 record means order is immaterial for this probe. This is verified source behavior, not a verified shipped package identity.

**VERIFIED — lookup storage:** target serialized tree contains no lookup dictionary fields, and feature table stores only five record lists. Existing scalar m_FeatureLookupFlags in pair records are flags, not serialized dictionaries, and remain unchanged. No serialized dictionary entry exists to update. Shipped native initializer calls `InitializeLigatureSubstitutionLookupDictionary` (retained WO004 bounded listing). **INFERRED:** lookup rebuild from list is the intended path. **UNKNOWN:** exact custom initializer internals/live execution; absence of exact unwind bounds was not bypassed with guessed decoding. The unsafe serialized-lookup STOP condition was not encountered. Source/package hashes retained in build JSON; game package version remains UNKNOWN.

**VERIFIED — structural PASS:** reloaded every output bundle; localisation TextAsset names/segment counts identical except533 and exact five-line codepoints; fonts raw object bytes change only target TMP; removing the added record makes its complete type tree equal baseline; count9→10, previous9 unchanged. Embedded font object raw bytes and embedded font SHA256 `f9855a702e9899b9cfa1e8cb7cbf36c2c7bb6fe31ee0cd6860ae61ae012155d0` unchanged. UI/prefab bundle byte-identical. All bundle and changed-object hashes, protected before/after hashes (frozen005,001a/b, three installed bundles, binary and metadata) are in `reports/sara-am-lig-001-build.json` and candidate manifest. Installed files were checked original/original/original by manager check; no install/restore action executed.

## Expected observations — all runtime NOT_RUN

| Row | Ligature executes (INFERRED) | Does not execute (INFERRED) | Failure / uncertainty |
|---|---|---|---|
| L1 | INFERRED: one ก-shaped sentinel replaces ต่ำ; prefix L1 remains. | INFERRED: original atomic ต่ำ remains (crowding may persist). | UNKNOWN: blank/tofu, partial sequence, clipping or crash is an invalid/inconclusive result. |
| L2 | INFERRED: ต้ำ remains unchanged; tone47 cannot match42. | INFERRED: ต้ำ unchanged. | INFERRED: any sentinel/substitution here violates specificity. |
| L3 | INFERRED: ค่ำ unchanged; different base cannot match118. | INFERRED: ค่ำ unchanged. | INFERRED: sentinel here violates specificity. |
| L4 | INFERRED: ตา ถี่ unchanged. | INFERRED: ตา ถี่ unchanged. | INFERRED: missing/changed controls invalidate clean comparison. |
| L5 | INFERRED: ก visible as standalone reference. | INFERRED: ก still visible if loading succeeds. | INFERRED: absent/tofu ก leaves glyph loading unresolved; do not call executor absent. |


## Interpretation and risks

**INFERRED:** positive evidence requires L1 visibly replaced by a single ก-shaped glyph matching L5 while L2–L4 remain intact. This supports the exact target-sequence executor in this modal context only, not correct Thai shaping, all consumers, longest-match behavior or a production fix. Screenshot should preserve labels/negative controls and visible L5. Do not infer execution from bundle readback alone.

**UNKNOWN:** unchanged L1 may reflect liga disabled, different fallback, runtime lookup not initialized/refreshed, record override/import, preprocessing/alternative glyphs or atlas/font loading. Existing kerning flag does not establish liga; this probe intentionally changes no flags. Visible L5 narrows glyph availability but does not prove the ligature executor or target-font identity. A negative result is INCONCLUSIVE about global ligature support unless these gates are resolved. Blank/tofu/partial substitutions, unintended L2–L4 changes or crash are failure modes; screen/runtime behavior was not tested here. Three-component consumption may affect index/line-layout behavior, and the five-line specimen may clip; do not treat an unseen row as a negative test.

**VERIFIED — handoff boundary:** build/offline verification complete. Stop here for PM acceptance. Only PM may issue the later Antigravity runtime WO. Frozen005/001a/b and installed originals unchanged; no production wording/Unicode rewrite. This diagnostic must never ship as a fix. Any later rollback/install lifecycle is outside this WO.
