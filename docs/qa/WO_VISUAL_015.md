# WO-VISUAL-015 — QualityPresets parent-gap diagnostic

Date: 2026-10-18. Prepared for Antigravity / desktop QA. Runtime NOT_RUN. Unchanged probe-013, not probe-015. Read ../TOOLTIP_NATIVE_FINDINGS.md, ../WO_VISUAL_014_ACCEPTANCE.md, WO_VISUAL_014_REPORT.md and probe-013 manifest/map. Preserve the accepted 17-key matrix; do not repeat it.

## Question

Does hovering a visible empty gap/padding area of the preset BUTTON ROW expose the parent OptionsQuality tooltip? Native code can stop at a foreground child Image before reaching the provider on the parent. Heading and selected Very High were already tested; neither is this assignment's target. Runtime activation is a hypothesis, not an established PASS.

## Preflight and lifecycle

Require working current desktop target capture and documented non-mutating pointer placement, as for WO-014. If unavailable, stop before install and record the failed capability. With Campus closed normally, execute separately and inspect each successful result:

1. `python tools/manage_probe.py check --probe probe-013` — all THREE original; verify unchanged manifest/map/staged hashes.
2. `python tools/manage_probe.py install --probe probe-013` — all THREE probe.
3. `python tools/manage_probe.py check --probe probe-013` — all THREE probe.
4. Only afterward launch through Steam in a later call. Verify current build, English, unchanged resolution, Medium UI Scale and Settings > Video.

Only UI Scale may change. No preset/button/background click, graphics dropdown/slider change, Apply, hidden-row enabling, gameplay, save load, loader/injection or asset change. Backups must remain intact. Do not use a fabricated test tooltip or a new build.

## Bounded diagnostic

At Medium, inspect a fresh unobscured capture of Quality Presets. Identify an actual empty strip/gap INSIDE the five-button row's region, between button backgrounds or in its visible padding, away from the heading, text, icons and buttons. Record the chosen point on the original screenshot in the report; preserve unedited original capture bytes. Serialized Unity coordinates are not screen coordinates.

If no distinct safe gap is visible at current capture detail, mark NOT_RUN/no reliable parent-gap target and stop the diagnostic. Do not enlarge the UI resolution, click, guess a narrow invisible gap or modify raycast targets.

Move the pointer to the chosen gap using documented non-mutating placement. Hold still for 1.8 seconds, then take one fresh capture. At most one alternative clearly visible parent-gap point at Medium is allowed if the first produces no tooltip. Move to empty background between attempts so the hover timer resets. Do not repeat the heading/selected-preset targets or chase other settings.

If no tooltip appears, mark NOT_OBSERVED for attempted points, stop, and do not test Small/Large. This means activation not established, not missing translation or proven defect.

Only if Medium exposes the actual QualityPresets tooltip: compare its complete text with tooltip-map, record identifying controls, bounds, line count, source LF versus extra wraps, containment/clipping/readability/base/mark boundaries and unused-width effects. Then inspect the same parent-gap target at Small and Large, at most one 1.8-second attempt per scale if a reliable visible gap exists. Record actual text rather than trusting filenames. If Medium text is wrong, clipped or clearly defective, record it and stop expansion. No restart or prior primary-key regression is required.

## Restoration and report

Return UI Scale to Medium, capture it, quit normally. After game closure execute separately:

1. `python tools/manage_probe.py restore --probe probe-013`
2. `python tools/manage_probe.py check --probe probe-013`

Require all THREE original; independently verify original/backup/staged and manifest/map hashes. Restore on every path after installation, including an unavailable gap or no observed tooltip. If restoration fails, stop and report without bypass.

Write docs/qa/WO_VISUAL_015_REPORT.md with original evidence under local/qa/WO-VISUAL-015/. Include capability, actual environment, exact attempted point descriptions/capture references, wait duration, per-scale outcomes, limitations and final Medium/original state. AnimationSkinningQuality and RenderScale stay outside scope. No all-20 or release claim, branch switch, commit/push or game asset upload by the tester.
