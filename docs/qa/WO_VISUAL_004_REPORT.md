# WO-VISUAL-004 REPORT

Date: 2026-10-16 (Asia/Bangkok). Target: probe-004. Runtime inspection completed; comparison coverage is scoped below. Evidence directory: `local/qa/WO-VISUAL-004/` (image names below are relative to that directory).

## Execution and environment

Read WO_VISUAL_004.md, diagnostic-map.json, manifest.json, CONTROLLER_ACCEPTANCE.md and PROBE_003_ACCEPTANCE.md before runtime. The diagnostic-map SHA-256 matched the manifest before installation. All manage_probe invocations explicitly used `--probe probe-004`.

Real Windows access used the computer-use skill. Started normally with Steam Play, visited only main-menu Settings, quit normally, then started once more with Steam Play and repeated the representative Controls cases. No gameplay/save was loaded. No language/autosave values, sensitivity sliders, resolution, or Apply were changed. English remained selected. UI Scale started Medium, was inspected at Small and Large, returned to Medium, and remained Medium after restart. Video showed Full Screen Window, 3840 x 2160 @ 60hz. Game version shown: 10.3.169253+2024-12-06.1241.

Captures returned by the Windows tool are 1920 x 1080 for game and approximately 1073 x 771 for Chrome, despite the game resolution above. Saved JPGs are the original screenshot data returned by the tool, without subsequent crop, scaling, or annotation. Tool capture scaling/compression limits precise pixel comparison. Browser custom face evidence showed ProbeThai, weight 500, status loaded, loadCount 1, check=true, verifiedLoaded=true, devicePixelRatio=2, visualViewportScale=1. Browser menu explicitly showed 100% (05-reference-zoom100.jpg). Reference: local/prototype/probe-003/same-font-reference.html. No reference/source files were edited. Chrome's original window disappeared during the session; reopened the same existing reference and inspected its loaded evidence panel again.

## Results

All 12 injected strings were observed in their mapped slots. These are synthetic diagnostic contents, not translations of the Settings functions. PASS below applies only to the injected sequence and visual comparison described; it does not pass the full broader corpus/matrix.

| Case / mapped key suffix | Observed display and layout | Reference comparison | Evidence | Status |
|---|---|---|---|---|
| CRP-VOWEL-02 / CameraPanSensitivity | ปิ ปี ปึ ปื ฝี ฟิ ปั ฟั; all groups visible, no container clipping in scrolled view. Upper marks visible. | Existing reference corpus contains different word combinations (e.g. ปิกนิก ปีนี้ ปีกแผ่น ปั้นโต ฝีมือ ฟิตเนส ปักหมุด ฟันดาบ). Only matching glyph sequences can be compared; it does not supply every injected pair. | 08-controls-unclipped.jpg; 20-ref-vowel02.jpg | PARTIAL; no full shaping PASS |
| CRP-STACK-01 / CameraPitchSensitivity | ที่นี่ ปิ้ง ฟื้น กลิ่น ขี้ ดื่ม; all visible. Tone marks above upper vowels remain distinguishable; no visible collision or clipping. Same result after restart. | Matching sequences in ที่นี่ ปิ้งย่าง ฟื้นฟู กลิ่นหอม ขี้เกียจ ดื่มน้ำ have consistent relative stacking. | 08-controls-unclipped.jpg; 21-ref-desc-stack.jpg; 31-restart-controls.jpg | PASS, injected subset |
| CRP-DESC-01 / CameraRotateSensitivity | ญุ ญู ญฺ ฐุ ฐู ฐฺ; all six visible, lower marks distinguishable. | Exact six-group corpus visible; relative forms consistent. No universal descender-offset rule assumed. | 08-controls-unclipped.jpg; 22-ref-desc-full.jpg; 31-restart-controls.jpg | PASS |
| CRP-DESC-02 / CameraZoomSensitivity | ฎุ ฎู ฎฺ ฏุ ฏู ฏฺ; all six visible after scroll. Initial bottom-edge position is container clipping risk, resolved by scrolling, not a shaping defect. | Exact corpus visible; relative lower-mark forms consistent. | 07-controls-medium.jpg; 08-controls-unclipped.jpg; 22-ref-desc-full.jpg; 31-restart-controls.jpg | PASS |
| CRP-AM-01 / AudioLanuuage | น้ำ ถ้ำ ต้มยำ ลำคลอง; complete visible label, no missing glyph boxes. | Matches corresponding sequences in reference น้ำดื่ม ในถ้ำ … ต้มยำ ลำคลอง. Standard sara am and tone arrangement visually consistent. | 06-game-medium.jpg; 23-ref-am01-stack02-partial.jpg | PASS, injected subset |
| CRP-AM-02 / GameAutosaveFreq | Exact intentionally MALFORMED input นำ้ดื่ม ในถำ้ observed in Game Autosave slot. Marks render in the deliberately supplied sequence; no container clipping. | Reference exact malformed string inspected. This observation is not a spelling/translation failure and does not require auto-normalization. | 06-game-medium.jpg; 24-ref-am02-am03.jpg | OBSERVED diagnostic; normalization not graded |
| CRP-AM-03 / CareerAutosaveFreq | น้ําดื่ม ในถ้ํา observed; separated nikhahit/sara aa representation remains visually distinct from standard case. No clipping. | Exact decomposed reference inspected; broadly consistent arrangement. No claim of canonical equivalence or automatic normalization. | 06-game-medium.jpg; 24-ref-am02-am03.jpg | OBSERVED diagnostic |
| CRP-STACK-02 / Language | พ่อ แม่ ช้า น่า ป้า กู้; all six visible. | Reference image provides first groups but its fixed evidence panel obscures part of the row, including the last matching group. Full-case comparison incomplete. | 06-game-medium.jpg; 23-ref-am01-stack02-partial.jpg | PARTIAL; no full-case PASS |
| CRP-WRAP-01 / Tooltips/Resolution | Full mapped Thai paragraph appears on one line. White body approximately (939,361)-(1751,406), excluding pointer, in 1920x1080 capture. No line break or stranded mark visible. | Reference inspected across 25/26; reference wraps in a different layout. No controlled width comparison. | 10-resolution-tooltip.jpg; 25-ref-wrap01-top.jpg; 26-ref-wrap01-end-wrap02-end.jpg | OBSERVED; runtime wrapping NOT_EXERCISED |
| CRP-WRAP-02 / Tooltips/FullScreenMode | Same underlying paragraph with mapped ZWSP, one line. Body approximately (939,297)-(1751,342). No visible ZWSP boxes/artifacts. | Reference inspected in 26/27. Different placement/container; no dictionary-breaking or production ZWSP approval inferred. | 11-fullscreen-zwsp.jpg; 26-ref-wrap01-end-wrap02-end.jpg; 27-ref-wrap02.jpg | OBSERVED; runtime wrapping NOT_EXERCISED |
| CRP-WRAP-03 / Tooltips/Vsync | Full เมื่อถึงเวลาทุกคนต้องเดินทางไปเรียนที่โรงอาหารและเตรียมตัวเข้าห้องเรียนวิชาเคมี on one line. Body approximately (939,485)-(1510,530). No stranded leading vowel or combining mark at a line boundary (there is no boundary). | Same reference paragraph inspected; browser wraps into two lines. | 12-vsync-tooltip.jpg; 28-ref-wrap03.jpg | OBSERVED; runtime wrapping NOT_EXERCISED |
| CRP-MIX-01 / Tooltips/AntialiasingMode | อัปเกรด Campus Hub สู่ Level 10 เพื่อเปิดหลักสูตรใหม่สำหรับ Staff และ Student complete on one line; Thai, Latin, digits display without missing boxes. Body approximately (939,829)-(1516,869). | Same mixed text inspected; relative mark placement legible. This does not identify the engine's actual fallback face. | 13-mixed-tooltip.jpg; 29-ref-mixed.jpg | PASS for visible injected text; fallback mechanism unverified |

Tooltips activated by pointer placement using zero-delta scroll and waiting, without clicking their controls. Bounds are approximate from visual inspection of returned captures, not native 4K bounds.

Small and Large: Game labels and Controls groups remain visible in 15-game-small.jpg, 16-controls-small.jpg, 17-game-large.jpg, 18-controls-large.jpg. Large Controls required scrolling to bring bottom case clear of panel edge. These are supplementary layout observations, not separately exhaustive same-font comparisons at each scale. 14-scale-dropdown.jpg shows open values Small/Medium/Large; 19-medium-restored.jpg and 30-restart-game-medium.jpg show closed Medium. Other closed dropdown values (English, Every Month, Every Change, video values) remained legible. No language/autosave dropdown selection was made.

Restart result: 30-restart-game-medium.jpg and 31-restart-controls.jpg repeat valid stacked/lower-mark cases without a visible change. Persistent caches were not cleared; restart does not prove cache clearing. Atlas stress, tokens/plurals, parser semantics, uninjected matrix cases, and corpus beyond matching subsets remain NOT_RUN. No valid mark collision was established by these captures. Partial reference coverage must not be promoted to PASS.

## Integrity and restoration

Manifest and build report SHA-256: d720c0470d56f9cc35222b5584f90135cd9293cdfc747a7c2da7ce69c3073dd5.
Diagnostic map SHA-256: bc9811ce02e749a9eafa3a469149f79d7984e2d1037855da6a6abfe1f037535f (matches manifest).

| Bundle | Staged probe SHA-256 | Final installed and retained backup SHA-256 |
|---|---|---|
| fonts_assets_all.bundle | 588f15fad01635da3fb5b86d5c3946cbb7bd85b40304364294fb23d73c207f3e | 33aa34892719fbc7caaabd0a292c32bb135bc61978a4cd3ce73c6c40da8f4e6e |
| localisation_assets_localisationenglish.bundle | 837fdfd9bccc3b5d998df23414353ff198d6d28097218091815b6737a1b3a0d7 | c1e7ca97f260813ccc9a1cf463f20d066631f8e5616bf797fe8d5ae93227878f |

Preflight check: original/original. Initial sandbox install attempt stopped at tasklist before writes; rerun with permitted elevated execution succeeded (probe/probe). Installed check confirmed probe/probe. Final normal Quit followed by guarded restore succeeded original/original, and independent final check confirmed original/original. Backups retained. Exact path/hash records: 34-hashes.json. Outputs: 01-preflight.txt, 02-install.txt, 03-installed-check.txt, 32-restore.txt, 33-final-check.txt. The initial 02-install.txt was empty because the failed attempt wrote stderr; successful elevated install output is transcribed in 35-command-notes.txt.

No code, translation, diagnostic map, or staged build edits during testing. Only authorized temporary bundle installation/restoration and evidence/report creation. No commit/push or uploads.
