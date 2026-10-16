# WO-VISUAL-007 REPORT

Date: 2026-10-16 (Asia/Bangkok). **Short baseline PASS. Long: horizontal expansion/off-screen clipping; automatic wrapping NOT_ESTABLISHED.** English-only observation; no Thai, dictionary-breaking or ZWSP conclusion.

## Preflight and environment

Read WO_VISUAL_007.md, reports/probe-007-build.json and both manifests/maps before testing. Verified both map hashes against their respective manifests (01-map-hashes.json). Short map uses the original three-line Resolution tooltip. Long has exactly two LF separators at zero-based indexes 23 and 719, surrounding a newline-free middle segment containing 12 repetitions of `This is a readable English sentence with ordinary spaces.` separated by spaces. First/last source lines unchanged. No width/rich-text tags. Build report also records binding_matches=4 and scan_read_errors=1; no stronger static binding claim is inferred.

Used computer-use skill and real desktop captures. Started each variant separately through Steam Play. Game build 10.3.169253+2024-12-06.1241. English, Medium UI Scale, Full Screen Window, unchanged 3840 x 2160 @ 60hz verified for both (06/07 and 15/16). Only main-menu Settings visited, no gameplay/save load. No resolution selection, settings change, Apply, slider interaction, source/script/map/translation edit or force-close.

Hovered Settings > Video > Resolution label at the same window-relative (110,382) for each run, with zero-delta scroll pointer placement, then captured after fade-in. Full-screen returned captures are 1920x1080 JPG despite native resolution above. Saved original returned image bytes; no subsequent crop/rescaling/annotation. Approximate bounds below are capture pixels, not native game pixels. Native font point size, full container width and prefab identity unavailable.

## Short gate

Evidence: 08-short-tooltip.jpg. White body approximately (939,342)-(1426,425), about 487x83 captured pixels, excluding pointer. Three readable lines, all complete and on-screen:

1. Sets window resolution.
2. Higher resolution makes the whole game appear sharper.
3. Reduce resolution to increase CPU and graphics performance.

These correspond exactly to source lines separated at LF indexes 23 and 78. No extra break, clipping, oversized blank background or raw tags. Text legible at approximately the same visible scale as the original WO-006 tooltip; no runtime point-size measurement. **Short gate PASS**, scoped to intact original tooltip under the accepted font baseline.

Quit normally via Settings X > main-menu Quit. Restored short and checked original/original; separately recorded actual installed hashes before installing long. No direct probe-over-probe installation.

## Long behavior

Evidence: 17-long-tooltip.jpg. White region approximately (0,342)-(1919,425), spanning the full viewport width at the same vertical range as short. Full horizontal extent lies beyond measurable screen bounds or is clipped at them; cannot calculate actual intended width. The region obscures the Resolution row. It is not blank: one long English row is visible at about y=382.

The visible middle row begins at the left screen boundary in the middle of a sentence (roughly `...nce with ordinary spaces.`), followed by four complete visible occurrences of `This is a readable English sentence with ordinary spaces.` ending near the right screen edge. Repetitions are identical and edges/pointer obscure small portions, so ordinal identities among the 12 source repetitions cannot be assigned confidently. Visible sequence count is approximately four complete sentences plus the leading partial tail, not a claim that only four were rendered. The first source line `Sets window resolution.` and final source line `Reduce resolution to increase CPU and graphics performance.` are not visible/readable in the captured long tooltip, despite remaining present in the map. Their absence is recorded without asserting deletion or a particular renderer cause.

No additional visible line break occurs inside the repeated middle segment. Visible English glyph size remains broadly similar to short (not a single tiny unreadable shrunk line); precise font-size equality is unmeasured. Dominant observed behavior is horizontal growth and clipping/off-screen content, rather than a readable bounded multiline middle segment. No literal tags visible and none exist in source. No in-session changes attempted to force a different result.

**Automatic wrapping NOT_ESTABLISHED; no automatic-wrap PASS.** This does not prove wrapping is universally disabled, identify an internal layout setting, or establish any Thai/ZWSP behavior. Only the visible English case at these unchanged settings is covered.

## Lifecycle, command evidence and hashes

Every manager invocation used the exact variant being checked/installed/restored. Sequence:

- probe-007-short: check original/original (02), install probe/probe (03), check probe/probe (04), normal Quit, restore original/original (09), check original/original (10).
- Between variants: actual original hashes saved in 11-between-original-hashes.json; probe-007-long check original/original (12).
- probe-007-long: install probe/probe (13), check probe/probe (14), normal Quit, restore original/original (18), check original/original (19).

Files named by those numeric prefixes are exact saved command outputs under local/qa/WO-VISUAL-007/. Final installed and retained backups for both variants are recorded in 20-final-hashes.json. Original hashes verified after each run:

| Bundle | Original SHA-256 |
|---|---|
| fonts_assets_all.bundle | 33aa34892719fbc7caaabd0a292c32bb135bc61978a4cd3ce73c6c40da8f4e6e |
| localisation_assets_localisationenglish.bundle | c1e7ca97f260813ccc9a1cf463f20d066631f8e5616bf797fe8d5ae93227878f |

Build report SHA-256: 2dd293d31fea51c17ca82edd19f481381942cb56f62120de41fa6c84caeec7f7.

| Variant | Manifest SHA-256 | Map SHA-256, verified |
|---|---|---|
| probe-007-short | bf0f3744ff0c14cee9f90d5c844ba90f58dd96287fc5b8d196213285a2b5a65b | 7a47b79bb2ce314d22bd7b272f4154625c2b6c1bf3a880fd50b1dcb0d5f5e687 |
| probe-007-long | 9fcf07c737efd59f802fe282766c0e613ab1e610e652278f095a33952f6e2f64 | ba90466a2bf3bd0f294d5c16f2e91b67470c81a8b93b7bfaf7d3ed82d67ed497 |

Manager verified staged/installed probe hashes: common font 588f15fad01635da3fb5b86d5c3946cbb7bd85b40304364294fb23d73c207f3e; short localisation 4f1e6033cd54b3bf6f97a3f644dd9598514bac6d53781dcc235fe8d3177dd567; long localisation fb3719a4f431e259340d51537395c3077ad5372968635139a69a3402723053c0.

Final state original/original, backups retained. No commit/push, branch switch or asset upload. Only temporary authorized install/restore and requested evidence/report creation.
