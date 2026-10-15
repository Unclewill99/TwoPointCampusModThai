# WO-VISUAL-002 — original/probe-002 Settings comparison

Owner: desktop visual-testing agent. Controller: ChatGPT. Date: 2026-10-15.

Goal: determine whether dropdown selected values are visible in the original build and in the fallback-only probe. probe-001 is FAIL; do not reinstall it. No root cause has been confirmed.

## Preparation

Read WO_VISUAL_001_REPORT.md and ../PROBE_001_HANDOFF.md for context. Use project root as working directory. Confirm real Windows game control and screenshot capability before mutation. Keep game closed for installer actions. Do not force-close unsaved gameplay.

1. Run `python tools/manage_probe.py check --probe probe-002`. Both files must be original; stop on errors.
2. Launch original game through Steam. Capture Settings > Game and Video with dropdowns CLOSED, then open Language and Resolution to compare. Record actual values and UI Scale. Do not apply resolution changes or load a save. This original baseline is mandatory.
3. Quit normally. Run `python tools/manage_probe.py install --probe probe-002`, then `python tools/manage_probe.py check --probe probe-002`. Both files must be probe.
4. Launch through Steam with English. Repeat the same Settings pages at the same supported UI scale. Verify selected values while CLOSED and options while OPEN. Capture matching before/after views.
5. Verify pilot Thai labels still render, especially Audio Language and camera sensitivity. Check missing characters, clipping and Latin/numbers. Restart once and repeat closed Game/Video dropdown checks. Do not infer clean persistent cache.
6. Quit normally. Run `python tools/manage_probe.py restore --probe probe-002`, then `python tools/manage_probe.py check --probe probe-002`. Both files must be original. Keep backups.

## Delivery

Write docs/qa/WO_VISUAL_002_REPORT.md. Store screenshots and exact command outputs in local/qa/WO-VISUAL-002/. Include manifest hashes, build, tested UI scale, baseline/probe paired results and final restoration state. If the original dropdowns are also blank, explicitly record that observation; do not blame the probe alone. If probe dropdowns recover but Thai disappears, report FAIL rather than accepting the regression. Inconclusive comparisons remain BLOCKED.

No font, translation or catalog edits; no branch switching, commit or push. No binary/font uploads. No important-save writes. Synthetic corpus and full shaping/wrapping coverage remain outside this comparison. Results must reflect inspected images, not inferred success from command exit codes.
