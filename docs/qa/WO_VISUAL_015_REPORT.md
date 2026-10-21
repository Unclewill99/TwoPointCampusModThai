# WO-VISUAL-015 REPORT

Date: 2026-10-18 (Asia/Bangkok). **Completed: actual QualityPresets tooltip observed at Medium, Small and Large using one visible parent-gap hover per scale. Scoped visual PASS. Final Medium and all THREE original verified.** Unchanged probe-013; no probe-015 or new build.

## Capability and inputs

Read WO_VISUAL_015.md, TOOLTIP_NATIVE_FINDINGS.md, WO_VISUAL_014_ACCEPTANCE.md, WO_VISUAL_014_REPORT.md and unchanged probe-013 manifest/map. Current Computer Use skill/API/guidance/confirmations had already been read in this conversation. Windows native target capture and documented coordinate-based non-mutating pointer placement were reverified in the current session before installation. Fresh inventory showed Campus absent; selected the unique returned Steam window via get_window, activated it, inspected the correct Steam image, then used sky.scroll with scrollX=0, scrollY=0 at (580,610). The pointer visibly moved without click or scrolling: [00-steam.jpg](../../local/qa/WO-VISUAL-015/00-steam.jpg), [00-pointer-placement.jpg](../../local/qa/WO-VISUAL-015/00-pointer-placement.jpg). No guessed hover API or native-input bypass.

Pre-install manager check found all three originals. Manifest/map/staged verification matched: [01-input-hashes.json](../../local/qa/WO-VISUAL-015/01-input-hashes.json). Installation and the separate installed check both passed for all three before launching through the returned Steam game identifier in a later call. launch_app reported no targetable window before startup finished; fresh inventory then found one Campus window, which was explicitly selected/activated and visually verified. No blind input followed the launch message. [02-windows.json](../../local/qa/WO-VISUAL-015/02-windows.json).

## Actual environment

- Build 10.3.169253+2024-12-06.1241: [03-menu-build.jpg](../../local/qa/WO-VISUAL-015/03-menu-build.jpg).
- English and initial Medium: [04-medium-english.jpg](../../local/qa/WO-VISUAL-015/04-medium-english.jpg).
- Full Screen Window, unchanged 3840 x 2160 @ 60hz; VSync On, Framerate Limit Unlimited: [05-medium-gap-targets.jpg](../../local/qa/WO-VISUAL-015/05-medium-gap-targets.jpg). No graphics setting was changed or applied.
- Scale path Medium -> Small -> Large -> Medium: [S-setting.jpg](../../local/qa/WO-VISUAL-015/S-setting.jpg), [L-setting.jpg](../../local/qa/WO-VISUAL-015/L-setting.jpg), [R-medium.jpg](../../local/qa/WO-VISUAL-015/R-medium.jpg). At Large, a normal Game-list scroll exposed the initially partly obscured scale row fully; no setting other than UI Scale changed.

All image files preserve the returned original screenshot bytes without crop, resize, annotation or re-encoding. Captures are 1920 x 1080; this is not the game's render resolution. Coordinates below refer to the inspected screenshot/window coordinate system, not serialized Unity coordinates.

## Exact bounded targets and outcomes

The target was the visible beige separator between the Low and Medium button backgrounds, inside the five-button row. It is outside the heading, label text/icons and colored button backgrounds. It was selected from each fresh unobscured image, not by scaling serialized positions or assuming the previous scale's coordinate. The separator is narrow but distinctly visible at the returned image detail: approximately x=377..382 at Medium, x=313..317 at Small, x=419..424 at Large. Points were placed in its center at a height within the button row, away from text. The original pre-hover captures allow independent inspection of the target before the cursor obscures it.

| Scale | Original target capture | Exact point (x,y) | Hold | Attempts | Actual tooltip evidence | Outcome |
|---|---|---|---|---|---|---|
| Medium | [05-medium-gap-targets.jpg](../../local/qa/WO-VISUAL-015/05-medium-gap-targets.jpg) | (379,755) | 1.8 seconds | 1 | [M-QualityPresets.jpg](../../local/qa/WO-VISUAL-015/M-QualityPresets.jpg) | OBSERVED; scoped visual PASS |
| Small | [S-gap-target.jpg](../../local/qa/WO-VISUAL-015/S-gap-target.jpg) | (315,654) | 1.8 seconds | 1 | [S-QualityPresets.jpg](../../local/qa/WO-VISUAL-015/S-QualityPresets.jpg) | OBSERVED; scoped visual PASS |
| Large | [L-gap-target.jpg](../../local/qa/WO-VISUAL-015/L-gap-target.jpg) | (421,823) | 1.8 seconds | 1 | [L-QualityPresets.jpg](../../local/qa/WO-VISUAL-015/L-QualityPresets.jpg) | OBSERVED; scoped visual PASS |

Each attempt used documented sky.scroll coordinate placement with zero deltas, held still for an explicit 1800 ms, then took one fresh capture. Medium succeeded on its first point, so no alternative attempt or between-attempt reset was needed. Scale navigation moved the pointer away before the next scale's independent attempt. No heading or selected Very High hover was repeated, and no preset/button/background was clicked. Very High remained selected in all evidence images. The 17 accepted keys were not tested again; AnimationSkinningQuality and RenderScale were outside scope.

This establishes runtime activation at these visible gaps. It is consistent with the static foreground-child-raycast explanation, but does not measure runtime raycast order or prove which internal component was hit. The two negative WO-014 heading/button observations remain valid for their different targets.

## Actual text and layout

Exact key: UI/Settings/Tooltips/QualityPresets. All three captures visibly show these four rows:

~~~text
เลือกจากพรีเซ็ตคุณภาพกราฟิกหลายระดับ
พรีเซ็ตที่สูงขึ้นให้คุณภาพกราฟิกดีกว่า แต่ประสิทธิภาพต่ำลง
พรีเซ็ตระดับต่ำกว่าจะลดคุณภาพกราฟิกเพื่อให้ประสิทธิภาพ
ดีขึ้น
~~~

All first, middle and last source text is accounted for. [93-observed-text.json](../../local/qa/WO-VISUAL-015/93-observed-text.json) records the manually transcribed rows and whitespace-insensitive comparison against tooltip-map; comparison matched. Source contains 2 LF delimiters, while the rendered text has 4 rows: one additional runtime break in the final source segment, exactly “พรีเซ็ตระดับต่ำกว่าจะลดคุณภาพกราฟิกเพื่อให้ประสิทธิภาพ / ดีขึ้น”. No source LF edit was made. This is additional wrapping evidence, not four source-authored rows.

| Scale | Approximate body bounds (capture pixels; triangle excluded) | Rows / source LF / extra runtime breaks | Complete / readable / contained / no observed glyph-boundary failure |
|---|---|---|---|
| Medium | (939,674)..(1356,814) | 4 / 2 / 1 | PASS |
| Small | (783,585)..(1129,702) | 4 / 2 / 1 | PASS |
| Large | (1043,732)..(1505,888) | 4 / 2 / 1 | PASS |

Identifying heading and all five preset controls remain visible with each tooltip. White bodies and text fit entirely within the viewport, with visible padding, no clipped final row, border crossing or screen-edge overflow. Small text is readable at returned capture detail; apparent text size increases with UI Scale. No missing-glyph square, isolated combining mark or stranded leading vowel is observed. The short final row “ดีขึ้น” retains its base/vowels/tone mark at this capture detail. Fine native-resolution mark attachment/shaping and dictionary-quality segmentation remain unproven.

The final centered “ดีขึ้น” row leaves substantial unused horizontal width at all scales; this is a shared-width layout tradeoff, not missing content. Its surrounding vertical spacing and the broad fixed body remain visually apparent. No ZWSP, manual newline, font/layout/translation change or new candidate was used to obtain this result.

![Medium actual QualityPresets tooltip](../../local/qa/WO-VISUAL-015/M-QualityPresets.jpg)

![Small actual QualityPresets tooltip](../../local/qa/WO-VISUAL-015/S-QualityPresets.jpg)

![Large actual QualityPresets tooltip](../../local/qa/WO-VISUAL-015/L-QualityPresets.jpg)

## Sequential lifecycle and final verification

Every manager command below ran in its own call with explicit --probe probe-013. Each exit code was 0 and each state was inspected before the next dependent step:

1. python tools/manage_probe.py check --probe probe-013 — original/original/original.
2. Independent manifest/map/staged hashes verified, before install.
3. python tools/manage_probe.py install --probe probe-013 — probe/probe/probe.
4. python tools/manage_probe.py check --probe probe-013 — probe/probe/probe.
5. Launch through Steam in a later call; bounded Medium/Small/Large tests.
6. Return Medium and capture [R-medium.jpg](../../local/qa/WO-VISUAL-015/R-medium.jpg); Settings X, then normal Quit. [90-final-windows.json](../../local/qa/WO-VISUAL-015/90-final-windows.json) confirms no Campus window. No force-close/restart test.
7. python tools/manage_probe.py restore --probe probe-013 — original/original/original.
8. python tools/manage_probe.py check --probe probe-013 — original/original/original.
9. Independent installed/backup/staged and manifest/map SHA-256 verification: [92-final-hashes.json](../../local/qa/WO-VISUAL-015/92-final-hashes.json), all matched. Existing backups retained.

Manifest SHA-256: 459d7e9ebc2db1cc294c25e48996e0fb8fb59054b05682a98bd6d49ea48e0075. Map SHA-256: 81d596fed3d94cfff34b011fdd5c42e46a7127bf9cfd998759920000b9953fda. Both equal pre-install values.

| Bundle | Installed original and retained backup SHA-256 | Unchanged staged probe-013 SHA-256 |
|---|---|---|
| fonts_assets_all.bundle | 33aa34892719fbc7caaabd0a292c32bb135bc61978a4cd3ce73c6c40da8f4e6e | 588f15fad01635da3fb5b86d5c3946cbb7bd85b40304364294fb23d73c207f3e |
| localisation_assets_localisationenglish.bundle | c1e7ca97f260813ccc9a1cf463f20d066631f8e5616bf797fe8d5ae93227878f | 78f4ef1f44bef0425934522c27542e4df767a4f5bad344528dfbe0b0f4ae6624 |
| ui-prefabs-general_assets_all.bundle | 2152e5ba289ccb0414c462371cfdfe05cc7ac589a10a75b8b46d359afd99786d | b8933a120178276ca8246b1494e881ec97a20a7b9b4804b3a16cf080efeb7e14 |

Final state: Medium directly observed before normal Quit; all THREE installed originals and retained backups verified. No persisted-restart claim. No gameplay/save load, graphics value/dropdown/slider changes, Apply, hidden-row enabling, loader/injection, asset/source/map/build edits, branch switch, commit/push, game asset upload or release approval. Existing 17-key acceptance preserved; this report adds one key at three scales for controller review, not all-20 acceptance.
