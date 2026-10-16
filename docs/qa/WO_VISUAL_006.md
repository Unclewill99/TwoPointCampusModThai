# WO-VISUAL-006 — original English multiline baseline (no installation)

Date: 2026-10-16. Controller: ChatGPT.

Goal: find a readable, bounded, automatically wrapping English text component in the original game's main-menu UI. This is investigation only, not a new patch test. Do not install any probe, edit assets or load gameplay.

1. Run `python tools/manage_probe.py check --probe probe-003`. Both bundles must be original. If not, stop and report; do not independently restore an unknown active session.
2. Launch original game through Steam. Record game build, English, actual UI Scale and resolution. Keep existing values, no Apply or slider changes.
3. Inspect Settings > Video tooltips for Antialiasing Mode, Max FPS/Framerate Limit, Quality Presets, Render Scale and Resolution where available. Hover without changing options. Capture full readable text and approximate bounds/line count. If a control isn't present, report not observed rather than guessing.
4. If none offers useful wrapping, inspect a reversible Quit-to-Desktop confirmation dialog only if it can be safely opened and canceled; never confirm deletion, overwrite or gameplay changes. Record the visible dialog text and exact navigation. Cancel/return normally.
5. Compare text to local/source/all-english.json, especially I2LS_UI_Settings keys UI/Settings/Tooltips/AntialiasingMode, MaxFPS, QualityPresets, RenderScale, Resolution. Locate candidate dialog text by exact content, not by inventing keys. Record source key and positions of actual newline characters. Multiple lines matching explicit source newlines alone do NOT establish automatic wrapping. Record any extra break inside an original newline-free segment.
6. A usable candidate must show readable bounded English and at least one automatic line break within a source segment containing no manual break at that position. Otherwise mark automatic wrapping NOT_ESTABLISHED. Do not infer runtime prefab identity from shape/name alone.
7. Quit normally; rerun the same read-only hash check. No install/restore commands are needed because no files were changed.

Delivery: docs/qa/WO_VISUAL_006_REPORT.md, inspected screenshots and source-comparison notes under local/qa/WO-VISUAL-006/. Distinguish explicit vs automatic line breaks, clipping vs resizing, facts vs hypotheses. If font/layout measurements are unavailable, state limits. No branch switch, commit/push, binary upload, save load or important-settings changes. If no suitable component is found, that is a valid investigation outcome; do not expand into gameplay without a new assignment.
