# WO-VISUAL-009 — visible prefab-consumption marker

Date: 2026-10-16. Target probe-009. Purpose: test whether the traced arrowLeft TMP asset supplies visible Settings tooltip text. NOT a width or wrapping fix.

The probe reuses probe-007-short original English tooltip and accepted fonts. Only one UI object changes: its TMP font colour becomes bright magenta (RGB 1,0,1). No layout, wrapping, material or text modifications. Read reports/probe-009-build.json and local/prototype/probe-009/manifest.json. Three bundles are involved.

With Campus closed normally, from project root:

```
python tools/manage_probe.py check --probe probe-009
python tools/manage_probe.py install --probe probe-009
python tools/manage_probe.py check --probe probe-009
```

Require original for all THREE before install and probe for all three afterward. Stop on mismatches. Start via Steam; English/Medium, existing resolution unchanged. Settings > Video > hover Resolution. Capture full screen and readable tooltip after fade-in. Compare prior original/short evidence: does its three-line text become magenta or retain the dark original colour? Record mixed/partial colour if present. Inspect Antialiasing and Quality Presets tooltips with separate images and transcribe identifying text to prevent the prior filename/citation mismatch. Do not change settings or Apply.

If magenta appears, record positive marker evidence supporting consumption of the patched serialized TMP path; it does not prove a specific runtime layout controller override or object instance identity. If it remains dark, record INCONCLUSIVE: colour may be overwritten, prefab bypassed/cached or another path used. Do not call absence proof that the asset is unused. If unreadable/blank, capture and stop; no in-session font or code patch.

Quit normally and restore:

```
python tools/manage_probe.py restore --probe probe-009
python tools/manage_probe.py check --probe probe-009
```

Require original for ALL THREE; keep backups. No gameplay/save load, code edits, loader installation, branch changes, commit/push or asset uploads. Do not test probe-008/long in this run. Save inspected images/exact command outputs under local/qa/WO-VISUAL-009/ and report docs/qa/WO_VISUAL_009_REPORT.md with marker result, actual environment, hashes and final state. No Thai/ZWSP or automatic-wrapping claims.
