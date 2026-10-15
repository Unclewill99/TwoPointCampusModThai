# WO-VISUAL-003 — Thai stacked-mark feature experiment

Controller: ChatGPT. Target: probe-003. Date: 2026-10-15.

## Objective and scope

Retest BUG-THAI-001: sara ii + mai ek overlap in ถี่ within ความถี่. Compare probe-002 baseline evidence with probe-003, which adds Museum Thai serialized font features only. Keep the successful dropdown behavior. Do not assume runtime consumes injected records merely because the bundle loads.

Project folder: D:\SteamLibrary\steamapps\common\Two Point Campus\ThaiCampusMod

Read BUG_THAI_001.md, WO_VISUAL_002_REPORT.md, ../PROBE_003_FINDINGS.md and the new manifest local/prototype/probe-003/manifest.json. Confirm Windows game control and screenshot access. Close game normally before mutations; do not force-close unsaved work.

## Reference inspection

Open local/prototype/probe-003/same-font-reference.html in a desktop browser. This self-contained local page embeds the identical Thai source TTF. Wait for font loading; if capable, verify `await document.fonts.load('500 48px ProbeThai', 'ความถี่')` returns a loaded FontFace and `document.fonts.check('500 48px ProbeThai', 'ความถี่')` is true. If font identity/loading cannot be verified, record that limitation; do not label the page a verified reference. Do not infer font loading from page generation alone.

Capture the BUG-THAI-001 section and inspect separation of ี and ่. Use browser zoom for inspection, record zoom. Browser size/antialiasing differs from the game: compare relative mark placement, not pixel-identical glyph sizes. Other corpus sections are browser-only references, not tested game inputs. Angle-bracket tags are literal on this page by design.

## Install and test

From project root, with game closed:

```
python tools/manage_probe.py check --probe probe-003
python tools/manage_probe.py install --probe probe-003
python tools/manage_probe.py check --probe probe-003
```

Initial state must be original for both files; installed state must be probe. Stop on errors; do not patch or skip guards. Use permitted execution rights if process inspection is blocked, never remove the process check.

Launch via Steam, English, UI Scale Medium, same resolution as WO-VISUAL-002 if already configured. Do not apply resolution changes or load a save.

1. Settings > Game: capture full screen and a close view of ความถี่. Compare with the previous 06-probe-game-closed.jpg and browser reference. Record whether marks separate, still overlap, disappear, float or clip.
2. Confirm closed/open Language and UI Scale values remain visible. Settings > Video: confirm current values remain visible.
3. Inspect Thai labels still present. Restart once, repeat ความถี่ and closed Game dropdown checks. Record no persistent-cache-clearing claim.
4. If safely supported, compare Small and Large UI Scale, recording actual setting and returning to Medium afterward. If any scale makes navigation difficult, revert immediately; do not force coverage.

FAIL the mark case if overlap remains. A no-change result is useful evidence; do not adjust code, font data or text during testing. If only dropdown tests pass, do not give overall mark-fix PASS. A single correctly placed word does not pass the full shaping matrix. Synthetic corpus injection and Thai wrapping are not included in this build.

## Restore and deliver

Quit normally, then:

```
python tools/manage_probe.py restore --probe probe-003
python tools/manage_probe.py check --probe probe-003
```

Both files must be original. Keep backups. Save inspected screenshots/command outputs under local/qa/WO-VISUAL-003/ and write docs/qa/WO_VISUAL_003_REPORT.md. Include hashes, environment, reference loading evidence, scale/zoom, paired observations, restart results and final restoration state. No branch switch, commit/push, asset upload or edits to translations. No important-save writes. Stop and report if restoration fails.
