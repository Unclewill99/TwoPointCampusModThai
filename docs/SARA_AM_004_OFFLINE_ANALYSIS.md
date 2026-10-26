# WO-SARA-AM-004 — Offline solution analysis

Date: 2026-10-26 (Asia/Bangkok). Analyst: ChatGPT. **INCONCLUSIVE**.

**VERIFIED — delivery boundary.** Analysis only; no candidate, install, game launch, runtime WO, commit or push. Protected-input hashes match for all 17 files captured before analysis. See `reports/sara-am-004-preservation-{before,after}.json`. Existing changes to `docs/PROJECT_STATUS.md` and `docs/AGENT_TASKS.md` predate this analysis and were preserved. This report does not change PM authority or close BUG-THAI-003.

## Evidence and version gate (Q1/Q2)

**VERIFIED — accepted baseline, not repeated.** Use `SARA_AM_001_REFERENCE_ACCEPTANCE.md`, `SARA_AM_003_EXPERIMENT.md`, `SARA_AM_002_AB_R2_ACCEPTANCE.md`, the corresponding QA report, `reports/sara-am-font-audit.json`, `sara-am-gsub-mappings.json`, `sara-am-tutorial-{provider,text,font-chain}.json` and `sara-am-002-ab-r2-image-diff.json`. Accepted reference is Chrome155/CSS64px, embedded font SHA256 `f9855a702e9899b9cfa1e8cb7cbf36c2c7bb6fe31ee0cd6860ae61ae012155d0`. Added59→42 changed 74 pixels in reordered row B; atomic A/original-order C unchanged. Do not interpret browser shaping as game runtime evidence.

**VERIFIED — authoritative source packages.** Unity registry metadata at [packages.unity.com/com.unity.textmeshpro](https://packages.unity.com/com.unity.textmeshpro) identifies downloaded `3.2.0-pre.4` (repository revision `26fadfb632ffe5cb14bab5019ef8097eece1e62a`, tar SHA1 `22accec50ea3c1d608e223c2eff5effdb7269e2b`) and `3.2.0-pre.10` (`8fca90baea965bab48c88326f1d4ca248b64097b`, SHA1 `e75768cd64591d1817bac4c54b9fe98fdf87d280`). Tarballs were checked against registry SHA1 and their package.json identities. Evidence: `reports/sara-am-004-package-evidence.json`; sources retained under `local/review/sara-am-004/official-packages/`. Earlier pre4 mirror text matches official source after BOM/line-ending normalization; analysis below cites official pre4 source, not an assumed shipped version.

**UNKNOWN — exact shipped package.** No binding project `packages-lock.json`/package manifest was found in the inspected game/local trees. Metadata identifies `Unity.TextMeshPro.dll`, assembly version `0.0.0.0`; independently checked codegen table maps get_version to `0x181fc9b20`, whose literal is `1.4.0`. The downloaded source also uses that stale literal. Neither number proves package version. Metadata contains custom loading fields (`DynamicFontLoadingMode`, `OnAsyncLoadRequiredFilesCompleted`, `m_fontFile`) absent from the two inspected standard TMP_FontAsset sources. A custom fork/backport is **INFERRED**, exact provenance **UNKNOWN**. Evidence: `metadata-v3.txt`, `globals.tsv`, `native/TMPro.TMP_Settings.get_version.asm.txt`, official TMP_Settings.cs. It would be incorrect to claim the game uses pre4 or pre10.

## Atomic sara am (Q1)

**VERIFIED — assets.** `reports/sara-am-004-asset-evidence.json` shows glyph82 is a TrueType composite of uni0E32 + uni0E4D. This is one glyph with two outlines, not two text glyphs. TMP object `-1239755799206566947` has empty serialized glyph/character tables, atlas mode1, 512×512, padding3, multiatlas disabled, point size30, reimport flag0. Existing base118/mark42 anchor y values both16.08 give zero vertical adjustment; no42→82 pair exists. Actual tones: `่=42`, `้=47`, `๊=50`, `๋=39` (not assumed43/44/45).

**VERIFIED — source behavior, conditional applicability.** Official pre4 `TMP_TextParsingUtilities.cs:IsBaseGlyph` treats U+0E48 as a mark and U+0E33 as a base. `TMPro_UGUI_Private.cs:2217–2335` applies pair positioning, then current-mark attachment to prior base/marks; it does not look ahead to an embedded component of a future glyph. `:1298–1364` implements fixed ligatures. No multiple-substitution consumer or Thai-specific reorder was found in the inspected TMP_FontAsset/TMP_Text/UGUI/feature-table paths. A type/list existing is not an executor.

**INFERRED — likely atomic path.** If this game follows that inspected path and uses the target fallback, ต่ำ maps `[118,42,82]`; tone42 attaches to ต118 through MarkToBase, while sara-am82 keeps its baked ring. It cannot use MarkToMark(82,42) to place an earlier tone over a later sara-am. This is consistent with accepted A/B, not proof of the actual glyph stream or root cause. **UNKNOWN:** runtime font selection, substitutions, active flags and exact branch. Static text route remains MAIN4694779218175474965 → TMP7894969370473676053 → PalanquinDark external8 → Thai fallback; it does not establish live selection.

## Executing records versus storage (Q2)

Each row separates **VERIFIED inspected-source/static evidence** from applicability to the shipped runtime. Detailed machine table: `reports/sara-am-004-analysis.json:record_support`.

| Record | Source/static result | Shipped-runtime conclusion |
|---|---|---|
| MultipleSubstitution | VERIFIED: record/list only in inspected paths; no lookup; no contextual field | UNKNOWN executor. Do not add82→[59,78] blindly; even substitution alone leaves preceding-tone order unresolved. |
| Ligature, 3 components | VERIFIED: length-driven matching and TryAddGlyphInternal, gated on liga | INFERRED support from native initializer/schema; active liga and exact matcher UNKNOWN. |
| Contextual GSUB/reordering | VERIFIED: no contextual guard in inspected multiple record; fixed ligature is not a general context shaper | UNKNOWN supported game path; no proven table-only contextual decomposition. |
| GlyphPairAdjustment | VERIFIED: pair getter calls before IsBaseGlyph in native GenerateTextMesh; source consumes first/second values under kern | INFERRED consumption; actual flags/inputs UNKNOWN. Mark placement can overwrite source pair x/yPlacement. |
| MarkToBase | VERIFIED: native initializer/getter sites; source uses prior base/current mark | INFERRED atomic branch; exact live branch UNKNOWN. |
| MarkToMark | VERIFIED: accepted59→42 effect for reordered rowB; native initializer/getter sites | VERIFIED only within accepted A/B scope; no atomic fix or universal fallback claim. |

**VERIFIED — native limits.** New bounded initializer listing at `0x182c08770` calls ligature/pair/MarkToBase/MarkToMark initialization, no multiple lookup. Existing GenerateTextMesh listing calls IsBaseGlyph at `0x183508ea9` after pair getter sites and before anchor getter sites. Several leaf initializers/IsBaseGlyph lack exact unwind bounds in the decoder; their internals remain **UNKNOWN**, not guessed. Existing shared-RET GSUB entry does not exclude other shaping paths. Source ImportFontFeatures/UpdateGSUB extraction is compile-flag dependent; serialization and dynamic feature import are separate questions.

## Options, ranking and impact (Q3)

**INFERRED — heuristic rank.** Scores are ordinal 1–3, efficacy × containment × offline verifiability, not measured probabilities. Scope/evidence gates override product. D+B is a possible asset-only branch, not an authorized build or proven fix.

| Rank / score | Option and exact change boundary | Confidence / blast radius | Offline verification / runtime gap / reversibility |
|---|---|---|---|
| 1 / 12 | D+B: new appended full-cluster glyph plus one fixed `[118,42,82]` ligature in target TMP | INFERRED medium efficacy, narrow exact sequence. Layout/index behavior risk; other occurrences of ต่ำ also match | Offline font validity, exact object diff and atlas inputs; UNKNOWN live liga/packing/fallback/layout. Revert future scratch bundle, preserve baseline. |
| 2 / 6 | A: renderer processing hook; requires code plugin/loader beyond data bundles | INFERRED highest conceptual shaping coverage; update/stability/indexing and hook-coverage risks | Offline algorithm checks cannot establish integration. **BLOCKED_NEEDS_DECISION** on scope; no plugin design here. Rollback would require separate plugin removal contract. |
| 3 / 6 | B alone: serialized substitution/positioning records in TMP only | INFERRED low efficacy: missing demonstrated multiple/contextual executor; existing glyphs do not provide a proven full replacement | Structure can pass while rules never execute. UNKNOWN runtime. A ligature without a suitable replacement glyph is incomplete. Revert new TMP-only scratch output. |
| 4 / 2 | C: pair42→82 or base118/mark42 anchors | INFERRED low efficacy or inadequate containment | Source mark assignment overwrites pair yPlacement. Raising base118/mark42 changes ต่า/ตี่ etc; pair has no third-context predicate. UNKNOWN game applicability. Rollback exact record delta; no global shifts. |
| 5 / 2 | D alone: GSUB/GPOS or existing82/cmap replacement | INFERRED low efficacy without consuming/selection path, broader sara-am impact | Font validation is possible, engine application UNKNOWN. Altering82 globally changes จำ/ทำ/ลำ too; source bytes and cached TMP atlas can diverge. New file only, revert scratch bundle. |
| excluded | E: convert stored text to reordered decomposition | VERIFIED rejected by WO; accepted diagnostic only | INFERRED changes codepoint identity, search/copy/index consumers; broader effects UNKNOWN. No corpus conversion performed or recommended. |

**INFERRED — C geometry bound.** Font glyph82 top794 and tone42 bottom632 imply a purely vertical separation would require tone rise greater than162 font units plus desired gap (greater than4.86 at point30), assuming unchanged origins and overlapping x extents. The known59→42 anchors imply236 units /7.08 at point30; that is not a validated atomic offset. Source successful MarkToBase currently assigns y=16.08−16.08=0, overwriting a pair placement. Raising the base anchor to23.16 would change all118/42 attachments; it cannot be confined to following sara-am by this record. Moving glyph82 instead moves sara-aa off baseline as well. These numbers are geometry/source bounds, not screen pixel predictions.

### Conditional bounded candidate specification — NOT READY / NOT BUILT

**INFERRED — D+B branch only after the evidence gate.** Start from frozen005 by read-only copy into a new, exclusive scratch directory. Target font object7716434233879021909 and TMP object−1239755799206566947 only. Append one full ต่ำ glyph (potential ID459 only if the new font still has459 glyphs and preserves all IDs0–458); ligature record fields `m_ComponentGlyphIDs=[118,42,82]`, `m_LigatureGlyphID=459`. No cmap/text change and no alteration of existing outlines/metrics. This selects a full cluster whose first character is a base, avoiding a tone-class replacement that would itself be attached as a mark. **UNKNOWN:** final composite placement/metrics and whether live liga and dynamic glyph loading accept it. No guessed final outlines or offsets are approved.

**INFERRED — expected future diff/checks.** Only embedded font bytes (new glyph plus required glyf/loca/maxp/hmtx/hhea/head/checksum changes as applicable) and one TMP ligature list entry; localization/UI bundles and all unrelated raw objects must compare byte-identical. Keep existing atlas settings, face metrics and all previous glyph IDs/advances. Current dynamic tables are empty; source TryAddGlyphInternal can populate a glyph at runtime, but this is **UNKNOWN** for the game. Do not assume replacing the TTF regenerates cached/static atlases. If static prepacking is needed, stop and respecify glyph records/rects/textures/materials with exact diffs; none are specified or built here.

**INFERRED — future acceptance/rollback contract.** Require fontTools reopen/checksums, preserved cmap and old glyph bounds/advances, parsed ligature uniqueness/no duplicate first-key conflict, exact component IDs, source hash and baseline bundle/object hashes, new font/bundle/object hashes, raw object diff, target TMP readback, unchanged localization hash/codepoints, no output overwrite. Active liga, actual replacement, glyph-cache lifetime, wrapping/index mapping and raster quality need later authorized runtime QA. Reversion is removal of the future scratch artifact / restoration of original installed bundle via the PM-approved lifecycle, never mutation of frozen005. This WO authorizes neither build nor runtime WO.

## Regression matrix (Q4)

**VERIFIED — codepoints; INFERRED — expected presentation.** All rows below are proposed coverage, **NOT_RUN** in this WO. Offline can check encoded sequence, cmap/record/outline structure and reason about the inspected source; only later runtime QA can confirm the game's fallback, visible stacking, clipping, advances and automatic wrap. Existing ต่ำ+ถี่ specimen format is retained. Synthetic tall-base/tone cases are coverage strings, not a linguistic approval. Test Small/Medium/Large, restart/cache, normal/bold/rich text and narrow/wide boxes; use actual screen captures and preserve input codepoints.

| Specimen | Exact codepoints (VERIFIED) | Expected (INFERRED) | Offline / runtime |
|---|---|---|---|
| ต่ำ | U+0E15 U+0E48 U+0E33 | Nikkhahit below tone, visible separation, sara-aa stays on normal baseline. | Structure only / runtime NOT_RUN |
| ค่ำ | U+0E04 U+0E48 U+0E33 | Nikkhahit below tone, visible separation, sara-aa stays on normal baseline. | Structure only / runtime NOT_RUN |
| ช้ำ | U+0E0A U+0E49 U+0E33 | Nikkhahit below tone, visible separation, sara-aa stays on normal baseline. | Structure only / runtime NOT_RUN |
| ค้ำ | U+0E04 U+0E49 U+0E33 | Nikkhahit below tone, visible separation, sara-aa stays on normal baseline. | Structure only / runtime NOT_RUN |
| ถ้ำ | U+0E16 U+0E49 U+0E33 | Nikkhahit below tone, visible separation, sara-aa stays on normal baseline. | Structure only / runtime NOT_RUN |
| น้ำ | U+0E19 U+0E49 U+0E33 | Nikkhahit below tone, visible separation, sara-aa stays on normal baseline. | Structure only / runtime NOT_RUN |
| จำ | U+0E08 U+0E33 | Single nikkhahit above base and sara-aa on normal baseline; no spurious tone or width change. | Structure only / runtime NOT_RUN |
| ทำ | U+0E17 U+0E33 | Single nikkhahit above base and sara-aa on normal baseline; no spurious tone or width change. | Structure only / runtime NOT_RUN |
| ลำ | U+0E25 U+0E33 | Single nikkhahit above base and sara-aa on normal baseline; no spurious tone or width change. | Structure only / runtime NOT_RUN |
| ป่ำ | U+0E1B U+0E48 U+0E33 | Tone above nikkhahit; tall ascender remains clear; narrow variant/offset must suit this base. | Structure only / runtime NOT_RUN |
| ป้ำ | U+0E1B U+0E49 U+0E33 | Tone above nikkhahit; tall ascender remains clear; narrow variant/offset must suit this base. | Structure only / runtime NOT_RUN |
| ป๊ำ | U+0E1B U+0E4A U+0E33 | Tone above nikkhahit; tall ascender remains clear; narrow variant/offset must suit this base. | Structure only / runtime NOT_RUN |
| ป๋ำ | U+0E1B U+0E4B U+0E33 | Tone above nikkhahit; tall ascender remains clear; narrow variant/offset must suit this base. | Structure only / runtime NOT_RUN |
| ฝ่ำ | U+0E1D U+0E48 U+0E33 | Tone above nikkhahit; tall ascender remains clear; narrow variant/offset must suit this base. | Structure only / runtime NOT_RUN |
| ฝ้ำ | U+0E1D U+0E49 U+0E33 | Tone above nikkhahit; tall ascender remains clear; narrow variant/offset must suit this base. | Structure only / runtime NOT_RUN |
| ฝ๊ำ | U+0E1D U+0E4A U+0E33 | Tone above nikkhahit; tall ascender remains clear; narrow variant/offset must suit this base. | Structure only / runtime NOT_RUN |
| ฝ๋ำ | U+0E1D U+0E4B U+0E33 | Tone above nikkhahit; tall ascender remains clear; narrow variant/offset must suit this base. | Structure only / runtime NOT_RUN |
| ฟ่ำ | U+0E1F U+0E48 U+0E33 | Tone above nikkhahit; tall ascender remains clear; narrow variant/offset must suit this base. | Structure only / runtime NOT_RUN |
| ฟ้ำ | U+0E1F U+0E49 U+0E33 | Tone above nikkhahit; tall ascender remains clear; narrow variant/offset must suit this base. | Structure only / runtime NOT_RUN |
| ฟ๊ำ | U+0E1F U+0E4A U+0E33 | Tone above nikkhahit; tall ascender remains clear; narrow variant/offset must suit this base. | Structure only / runtime NOT_RUN |
| ฟ๋ำ | U+0E1F U+0E4B U+0E33 | Tone above nikkhahit; tall ascender remains clear; narrow variant/offset must suit this base. | Structure only / runtime NOT_RUN |
| ต้ำ | U+0E15 U+0E49 U+0E33 | Correct mai-tho/mai-tri/mai-chattawa above nikkhahit. | Structure only / runtime NOT_RUN |
| ต๊ำ | U+0E15 U+0E4A U+0E33 | Correct mai-tho/mai-tri/mai-chattawa above nikkhahit. | Structure only / runtime NOT_RUN |
| ต๋ำ | U+0E15 U+0E4B U+0E33 | Correct mai-tho/mai-tri/mai-chattawa above nikkhahit. | Structure only / runtime NOT_RUN |
| ถี่ | U+0E16 U+0E35 U+0E48 | Preserve ordinary vowel/tone stacking, base baseline and spacing; no unintended substitution. | Structure only / runtime NOT_RUN |
| ที่ | U+0E17 U+0E35 U+0E48 | Preserve ordinary vowel/tone stacking, base baseline and spacing; no unintended substitution. | Structure only / runtime NOT_RUN |
| ปี้ | U+0E1B U+0E35 U+0E49 | Preserve ordinary vowel/tone stacking, base baseline and spacing; no unintended substitution. | Structure only / runtime NOT_RUN |
| ตี่ | U+0E15 U+0E35 U+0E48 | Preserve ordinary vowel/tone stacking, base baseline and spacing; no unintended substitution. | Structure only / runtime NOT_RUN |
| ตา | U+0E15 U+0E32 | Preserve ordinary vowel/tone stacking, base baseline and spacing; no unintended substitution. | Structure only / runtime NOT_RUN |
| ต่า | U+0E15 U+0E48 U+0E32 | Preserve ordinary vowel/tone stacking, base baseline and spacing; no unintended substitution. | Structure only / runtime NOT_RUN |
| ต้า | U+0E15 U+0E49 U+0E32 | Preserve ordinary vowel/tone stacking, base baseline and spacing; no unintended substitution. | Structure only / runtime NOT_RUN |
| นำ | U+0E19 U+0E33 | Preserve ordinary vowel/tone stacking, base baseline and spacing; no unintended substitution. | Structure only / runtime NOT_RUN |
| ตำ | U+0E15 U+0E33 | Preserve ordinary vowel/tone stacking, base baseline and spacing; no unintended substitution. | Structure only / runtime NOT_RUN |
| ต่ำต่ำ | U+0E15 U+0E48 U+0E33 U+0E15 U+0E48 U+0E33 | Preserve ordinary vowel/tone stacking, base baseline and spacing; no unintended substitution. | Structure only / runtime NOT_RUN |
| ต่ำ ต่ำ | U+0E15 U+0E48 U+0E33 U+0020 U+0E15 U+0E48 U+0E33 | Preserve ordinary vowel/tone stacking, base baseline and spacing; no unintended substitution. | Structure only / runtime NOT_RUN |
| A: ต่ำ ถี่ | U+0041 U+003A U+0020 U+0E15 U+0E48 U+0E33 U+0020 U+0E16 U+0E35 U+0E48 | Atomic target separates and ถี่ control unchanged; reuse A/B R2 specimen format. | Structure only / runtime NOT_RUN |
| B: ตํ่า ถี่ | U+0042 U+003A U+0020 U+0E15 U+0E4D U+0E48 U+0E32 U+0020 U+0E16 U+0E35 U+0E48 | Historical reordered-decomposed diagnostic; do not convert production text. | Structure only / runtime NOT_RUN |
| C: ต่ํา ถี่ | U+0043 U+003A U+0020 U+0E15 U+0E48 U+0E4D U+0E32 U+0020 U+0E16 U+0E35 U+0E48 | Preserve recorded original-order diagnostic interpretation; not a production spelling/fix. | Structure only / runtime NOT_RUN |
| Campus 2026: ต่ำ ถี่ 123 | U+0043 U+0061 U+006D U+0070 U+0075 U+0073 U+0020 U+0032 U+0030 U+0032 U+0036 U+003A U+0020 U+0E15 U+0E48 U+0E33 U+0020 U+0E16 U+0E35 U+0E48 U+0020 U+0031 U+0032 U+0033 | No Latin/number/colon/space change; Thai stacking preserved. | Structure only / runtime NOT_RUN |
| ต่ำ ถี่ น้ำ ⏎ Campus 123 ต่ำ ถี่ | U+0E15 U+0E48 U+0E33 U+0020 U+0E16 U+0E35 U+0E48 U+0020 U+0E19 U+0E49 U+0E33 U+000A U+0043 U+0061 U+006D U+0070 U+0075 U+0073 U+0020 U+0031 U+0032 U+0033 U+0020 U+0E15 U+0E48 U+0E33 U+0020 U+0E16 U+0E35 U+0E48 | Explicit LF retained; also test same text without LF in a narrow box for automatic wrap. | Structure only / runtime NOT_RUN |
| &lt;b&gt;ต่ำ&lt;/b&gt; &lt;color=#FFFFFF&gt;ถี่&lt;/color&gt; | U+003C U+0062 U+003E U+0E15 U+0E48 U+0E33 U+003C U+002F U+0062 U+003E U+0020 U+003C U+0063 U+006F U+006C U+006F U+0072 U+003D U+0023 U+0046 U+0046 U+0046 U+0046 U+0046 U+0046 U+003E U+0E16 U+0E35 U+0E48 U+003C U+002F U+0063 U+006F U+006C U+006F U+0072 U+003E | Rich-text indices/tags preserved; cluster stays intact across layout operations. | Structure only / runtime NOT_RUN |


## Status and one next step

**INCONCLUSIVE.** **UNKNOWN:** exact shipped package/custom source, executing atomic path and live feature flags. A separately remains **BLOCKED_NEEDS_DECISION** because it requires code scope. No bounded candidate is justified for build yet, and BUG-THAI-003 remains OPEN.

**INFERRED — single next step:** PM obtains offline provenance for the exact shipped TMP package/custom source (build lock/package metadata plus matching source/revision or equivalent build artifacts), resolving the execution/feature-flag gates before authorizing a candidate. Public package metadata verifies source downloads, not the game's dependency selection. If provenance is unavailable, retain UNKNOWN and do not treat a structurally valid table patch as a fix.
