# WO-VISUAL-016 REPORT

Date: 2026-10-18 (Asia/Bangkok). **Bounded Medium diagnostic completed. Five readable rows, all 237 codepoints / three exact repeats accounted for. Four runtime cuts observed; internal word/syllable splits recorded. No observed leading-vowel/base or combining-mark/base detachment at those four edges at available capture detail.** This is not full Thai/adversarial PASS, dictionary support, translation acceptance or native-shaping certification. Final Medium and all THREE original verified.

## Candidate and preflight

Read WO_VISUAL_016.md, LINE_BOUNDARY_FOLLOWUP.md, PROBE_013_MILESTONE.md, WO_VISUAL_012_REPORT.md and probe-016 manifest/diagnostic-map. Current Computer Use skill, API/guidance/confirmations had already been read in this conversation. Candidate is **probe-016**, the new synthetic CRP-WRAP-03 diagnostic in UI/Settings/Tooltips/Resolution; not probe-013 or an actual translated Resolution description. Only this one synthetic tooltip was observed. No actual-tooltip regression matrix or A/B test was performed.

Input paragraph (unchanged, 79 Unicode codepoints):

~~~text
เมื่อถึงเวลาทุกคนต้องเดินทางไปเรียนที่โรงอาหารและเตรียมตัวเข้าห้องเรียนวิชาเคมี
~~~

Three exact copies concatenated without separators total 237 codepoints. No whitespace, LF, ZWSP or tags. The paragraph contains เ, แ, โ and ไ, but no ใ; target occurrence within a row is not edge coverage.

Fresh Windows inventory showed Campus absent: [00-windows.json](../../local/qa/WO-VISUAL-016/00-windows.json). Selected the unique returned Steam window, activated it and visually inspected a correct Steam image. Documented sky.scroll coordinate input with zero horizontal/vertical deltas placed the pointer at (580,610) without clicking or scrolling. Evidence: [00-steam.jpg](../../local/qa/WO-VISUAL-016/00-steam.jpg), [00-pointer-placement.jpg](../../local/qa/WO-VISUAL-016/00-pointer-placement.jpg). Thus current capture and non-mutating placement were verified before install; no wrong-target capture or undocumented input workaround was used.

Original check passed for all THREE. Independent [01-input-hashes.json](../../local/qa/WO-VISUAL-016/01-input-hashes.json) verifies manifest/map/staged identity and actual font/UI hash equality with staged probe-013. Font and UI byte identities were retained; nothing was rebuilt. Manifest SHA-256: 7f83ea9073b7088bc3a22872efe87214eb9f29982a1f67c20d0ac85215fcc5a5; diagnostic-map SHA-256: e07ead50715dd447e24f69ecfce2209c8e26f479b217f0a8f07bac9055a9d7e3. Staged localisation SHA-256: 280fc29c6df482cf0cf32f4331317b94f901b56958866a68f9e56de84978f065. Paragraph SHA-256 from map: 1af9335e1295c5b2e3503d7bf6199fb133460dd27ab81809c7f9d6f8f5208fe3.

## Actual environment and acquisition

Build 10.3.169253+2024-12-06.1241: [03-menu-build.jpg](../../local/qa/WO-VISUAL-016/03-menu-build.jpg). English and initial UI Scale Medium: [04-medium-english.jpg](../../local/qa/WO-VISUAL-016/04-medium-english.jpg). Full Screen Window, 3840 x 2160 @ 60hz, VSync On and Framerate Limit Unlimited: [05-resolution-target.jpg](../../local/qa/WO-VISUAL-016/05-resolution-target.jpg). No graphics values changed; capture dimensions do not establish render resolution.

After separate successful install and installed check, launch through the returned Steam game app identifier occurred in a later call. launch_app initially reported no targetable window while starting; fresh inventory then found exactly one Campus window, rehydrated/activated it and verified the actual game image before input: [02-game-windows.json](../../local/qa/WO-VISUAL-016/02-game-windows.json). Main-menu Settings > Video only.

Derived hover point (109,383) from the fresh correct [05-resolution-target.jpg](../../local/qa/WO-VISUAL-016/05-resolution-target.jpg): on the Resolution LABEL, far from its dropdown. Used documented coordinate placement with scrollX=0, scrollY=0, held still for an explicit 1800 ms, then took one unobscured capture: [06-resolution-paragraph.jpg](../../local/qa/WO-VISUAL-016/06-resolution-paragraph.jpg). The tooltip was fully visible; no additional attempt/capture or force-wrapping setting change was needed.

Original returned 1920 x 1080 image bytes were saved without crop, resize, sharpening, annotation or re-encoding. The original compressed capture supports readable row transcription but cannot certify fine native-resolution mark attachment/placement. No enlarged image is offered as higher-detail evidence.

## Exact observed rows and literal completeness

~~~text
เมื่อถึงเวลาทุกคนต้องเดินทางไปเรียนที่โรงอาหารและเตรียม
ตัวเข้าห้องเรียนวิชาเคมีเมื่อถึงเวลาทุกคนต้องเดินทางไปเรีย
นที่โรงอาหารและเตรียมตัวเข้าห้องเรียนวิชาเคมีเมื่อถึงเวลาทุ
กคนต้องเดินทางไปเรียนที่โรงอาหารและเตรียมตัวเข้าห้องเรี
ยนวิชาเคมี
~~~

[93-row-boundary-accounting.json](../../local/qa/WO-VISUAL-016/93-row-boundary-accounting.json) preserves these raw rows, per-row lengths and every edge. Exact automated comparison: rawObservedRows.join("") === diagnosticMap.text returned true. **Normalization: NONE.** No whitespace removal, Unicode normalization, mark stripping or spelling repair. Row lengths in Unicode codepoints are 55, 58, 59, 55 and 10; total 237. Counting uses Array.from(string), not UTF-16 length or glyph count.

First text begins เมื่อถึงเวลาทุกคน; final row is exactly ยนวิชาเคมี, ending เคมี. Literal equality accounts for all three entire map paragraphs. Synthetic joins at 79 and 158 occur inside rows 2 and 3 respectively, not at visual boundaries. There is no LF in source: all four displayed breaks are runtime breaks. No text remains unaccounted for at readable capture detail. Literal accounting is not independent proof of subpixel mark fidelity.

## Every observed edge

Offset means number of original Unicode codepoints before the break, a zero-based string cut offset. Paragraph indices below are one-based, local cut offsets are codepoint counts within that paragraph. Context is transcribed/cross-checked literally, with slash marking the actual visual edge.

| After row | Global cut | Paragraph / local cut | Actual local context | Leading vowel separated from following base | Following combining mark detached from preceding base | Linguistic observation |
|---|---:|---|---|---|---|---|
| 1 | 55 | 1 / 55 | เตรียม / ตัว | No observed; cut is not immediately after เ/แ/โ/ใ/ไ | No observed; next codepoint is ต | Break between เตรียม and ตัว inside the broader เตรียมตัว expression; retain for linguistic review. |
| 2 | 113 | 2 / 34 | ไปเรีย / นที่ | No observed; cut is not immediately after เ/แ/โ/ใ/ไ | No observed; next codepoint is น | Internal split เรีย / น within เรียน; segmentation concern. เ and ร and upper ี remain together on the left. |
| 3 | 172 | 3 / 14 | เวลาทุ / กคน | No observed; cut is not immediately after เ/แ/โ/ใ/ไ | No observed; next codepoint is ก | Internal split ทุ / ก within ทุก; segmentation concern. Lower ุ remains with ท on the left. |
| 4 | 227 | 3 / 69 | ห้องเรี / ยนวิชา | No observed; cut is not immediately after เ/แ/โ/ใ/ไ | No observed; next codepoint is ย | Internal split เรี / ยน within เรียน, including an internal vowel/syllable sequence split; segmentation concern. เ, ร and upper ี remain together on the left. |

Nearby original codepoints, with offsets in the complete 237-codepoint source:

| Cut | Four codepoints before / four after |
|---|---|
| 55 | 51: ร U+0E23; 52: ี U+0E35; 53: ย U+0E22; 54: ม U+0E21; **/** 55: ต U+0E15; 56: ั U+0E31; 57: ว U+0E27; 58: เ U+0E40 |
| 113 | 109: เ U+0E40; 110: ร U+0E23; 111: ี U+0E35; 112: ย U+0E22; **/** 113: น U+0E19; 114: ท U+0E17; 115: ี U+0E35; 116: ่ U+0E48 |
| 172 | 168: ล U+0E25; 169: า U+0E32; 170: ท U+0E17; 171: ุ U+0E38; **/** 172: ก U+0E01; 173: ค U+0E04; 174: น U+0E19; 175: ต U+0E15 |
| 227 | 223: ง U+0E07; 224: เ U+0E40; 225: ร U+0E23; 226: ี U+0E35; **/** 227: ย U+0E22; 228: น U+0E19; 229: ว U+0E27; 230: ิ U+0E34 |

All four cuts are inside individual paragraph copies, not synthetic joins at 79/158. Their local offsets (55,34,14,69) are four different contexts. The two cuts through เรียน occur at different positions (เรีย / น versus เรี / ยน), not duplicate same-context evidence. Repetition alone is not three independent corpus samples.

At cut 55, final ม and next ต do not separate a combining mark; next ั stays with ต within row 2. At cut 113, เ+ร+ี+ย stay on row 2 and น begins row 3. At cut 172, ท+ุ stay on row 3 and ก begins row 4. At cut 227, เ+ร+ี stay on row 4 and ย begins row 5. These observations support only no visible base/combining-mark detachment at these exact edges. They do not make เรี / ยน a valid syllable/word boundary: that internal sequence split is explicitly retained as a segmentation concern.

No cut immediately follows a leading-vowel codepoint or begins with a combining mark; thus this sample did not force the most direct leading-vowel/base or base/mark edge cases. Presence of แ/โ/ไ elsewhere within rows is NOT targeted edge coverage; ใ is absent. Fine native mark positioning at each edge remains UNRESOLVED at this capture resolution even though readable codepoint/row accounting is resolved. No dictionary, five-vowel, all-cluster or full-adversarial claim.

## Visible layout

Five ink rows. Approximate white body bounds (939,297)..(1356,470), turquoise edge near x=936; text bounds approximately x=947..1345, y=310..453 in capture pixels. All white-box edges and final row are visible, text contained with padding; no clipped edge/last row, missing-glyph square, blank body or border overlap observed. Identifying Resolution control and unchanged value remain visible.

The first four rows span much of the bounded width; final ยนวิชาเคมี is short and centered, leaving broad unused horizontal space. Vertical gaps vary visibly between rows; these are runtime layout, not source LF. Readable/completeness/containment observation succeeds for this sample, while internal word/syllable segmentation concerns remain. Native font size and fine shaping quality are not measured.

![Original Medium synthetic paragraph capture](../../local/qa/WO-VISUAL-016/06-resolution-paragraph.jpg)

## Sequential lifecycle and restoration

Each manager command ran separately with --probe probe-016, exit 0, and all THREE states were inspected before continuing:

1. python tools/manage_probe.py check --probe probe-016 — original/original/original.
2. Independent manifest/map/staged check, with font/UI equality to probe-013.
3. python tools/manage_probe.py install --probe probe-016 — probe/probe/probe.
4. python tools/manage_probe.py check --probe probe-016 — probe/probe/probe.
5. Later Steam launch; fresh game selection/capture; Medium-only observation.
6. Medium remained unchanged throughout; direct final capture [07-final-medium.jpg](../../local/qa/WO-VISUAL-016/07-final-medium.jpg). Settings X then normal Quit. [90-after-quit.json](../../local/qa/WO-VISUAL-016/90-after-quit.json) confirms Campus absent. No force-close or restart test.
7. python tools/manage_probe.py restore --probe probe-016 — original/original/original.
8. python tools/manage_probe.py check --probe probe-016 — original/original/original.
9. Independent [92-final-hashes.json](../../local/qa/WO-VISUAL-016/92-final-hashes.json) verifies all THREE installed originals, retained probe-016 backups, staged files, manifest/map. All match, and manifest/map equal the pre-install values. Existing backups kept.

| Bundle | Installed original AND retained backup SHA-256 | Unchanged staged probe-016 SHA-256 |
|---|---|---|
| fonts_assets_all.bundle | 33aa34892719fbc7caaabd0a292c32bb135bc61978a4cd3ce73c6c40da8f4e6e | 588f15fad01635da3fb5b86d5c3946cbb7bd85b40304364294fb23d73c207f3e |
| localisation_assets_localisationenglish.bundle | c1e7ca97f260813ccc9a1cf463f20d066631f8e5616bf797fe8d5ae93227878f | 280fc29c6df482cf0cf32f4331317b94f901b56958866a68f9e56de84978f065 |
| ui-prefabs-general_assets_all.bundle | 2152e5ba289ccb0414c462371cfdfe05cc7ac589a10a75b8b46d359afd99786d | b8933a120178276ca8246b1494e881ec97a20a7b9b4804b3a16cf080efeb7e14 |

Final Medium directly observed before normal Quit; all THREE originals restored/hash verified. No graphics value, UI Scale, resolution or save-state change, gameplay/save load, Small/Large/restart matrix, actual-tooltip repeat, hidden-row activation, high-detail VOWEL-02 grading, loader/injection, font/layout rebuild, ZWSP experiment, branch switch, commit/push or asset upload. No A/B improvement, new actual-tooltip acceptance or release approval is claimed.
