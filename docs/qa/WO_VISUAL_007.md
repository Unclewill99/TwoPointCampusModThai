# WO-VISUAL-007 — tag-free English tooltip length control

Date: 2026-10-16. Controller: ChatGPT. Variants: probe-007-short then probe-007-long. English only; no Thai A/B.

Read reports/probe-007-build.json and each local variant manifest/diagnostic-map.json. Verify map hashes first. Short uses the original Resolution tooltip under probe-003's accepted font baseline. Long replaces only its middle explicit line with repeated spaced English; first/last lines and two LF separators stay unchanged. Neither includes rich-text width tags. No fixed width is assumed.

## Procedure

Confirm real desktop/screenshot access and original hashes with `python tools/manage_probe.py check --probe probe-007-short`. Close Campus normally before each install/restore. No save loading, setting changes, Apply, code edits or force-close.

For each VARIANT, use the exact name with every command:

```
python tools/manage_probe.py check --probe VARIANT
python tools/manage_probe.py install --probe VARIANT
python tools/manage_probe.py check --probe VARIANT
```

Start via Steam, English, Medium, unchanged resolution. Settings > Video: hover Resolution at the same location, wait for tooltip and capture full readable output. Record actual visible bounds, line count, text size/readability, offscreen extent, clipping and raw content. Do not assume capture pixels equal native game pixels.

Short gate: all original three lines must remain readable without oversized blank background. If it fails, quit/restore, mark experiment BLOCKED and do not install long.

If short passes, restore it BEFORE installing long. In long, identify every break within the repeated middle segment. Compare with exact diagnostic-map text: only LF separators before/after that segment are manual. Any additional breaks are automatic behavior within the English segment. If single-line shrinking, offscreen growth, blank tooltip or clipping occurs, report exactly that; do not label it a Thai defect. Stop rather than changing text/tags in-session. Single repeated words may be difficult to transcribe; record visible sequence count and line starts/ends when possible, with uncertainty.

Quit and restore each variant:

```
python tools/manage_probe.py restore --probe VARIANT
python tools/manage_probe.py check --probe VARIANT
```

Both must be original before the next variant. Keep backups. No direct probe-to-probe installation. If restoration fails, stop and notify Controller.

## Delivery

docs/qa/WO_VISUAL_007_REPORT.md; inspected screenshots, hashes and exact outputs under local/qa/WO-VISUAL-007/. Separate short baseline acceptance from long behavior. Give automatic wrapping ESTABLISHED only if an extra break within the newline-free middle segment is visible and supported. If text is unreadable, no automatic-wrap PASS. No dictionary or Thai/ZWSP conclusion. Do not commit/push, switch branches, upload game assets or alter translator files.
