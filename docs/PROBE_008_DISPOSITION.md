# Controller disposition — probe-008

Date: 2026-10-16. Report: docs/qa/WO_VISUAL_008_REPORT.md preserved as received. Controller read report, inspected 07-maxfps-tooltip.jpg and independently checked all THREE installed bundles as original. No new runtime session performed.

## Accepted observations

Requested content width/fitter edits did not establish a readable bounded long-English tooltip. Visible region reaches viewport edges; true offscreen width cannot be measured from those bounds. Automatic wrapping NOT_ESTABLISHED. First/last source lines are not visible, which does not prove deletion or their exact offscreen position. Original files restored and hash-checked.

## Required qualifications

Report section 4 and the relay summary overstate causality. No live component inspection, runtime trace or code analysis demonstrates that TooltipController/LayoutWrapper overrides these fields. Possible alternatives include unused/cached prefab, runtime asset selection, another layout owner or TMP settings. Hash verification proves installed bytes, not which object instance was used. Do not claim only a runtime hook or inserted newlines can solve all long text.

Capture dimensions do not alone verify native render resolution. The native screenshot may provide more detail, but scaling pixel measurements between images is not an engine RectTransform measurement.

Regression evidence citations conflict: report cites 06-resolution-tooltip.jpg for VSync despite identifying that image as the long Resolution test; 07-maxfps-tooltip.jpg is cited for both VSync and Quality Presets. Controller inspection of 07 confirms a readable three-line Quality Presets tooltip despite its maxfps filename. Quality Presets is corroborated; VSync remains UNVERIFIED until a corrected per-image citation/transcription is supplied. Do not erase the original report; append a correction if needed.

## Next work

No additional visual test yet. First verify the patched prefab was actually instantiated with a temporary distinctive marker in its serialized default text or another observable, reversible component property, accounting for localisation overwrite; or inspect runtime instances with a separately scoped diagnostic tool. A marker must be chosen so it survives the known runtime path; a changed source tooltip alone cannot prove the UI prefab patch loaded. No loader/assembly installation is implied.

Then trace the TMP text rect and layout ownership and change one verified constraint at a time. Probe-003 remains translation baseline. Long tooltip behavior is not evidence of a Thai-specific defect or a production newline policy. Keep backups and all source texts unchanged.
