# WO-VISUAL-008 — traced tooltip width experiment

Date: 2026-10-16. Target probe-008. English control only. Read reports/probe-008-layout-trace.json and build report/manifest. This probe includes THREE bundles, including UI prefabs. It shares the same long English stimulus as probe-007-long; only two UI objects change. Shared tooltip prefab changes may affect other tooltips.

Confirm desktop access. Close game normally. Run from project root:

```
python tools/manage_probe.py check --probe probe-008
python tools/manage_probe.py install --probe probe-008
python tools/manage_probe.py check --probe probe-008
```

Preflight must show original for ALL THREE files, installed check probe for all three. Stop on mismatch; no direct probe switching or bypass of guards.

Launch via Steam. English/Medium, unchanged resolution. Main menu Settings > Video, hover Resolution as in WO-007. Capture readable full screen, approximate white background/text bounds, line count, line starts/ends, clipping, text scale and blank regions. Compare existing WO-007 17-long-tooltip.jpg without reinstalling old probes. The requested 800 Unity-unit content width is NOT a guaranteed native/capture-pixel width. Observe actual results.

Classify independently: (a) width bounded or still viewport/offscreen growth; (b) English automatic wrapping established only if extra breaks occur inside the newline-free repeated middle segment; (c) readability/clipping. Bounded width alone is not wrapping PASS. If clipped or blank, report FAIL/setup and do not change TMP fields or experiment with Thai. If usable, also hover original MaxFPS/Antialiasing tooltips briefly to spot shared-prefab regressions; do not change settings. No gameplay/save load, Apply or sliders. No persistent-cache claims.

Quit normally, then:

```
python tools/manage_probe.py restore --probe probe-008
python tools/manage_probe.py check --probe probe-008
```

ALL THREE files must return original; retain backups. If restoration fails stop and report. Save inspected images/exact outputs in local/qa/WO-VISUAL-008/; write docs/qa/WO_VISUAL_008_REPORT.md including manifest hashes, environment, comparison and restoration. No code/translation edits, branch switching, commit/push or asset uploads. No Thai/ZWSP conclusion from this English run.
