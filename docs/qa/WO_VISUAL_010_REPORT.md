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
