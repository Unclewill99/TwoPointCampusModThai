# WO-VISUAL-013 REPORT

Date: 2026-10-17 (Asia/Bangkok). **Five primary tooltips observed complete/readable at Small, Medium and Large; Medium restart recheck completed. Final restoration PASS, all THREE original.** Six additional Medium tooltips inspected; remaining coverage explicitly NOT_RUN below. Scoped visual results only: no release, glossary, fixed-width, dictionary or production ZWSP approval.

## Inputs and actual environment

Read WO_VISUAL_013.md, reports/probe-013-build.json, local/prototype/probe-013/manifest.json and tooltip-map.json. Map SHA-256 verified against manifest before install: `81d596fed3d94cfff34b011fdd5c42e46a7127bf9cfd998759920000b9953fda`. Manifest SHA-256: `459d7e9ebc2db1cc294c25e48996e0fb8fb59054b05682a98bd6d49ea48e0075` (00-input-hashes.json, 00-map-verified.txt). Supplied candidate contains 50 pilot r3 records and 20 actual tooltip r2 records; no synthetic body or ZWSP. No translation/code/map edits during test.

Windows desktop; Steam visible Play button used for both initial launch and one restart. Build 10.3.169253+2024-12-06.1241 (04-menu.jpg). Language remained English; actual UI Scale verified in 05-medium-setting.jpg, S-setting.jpg, L-setting.jpg and R-medium-setting.jpg. Full Screen Window, unchanged 3840 x 2160 @ 60hz verified in 06-medium-video.jpg, S-Resolution.jpg, L-video.jpg and R-video.jpg. VSync On, Framerate Limit Unlimited and Antialiasing SMAA unchanged. Only UI Scale changed: Medium -> Small -> Large -> Medium. No Apply, graphics selection/change, gameplay/save load or force-close.

Used computer-use skill and inspected original returned 1920 x 1080 JPG screenshots, saved without cropping/rescaling/annotation under local/qa/WO-VISUAL-013/. Capture size is not render-resolution proof; no native-resolution capture option was exposed. Fine mark placement at native resolution is outside coverage. Coordinates/bounds below are approximate capture pixels, excluding left pointer; not Unity/native units.

## Primary per-key/per-scale matrix

All key suffixes below have exact prefix `UI/Settings/Tooltips/`. `Vsync` is the map's exact casing. Each image includes the identifying visible control. C=all source text segments visibly accounted for, R=readable, E=box contained on-screen, G=no observed missing glyph or stranded base/mark at line boundary. PASS here means C/R/E/G in that inspected image only.

| Exact key suffix | Small image / rows / result | Medium image / rows / result | Large image / rows / result | Source LF / additional breaks at S,M,L |
|---|---|---|---|---|
| Resolution | S-Resolution.jpg / 3 / PASS | M-Resolution.jpg / 3 / PASS | L-Resolution.jpg / 3 / PASS | 2 LF / 0,0,0 |
| FullScreenMode | S-FullScreenMode.jpg / 1 / PASS | M-FullScreenMode.jpg / 1 / PASS | L-FullScreenMode.jpg / 1 / PASS | 0 LF / 0,0,0 |
| MaxFPS | S-MaxFPS.jpg / 3 / PASS | M-MaxFPS.jpg / 3 / PASS | L-MaxFPS.jpg / 3 / PASS | 2 LF / 0,0,0 |
| AntialiasingMode | S-AntialiasingMode.jpg / 4 / PASS | M-AntialiasingMode.jpg / 4 / PASS | L-AntialiasingMode.jpg / 4 / PASS | 3 LF / 0,0,0 |
| Vsync | S-Vsync.jpg / 2 / PASS | M-Vsync.jpg / 2 / PASS | L-Vsync.jpg / 2 / PASS | 1 LF / 0,0,0 |

### Measured visible body bounds

| Key | Small (x1,y1)-(x2,y2) | Medium | Large |
|---|---|---|---|
| Resolution | (783,300)-(1128,389) | (939,330)-(1355,437) | (1043,350)-(1505,470) |
| FullScreenMode | (783,274)-(1128,309) | (939,299)-(1355,340) | (1043,315)-(1505,361) |
| MaxFPS | (783,456)-(1128,545) | (939,518)-(1355,625) | (1043,559)-(1505,678) |
| AntialiasingMode | (783,239)-(1128,349) | (939,783)-(1355,915) | (1043,714)-(1505,861) |
| Vsync | (783,418)-(1128,476) | (939,472)-(1355,542) | (1043,508)-(1505,586) |

Widths approximately 345/416/462 capture pixels for Small/Medium/Large, respectively. Apparent glyph scale increases with UI Scale; Small is smaller but remains readable in returned captures. No native point-size equality claim. Antialiasing Small was captured while Video retained its lower scroll position; Large required scrolling to expose that control. Bounds/vertical placement therefore reflect actual scroll state, not a pure position-only scale comparison.

All primary bodies and text remain inside the viewport, with visible side/top/bottom padding. No blank tooltip, text crossing white box borders, clipped last row or screen-edge overlap. FullScreenMode's short centered single line leaves substantial horizontal empty space in the experimental fixed-width body at all scales; readable but inefficient use of width, recorded as shared-width behavior rather than a blankness failure. Other primary bodies have modest padding/gaps. Tooltip triangles sit next to controls; closed selected values remain readable and are not covered by tooltip bodies.

### Actual primary rows and source accounting

Rows below were visible identically at all three scales. Every displayed row matches one original LF-delimited segment; multiline appearance in these five keys is **not evidence of additional wrapping**.

Resolution:

```text
กำหนดความละเอียดการแสดงผลของเกม
ความละเอียดที่สูงขึ้นทำให้ทั้งเกมดูคมชัดขึ้น
ลดความละเอียดเพื่อเพิ่มประสิทธิภาพ CPU และกราฟิก
```

FullScreenMode:

```text
เลือกโหมดการแสดงผล
```

MaxFPS (visible label Framerate Limit):

```text
จำกัดเฟรมเรตสูงสุดที่เกมจะทำงานได้
ลดค่านี้หากเครื่องร้อนหรือเสียงดังเกินไป
ไม่ทำงานร่วมกับ VSync
```

AntialiasingMode:

```text
เปิด Anti-Aliasing เพื่อลดรอยหยักตามขอบภาพ
SMAA คุณภาพสูงกว่า FXAA
SMAA ทำงานช้ากว่า FXAA ด้วย
ปิดเพื่อเพิ่มประสิทธิภาพกราฟิก
```

Vsync (visible label VSync):

```text
ซิงก์เฟรมเรตของเกมให้ตรงกับรีเฟรชเรตของจอภาพ
ลดภาพฉีก แต่อาจเพิ่มความหน่วงของอินพุต
```

All first/last phrases and middle segments accounted for. No problematic boundary to transcribe in this primary set: no line ends with stranded เ/แ/โ/ใ/ไ before its consonant, and no next line begins with isolated combining vowel/tone mark. No observed missing-glyph square, raw colour tag or literal variable token. Fine glyph attachment quality remains limited by compressed capture detail. Wording is provisionally consistent with visible English labels: Resolution describes resolution, Fullscreen Mode display mode, Framerate Limit a maximum rate, Antialiasing Mode edge smoothing, and VSync sync/tearing/latency. This is not glossary approval or validation of MaxFPS/VSync functional claims.

## Additional Medium observations and coverage limits

Additional keys share the same exact prefix. These were activated safely by hover while scrolling Video, with no value changes. All inspected bodies fit on screen, show complete source content and readable glyphs; no observed mark split/missing glyph/raw token/colour-tag text. Bounds all have x approximately 939..1355. Extra breaks are runtime breaks, separate from source LF.

| Key suffix | Evidence | Rows / source LF / extra breaks | Approximate y bounds | Actual extra boundary |
|---|---|---|---|---|
| MSAASamples | M-MSAASamples.jpg | 2 / 0 / 1 | 807..881 | รอยหยัก / หรือลดจำนวนลงเพื่อเพิ่มประสิทธิภาพกราฟิก |
| AntialiasingQuality | M-AntialiasingQuality.jpg | 2 / 1 / 0 | 741..819 | None; trailing source space not visually distinguishable |
| DepthOfField | M-DepthOfField.jpg | 3 / 1 / 1 | 786..893 | เปิด Depth of Field / ซึ่งจะทำให้ส่วนใกล้และส่วนไกลของฉากเบลอเล็กน้อย |
| AmbientOcclusionMode | M-AmbientOcclusionMode.jpg | 5 / 3 / 1 | 567..728 | เปิด Ambient Occlusion / เพื่อเพิ่มคุณภาพของแสงในมุมมืด |
| AmbientOcclusionModeQuality | M-AmbientOcclusionModeQuality.jpg | 4 / 2 / 1 | 645..778 | คุณภาพระดับต่ำทำให้ภาพดูดีไม่เท่า / แต่จะช่วยเพิ่มประสิทธิภาพ |
| CharacterDrawDistance | M-CharacterDrawDistance.jpg | 4 / 2 / 1 | 734..879 | ระยะแสดงผลที่สูงขึ้นทำให้ตัวละครยังอยู่ในมุมมองได้ในระยะ / ไกลขึ้น |

Actual complete additional rows are preserved in 93-observed-rows.json and programmatically accounted against map segments (ignoring source line breaks/whitespace only for accounting; original LF counts retained separately). Observed extra boundaries above do not strand a leading vowel or combining mark; `ไกลขึ้น` keeps ไ with ก. No word/mark quality conclusion beyond these cases. Shared-width effect can introduce large gaps between centered segments; the short `ไกลขึ้น` row is conspicuously short but not missing content.

Other map records were NOT_RUN, never inferred PASS from source presence:

| Key suffix | Medium | Small/Large | Reason |
|---|---|---|---|
| AnimationSkinningQuality | NOT_RUN | NOT_RUN | No such control naturally exposed during this main-menu pass |
| CharacterLimits | NOT_RUN | NOT_RUN | Not naturally exposed; no limits toggled or variables supplied; substitution/colour rendering untested |
| RenderScale | NOT_RUN | NOT_RUN | No such control naturally exposed |
| QualityPresets | NOT_RUN | NOT_RUN | Buttons/header visible; no tooltip activation recorded; not chased |
| AnisoTextures | NOT_RUN | NOT_RUN | Anisotropic Filtering control visible, tooltip not activated in this scoped pass |
| Bloom | NOT_RUN | NOT_RUN | Control visible, tooltip not activated in this scoped pass |
| ShadowQuality | NOT_RUN | NOT_RUN | Control visible, tooltip not activated in this scoped pass |
| TextureQuality | NOT_RUN | NOT_RUN | Control visible, tooltip not activated in this scoped pass |
| WorldDetail | NOT_RUN | NOT_RUN | Control visible, tooltip not activated in this scoped pass |

All six additional keys above are NOT_RUN at Small/Large; only the five primary keys were required/repeated at those scales. No claim of all-20 coverage or token substitution success.

## Dropdowns, Medium return and restart

UI Scale dropdown opened/selected Small, Large, then Medium. Closed selected scale values visible in S-setting.jpg, L-setting.jpg, R-medium-before-quit.jpg. At initial Large selection, UI Scale sat partly behind the bottom viewport/button region until a normal scroll revealed it fully; L-setting.jpg records the fully visible closed Large value. This is scroll/viewport coverage, not a claim that every offscreen row is always visible.

Closed graphics values stayed readable when their rows were exposed: Full Screen Window, 3840 x 2160 @ 60hz, On, SMAA; Unlimited slider label also visible. Evidence in each primary image and 06-medium-video.jpg/L-video.jpg/R-video.jpg. Graphics dropdown menus were not opened/selected, so expanded graphics-option-list layout is NOT_RUN. UI Scale's actual three-option list was visibly readable during navigation. No graphics setting changed and no Apply used.

Returned Medium before first normal Quit (R-medium-before-quit.jpg). Fresh window inventory showed Campus absent; Steam Play launched it again. R-medium-setting.jpg confirms persisted Medium and English after restart. R-video.jpg confirms same resolution/mode/closed values. Resolution and Antialiasing rechecked: R-Resolution.jpg (3 rows, bounds approximately 939,330..1355,437) and R-AntialiasingMode.jpg (4 rows, approximately 939,783..1355,915); both complete/readable, same LF-only segmentation and no visible clipping/mark failure as initial Medium. No persistent-cache-clearing claim. Final exit normal through Settings X > Quit, leaving UI Scale Medium.

## Sequential lifecycle and restoration

All manager commands ran in separate inspected calls with exact `--probe probe-013`; each exited 0 and returned expected states for ALL THREE:

1. `python tools/manage_probe.py check --probe probe-013`: all original (01-original.txt).
2. `python tools/manage_probe.py install --probe probe-013`: all probe (02-install.txt).
3. `python tools/manage_probe.py check --probe probe-013`: all probe (03-installed.txt). Manager validates staged/installed hashes and original backups. Only after this success did Steam launch in later calls.
4. Scale pass, normal Quit/restart at Medium, two rechecks, normal Quit, fresh inventory confirmed no Campus window.
5. `python tools/manage_probe.py restore --probe probe-013`: all original (90-restore.txt).
6. `python tools/manage_probe.py check --probe probe-013`: all original (91-final-original.txt).

Independent SHA-256 verification after restoration (92-final-hashes.json) confirms actual installed files AND retained backups match original for all THREE; staged candidates still match manifest:

| Bundle | Installed original AND retained backup SHA-256 | Staged probe-013 SHA-256 |
|---|---|---|
| fonts_assets_all.bundle | 33aa34892719fbc7caaabd0a292c32bb135bc61978a4cd3ce73c6c40da8f4e6e | 588f15fad01635da3fb5b86d5c3946cbb7bd85b40304364294fb23d73c207f3e |
| localisation_assets_localisationenglish.bundle | c1e7ca97f260813ccc9a1cf463f20d066631f8e5616bf797fe8d5ae93227878f | 78f4ef1f44bef0425934522c27542e4df767a4f5bad344528dfbe0b0f4ae6624 |
| ui-prefabs-general_assets_all.bundle | 2152e5ba289ccb0414c462371cfdfe05cc7ac589a10a75b8b46d359afd99786d | b8933a120178276ca8246b1494e881ec97a20a7b9b4804b3a16cf080efeb7e14 |

Final **original/original/original**, backups retained, UI Scale Medium. No branch switch, commit/push, translation edit, loader installation or asset upload. Main requested visual coverage completed; explicitly listed NOT_RUN areas remain ungraded.
