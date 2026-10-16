# WO-VISUAL-010 REPORT

Date: 2026-10-16 (Asia/Bangkok). **BLOCKED / NOT TESTED.** Installation failed before bundle mutation. There is no runtime evidence for probe-010 and no basis to grade wrapping, bounds, readability or shared-path regressions.

## Scope and preflight

Read docs/qa/WO_VISUAL_010.md, reports/probe-010-build.json, local/prototype/probe-010/manifest.json, probe-007-long diagnostic-map.json and WO_VISUAL_007_REPORT.md. Inspected existing local/qa/WO-VISUAL-007/17-long-tooltip.jpg directly. Baseline shows a full-viewport horizontal white strip, a single readable middle row clipped at screen edges, with first and last source segments not readable. The middle stimulus contains 12 repeated sentences without LF; source LF indexes are 23 and 719. This baseline observation does not establish probe-010 behavior.

Candidate is the supplied single m_TextWrappingMode raw 1 -> 0 patch, with unchanged probe-007-long English stimulus/fonts. Numeric enum semantics remain unverified. No values, scripts, translations or bundles were edited during this attempt.

## Failure and lifecycle

All manage_probe.py invocations explicitly used --probe probe-010:

1. `python tools/manage_probe.py check --probe probe-010`: all THREE original (01-original.txt).
2. `python tools/manage_probe.py install --probe probe-010`: failed at line 19, subprocess tasklist returned exit status 1, before backup creation or copying bundles. The exact captured combined tool output is preserved in 02-install-failure.txt; 02-install.txt is empty because the initial pipeline captured stdout only.
3. `python tools/manage_probe.py check --probe probe-010`: all THREE original (03-installed.txt; filename does not imply successful installation).
4. `python tools/manage_probe.py restore --probe probe-010`: failed at the same tasklist precondition (04-restore.txt). It did not copy files.
5. `python tools/manage_probe.py check --probe probe-010`: all THREE original (05-final-check.txt).

Stopped the visual test under the work order's “Stop/report any failure” requirement. No install retry or workaround was used. The Steam launch was mistakenly dispatched after the failed install within the same orchestration call. Steam launch initially reported no targetable window, but a subsequent window inventory found Campus. It reached the main menu under ORIGINAL assets and was exited normally using the visible Quit button. No Settings, gameplay, save load, Apply or configuration changes occurred. Restore was attempted before this late window discovery; its guard failed before any mutation. Final hashes below were independently collected after normal Quit; Get-Process found no TPC process.

Direct tasklist diagnostic returned `ERROR: The user name or password is incorrect.` (07-tasklist-error.txt). This is an execution-environment failure, not a probe rendering failure. No force-close, branch switch, commit/push, loader installation or asset upload.

## Actual environment and visual result

Windows desktop; launched through Steam using its returned Two Point Campus app identifier. Main menu displayed build 10.3.169253+2024-12-06.1241 and English labels. Returned screen was 1920 x 1080. English/Medium and native resolution were NOT verified in Settings because testing stopped. Do not carry prior-run settings forward as verified facts.

Probe-010 Resolution tooltip: NOT TESTED. Exact visible line starts/ends, additional breaks in the newline-free middle segment, actual tooltip bounds, first/middle/last completeness, blankness, clipping and glyph scale: unavailable. Original Antialiasing tooltip shared-path regression: NOT TESTED. No new tooltip images exist; the original main-menu observation is saved as 08-original-main-menu.jpg, explicitly not probe evidence. Neither automatic-wrap PASS nor NO OBSERVED IMPROVEMENT is claimed: the candidate never ran. No Thai, dictionary or ZWSP conclusion.

## Final installed hashes and backups

Independent SHA-256 checks after normal Quit (06-final-hashes.json) match originals for ALL THREE:

| Bundle | Actual installed SHA-256 = original |
|---|---|
| fonts_assets_all.bundle | 33aa34892719fbc7caaabd0a292c32bb135bc61978a4cd3ce73c6c40da8f4e6e |
| localisation_assets_localisationenglish.bundle | c1e7ca97f260813ccc9a1cf463f20d066631f8e5616bf797fe8d5ae93227878f |
| ui-prefabs-general_assets_all.bundle | 2152e5ba289ccb0414c462371cfdfe05cc7ac589a10a75b8b46d359afd99786d |

Final state **original/original/original**, unchanged throughout. Restore command success is NOT claimed. No probe-010 backups were created because installation stopped before backup creation; no existing backups were deleted or modified. Evidence and exact command outputs are under local/qa/WO-VISUAL-010/. Runtime comparison remains outstanding pending resolution of the tasklist precondition failure.

## Retry — 2026-10-16 (Asia/Bangkok)

**Runtime test completed: NO OBSERVED IMPROVEMENT versus probe-007-long. Automatic wrapping NOT_ESTABLISHED. Final restoration PASS for all THREE bundles.** This section supersedes only the outstanding runtime status above; the previous BLOCKED attempt is preserved as history.

### Sequential gates and environment

Followed WO_VISUAL_010_RETRY.md and the original work order using the same probe-010. Repaired Toolhelp process guard was retained. Each manager action was issued in a separate call, and its exit code plus all three states were inspected before the next action. Every manager command included `--probe probe-010`:

- `check`: exit 0, original/original/original (retry/01-original.txt).
- `install`: exit 0, probe/probe/probe (02-install.txt).
- `check`: exit 0, probe/probe/probe (03-installed.txt). Manager validates staged and installed SHA-256 against the manifest, and validates original backups. Only after this successful gate was Steam inspected and its visible Two Point Campus Play button clicked, in a later separate call.
- After normal Settings X > main-menu Quit and a fresh window inventory showing Campus absent, `restore`: exit 0, original/original/original (09-restore.txt).
- Final `check`: exit 0, original/original/original (10-final-original.txt).

Windows desktop, Steam Play launch, build 10.3.169253+2024-12-06.1241 (04-main-menu.jpg). English and Medium UI Scale verified visibly (05-en-medium.jpg); Full Screen Window and unchanged 3840 x 2160 @ 60hz verified (06-video.jpg), matching WO-007. Returned captures are 1920 x 1080 JPG. Saved returned original bytes without crop/rescale/annotation. Only main-menu Settings visited; no gameplay/save load, Apply, setting/value change, experiment/code/translation edit, force-close, branch switch, commit/push, loader installation or asset upload.

### Resolution comparison

Evidence: local/qa/WO-VISUAL-010/retry/07-resolution-tooltip.jpg, compared visually against local/qa/WO-VISUAL-007/17-long-tooltip.jpg. Pointer placed at the same window-relative (110,382) using zero-delta scroll, then captured again after the tooltip appeared fully. Bounds below are approximate capture pixels, not native pixels.

The white visible body still spans (0,342)-(1919,425), approximately 1920 x 83 pixels, with both horizontal ends meeting the viewport edges. Its intended full off-screen extent cannot be measured. It obscures the Resolution row. Same position and visible height as the WO-007 long reference; no observed improvement to boundedness, border containment or reading completeness.

Only ONE middle-segment text row is visible, around y=382. Its left edge begins inside a clipped sentence tail, approximately `...nce with ordinary spaces.`; this is followed by approximately four complete occurrences of `This is a readable English sentence with ordinary spaces.`, with the last visible text ending `ordinary spaces.` near x=1910. Pointer and center tooltip arrow obscure small portions. Since all 12 source repetitions are identical, their ordinal identities cannot be assigned. The count describes visible text, not total rendered content. No additional line break within the newline-free repeated middle segment is observed.

First segment `Sets window resolution.` and last segment `Reduce resolution to increase CPU and graphics performance.` are still not visible/readable. Thus all source segments are NOT readable on screen, and exact complete source-line boundaries cannot be reconstructed from this clipped image. No blank tooltip, raw tags or magenta marker visible. English glyph scale appears broadly unchanged from probe-007-long; no runtime font-size measurement or pixel-perfect equality claim.

**NO OBSERVED IMPROVEMENT** in this English case. Do not award automatic-wrap PASS from the single-field patch. This result does not prove the raw enum has no effect in all contexts, resolve numeric enum semantics, or establish Thai/dictionary/ZWSP behavior. No combined patches or parameter adjustments were attempted.

### Separate Antialiasing Mode check

Evidence: retry/08-antialiasing-mode-tooltip.jpg, actual content is the ORIGINAL Antialiasing Mode tooltip, not Quality Presets. Hovered (151,850) without changing SMAA. White body approximately (939,795)-(1337,902), excluding left pointer; all four visible lines complete and on-screen:

1. Enables anti-aliasing, which reduces jagged edges.
2. SMAA is higher quality that FXAA.
3. SMAA is also slower to run than FXAA.
4. Disable to increase graphics performance.

The second line is transcribed as visibly displayed, including `that`. No clipping, blankness or unreadable shrinking observed. No visible shared-path regression in this inspected tooltip; this is a scoped visual check, not a comprehensive regression suite or proof of newly introduced automatic wrapping. Quality Presets was not chased.

### Retry hashes and retained backups

Independent post-Quit/post-restore hashes are recorded in retry/11-final-hashes.json. Installed files AND retained probe-010 backups match the following originals for all THREE; staged candidate hashes also still match the supplied manifest:

| Bundle | Installed and backup SHA-256 (original) | Staged probe-010 SHA-256 |
|---|---|---|
| fonts_assets_all.bundle | 33aa34892719fbc7caaabd0a292c32bb135bc61978a4cd3ce73c6c40da8f4e6e | 588f15fad01635da3fb5b86d5c3946cbb7bd85b40304364294fb23d73c207f3e |
| localisation_assets_localisationenglish.bundle | c1e7ca97f260813ccc9a1cf463f20d066631f8e5616bf797fe8d5ae93227878f | fb3719a4f431e259340d51537395c3077ad5372968635139a69a3402723053c0 |
| ui-prefabs-general_assets_all.bundle | 2152e5ba289ccb0414c462371cfdfe05cc7ac589a10a75b8b46d359afd99786d | c36f1464ade3abf00152522e444631b85f50a65bb95529f17ac1e8cc442969c1 |

Manifest/build/reference diagnostic-map hashes are in retry/12-source-hashes.json. Retry evidence is separate under local/qa/WO-VISUAL-010/retry/. All manager outputs include their inspected exit codes. Final state original/original/original; backups retained. No commit/push.
