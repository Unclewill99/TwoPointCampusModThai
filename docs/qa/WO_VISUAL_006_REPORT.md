# WO-VISUAL-006 REPORT

Date: 2026-10-16 (Asia/Bangkok). Result: **automatic wrapping NOT_ESTABLISHED** within the inspected original main-menu UI. Readable multiline English tooltips were found, but every observed break matches an actual source newline. No probe installed and no game/source assets edited.

## Environment and procedure

Read-only `python tools/manage_probe.py check --probe probe-003` returned original/original before launch (01-original-check.txt). Launched through Steam Library > Two Point Campus > Play. Game build shown: 10.3.169253+2024-12-06.1241 (03-build.jpg). Main menu > Settings > Game showed English for both language values and UI Scale Medium (04-english-medium.jpg). Video showed Full Screen Window, 3840 x 2160 @ 60hz (05-video-resolution.jpg). Kept all values unchanged. No Apply, slider adjustment, preset selection, save load, gameplay, install or restore command.

Used the computer-use skill and real Windows UI. Hover used zero-delta scroll to place the pointer, without clicking controls. Screenshots inspected after tooltip fade-in. Saved full images exactly as returned by capture (1920x1080 JPG); no subsequent crops, rescaling or annotations. Reported bounds are approximate visual bounds in capture pixels, not native 4K dimensions or engine layout measurements. Font point size, native text container size, auto-size rules and prefab identity were not measured.

## Source comparison

Source: local/source/all-english.json, asset I2LS_UI_Settings. Exact strings, source segments, and zero-based Python Unicode indexes of actual LF characters are preserved in 02-source-comparison.json. JSON `\n` here represents an actual LF in the decoded source, not the two literal characters backslash+n.

| Tooltip | Observed readable lines / approximate white-body bounds (x1,y1)-(x2,y2) | Actual LF indexes | Comparison and result |
|---|---|---|---|
| UI/Settings/Tooltips/Resolution | 3; (939,342)-(1426,425) | 23, 78 | Each source segment appears as one complete line. No extra break. Explicit newlines only; auto wrap NOT_ESTABLISHED. 06-resolution-tooltip.jpg |
| UI/Settings/Tooltips/MaxFPS (Framerate Limit label) | 3; (939,530)-(1427,613) | 49, 113 | Each source segment is one complete line. No extra break. Explicit newlines only; auto wrap NOT_ESTABLISHED. 07-maxfps-tooltip.jpg |
| UI/Settings/Tooltips/AntialiasingMode | 4; (939,795)-(1338,903) | 50, 84, 122 | Each source segment is one complete line. No extra break. Explicit newlines only; auto wrap NOT_ESTABLISHED. 10-antialiasing-tooltip.jpg |
| UI/Settings/Tooltips/QualityPresets | Tooltip not observed | 49, 118 | Hovered heading at (472,719), then existing Very High preset at (825,761), without clicking, and recaptured after waiting. Neither produced tooltip. Source existence does not establish activation. 08-quality-heading-no-tooltip.jpg, 09-quality-control-no-tooltip.jpg |
| UI/Settings/Tooltips/RenderScale | Control not observed | 54, 128 | Inspected Video from top through advanced options and bottom (World Detail); no Render Scale label observed. No guessed activation point. 05-video-resolution.jpg, 11-video-bottom.jpg |

Observed line transcriptions, in order (each listed line matches one original newline-free segment):

Resolution:

1. Sets window resolution.
2. Higher resolution makes the whole game appear sharper.
3. Reduce resolution to increase CPU and graphics performance.

MaxFPS:

1. Limits the maximum framerate the game can run at.
2. Lower this if you find your machine is running too hot or loud.
3. Does not work in conjuction with VSync.

AntialiasingMode:

1. Enables anti-aliasing, which reduces jagged edges.
2. SMAA is higher quality that FXAA.
3. SMAA is also slower to run than FXAA.
4. Disable to increase graphics performance.

Spelling above follows source and screen (including “conjuction” and “quality that”). All three readable tooltips were on-screen, bounded, and visually unclipped. Their different body widths are observed; whether width follows content or an auto-size rule is unverified. Multiple explicit lines alone do not prove automatic wrapping. No extra break inside a newline-free source segment was observed.

## Quit path

With no useful automatic-wrapping candidate established, returned via Settings upper-right X to main menu (12-before-quit.jpg), then selected Quit at (273,925). The game closed directly: state capture reported no screenshot target and a fresh window inventory contained no Two Point Campus window. No reversible confirmation dialog was observed, so there is no visible dialog text to match to source and no dialog key was invented. No confirmation, deletion, overwrite or gameplay action occurred. This also completed normal exit.

## Final integrity and limits

Final same read-only check `python tools/manage_probe.py check --probe probe-003` returned original/original (13-final-check.txt). 14-hashes.json records installed bundle and source hashes. Final original bundle SHA-256:

- fonts_assets_all.bundle: 33aa34892719fbc7caaabd0a292c32bb135bc61978a4cd3ce73c6c40da8f4e6e
- localisation_assets_localisationenglish.bundle: c1e7ca97f260813ccc9a1cf463f20d066631f8e5616bf797fe8d5ae93227878f

Evidence and comparison notes are under local/qa/WO-VISUAL-006/. This investigation establishes explicit multiline English display in three Settings tooltips, but does not establish automatic English wrapping or any Thai wrapping behavior. QualityPresets activation and RenderScale runtime display remain not observed. No gameplay expansion, file patch, branch switch, commit/push or upload. Only the requested report and evidence files were created.
