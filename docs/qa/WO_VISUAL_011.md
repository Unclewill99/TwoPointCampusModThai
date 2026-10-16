# WO-VISUAL-011 — text child width ownership

Date: 2026-10-16. Target probe-011. Read reports/probe-011-build.json and manifest. Paired constraint experiment: text RectTransform width=800 and parent layout ChildControlWidth=0. Original Normal wrapping, content fitter and long English stimulus retained. Not a single-factor test and not a claimed fix. Three bundles.

Run all commands sequentially, inspect exit code and states before continuing. Game must be closed normally. Do not launch Steam in the same orchestration block as install.

```
python tools/manage_probe.py check --probe probe-011
python tools/manage_probe.py install --probe probe-011
python tools/manage_probe.py check --probe probe-011
```

Require original/original/original before and probe/probe/probe after. Stop on error; no guard bypass or force-close. Then launch normally through Steam, English/Medium, unchanged resolution. Main-menu Settings > Video, hover Resolution at the same location as WO-007; no Apply/settings changes/gameplay/save load.

Capture full readable tooltip and compare WO-007 long evidence. Report actual background/text bounds, extra line breaks inside the newline-free repeated middle segment, first/last source lines, completeness, glyph scale, clipping and blankness independently. Requested 800 units is not a measured native/capture width. Normal enum does not prove runtime wrapping. If actual multiple readable lines occur, transcribe starts/ends and separate manual LF boundaries from additional breaks. If unchanged or clipped, report it and do not adjust more fields.

Also capture original Antialiasing tooltip separately; shared layout patch may change its width/height/placement. Check readability and unexpected empty space/clipping. No need to chase Quality Presets. No Thai, ZWSP, dictionary or atlas conclusion.

Quit normally:

```
python tools/manage_probe.py restore --probe probe-011
python tools/manage_probe.py check --probe probe-011
```

Require originals for ALL THREE and retain backups. Stop/report restore failure. Save inspected screenshots/exact outputs in local/qa/WO-VISUAL-011/; report docs/qa/WO_VISUAL_011_REPORT.md with hashes/environment/comparisons/final state. No script/translation edits, branch changes, commit/push, loader installation or asset uploads.
