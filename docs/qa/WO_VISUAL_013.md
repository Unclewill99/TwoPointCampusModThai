# WO-VISUAL-013 — actual Thai tooltip scale regression

Date: 2026-10-17. Target probe-013. Read reports/probe-013-build.json, local manifest and tooltip-map.json; verify map hash. Candidate includes 50 pilot r3 strings and 20 actual tooltip r2 translations. No synthetic repeated body or ZWSP. Font/UI bytes equal accepted bounded experiment; fixed width remains experimental/shared, not approved globally.

With Campus normally closed, run commands in separate inspected calls:

```
python tools/manage_probe.py check --probe probe-013
python tools/manage_probe.py install --probe probe-013
python tools/manage_probe.py check --probe probe-013
```

Require ALL THREE original before and probe after. Only then launch via Steam. English, existing resolution unchanged; main-menu Settings only, no gameplay/save loading, Apply or graphics changes.

## Test scope

At Medium, inspect Resolution, FullScreenMode, MaxFPS/Framerate Limit, AntialiasingMode and VSync tooltips. Capture each separately with identifying visible control and exact map key. Inspect other translated tooltips that are safely accessible by hovering while scrolling Video; do not promise all 20 are exposed. Mark unobserved as NOT_OBSERVED/NOT_RUN, never PASS from source presence. Do not chase missing controls or enter gameplay.

Repeat the five primary tooltips at Small and Large UI Scale. Change ONLY UI Scale, then return Medium before exit. If navigation becomes hard, revert immediately; record incomplete coverage. Record actual setting for each image. Keep resolution constant; actual frame capture size does not prove render resolution.

For each key/scale: full text completeness, actual bounds, line count, original LF vs extra wrapping, Thai line-boundary quality (no stranded leading vowels/marks), missing glyphs, clipping, readability, empty space/position and overlap with screen edges. Use map text to account for every segment. Transcribe problematic boundaries exactly; do not guess pixels. Source LF retained intentionally; do not mistake all multiline display for automatic wrapping. Compare key wording to visible English setting labels as provisional consistency observations, not final glossary approval.

Inspect CharacterLimits only if naturally accessible without settings changes; otherwise NOT_RUN. Do not toggle limits or supply fake variables. Literal variable tokens, bad substitutions or colour-tag text visible are defects to record, not fix in-session. MaxFPS/VSync behavior is NOT part of this visual WO; do not change graphics values to test it.

Confirm closed dropdown values remain visible. Restart once at Medium and recheck Resolution and Antialiasing. No persistent-cache-clearing claim. Stop if loading/UI fails, capture evidence and restore.

## Restoration and report

Quit normally, then:

```
python tools/manage_probe.py restore --probe probe-013
python tools/manage_probe.py check --probe probe-013
```

Require originals for ALL THREE, retain backups. Save inspected images/exact outputs in local/qa/WO-VISUAL-013/. Write docs/qa/WO_VISUAL_013_REPORT.md with per-key/per-scale matrix, exact image references, manifest/map hashes, environment, restart and final restoration. No code/translation/map edits, branch switches, commit/push, force-close, loader or asset uploads. Scoped visual results only, not release approval.
