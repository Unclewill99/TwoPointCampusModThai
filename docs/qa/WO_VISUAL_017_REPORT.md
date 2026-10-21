# WO-VISUAL-017 REPORT

Date: 2026-10-18 (Asia/Bangkok). **OBSERVED EXPERIMENTAL BENEFIT for B in this paragraph/container at Medium.** All 237 underlying codepoints / three repeats are preserved in five readable rows. B cuts at 49,100,154,207; A's internal เรีย / น, ทุ / ก and เรี / ยน splits are absent, with no new bad edge observed. No visible U+200B artifact, clipping or apparent font-size/width regression. Final Medium and all THREE originals verified. No production ZWSP, dictionary, universal Thai wrapping or release approval.

## Independent proposal review before installation

Read WO_VISUAL_017.md, THAI_LINEBREAKING_FINDINGS.md, PROBE_016_DISPOSITION.md, BUG_THAI_002.md, WO_VISUAL_016_REPORT.md and probe-017 manifest/map. Reviewed the proposed per-paragraph units independently before installation:

เมื่อ | ถึง | เวลา | ทุกคน | ต้อง | เดินทาง | ไป | เรียน | ที่ | โรงอาหาร | และ | เตรียมตัว | เข้า | ห้องเรียน | วิชา | เคมี

No clearly invalid opportunity was found for this sentence. Each is a natural Thai unit in context; ทุกคน, เดินทาง, โรงอาหาร, เตรียมตัว and ห้องเรียน remain intact. Boundaries such as ไป / เรียน, ที่ / โรงอาหาร and วิชา / เคมี are plausible opportunities without cutting a word's letters or base/mark cluster. Keeping compound expressions together is a conservative experimental choice, not proof that these are the only acceptable linguistic units. No objection requiring stop-before-install, no silent revision, no tokenizer/dictionary approval. Proposed opportunities and actual runtime edges are assessed separately below.

## Capability, identity and environment

Current Computer Use skill/API/guidance/confirmations were already read in this conversation. A fresh JavaScript session required reinitialization; the initial uninitialized variable attempt stopped without app input. Fresh Windows inventory showed no Campus or Steam window. Launched the returned installed Steam app, then refreshed inventory, selected its unique returned window, activated it and inspected actual Steam content. Documented coordinate-based sky.scroll with zero deltas moved the pointer to (580,610), without click/scroll: [00-steam.jpg](../../local/qa/WO-VISUAL-017/00-steam.jpg), [00-pointer-placement.jpg](../../local/qa/WO-VISUAL-017/00-pointer-placement.jpg). Capture and supported non-mutating placement were established before installation. Launcher no-window messages during startup were followed by fresh selection/correct capture, never blind input.

Pre-install check: original/original/original. [01-input-verification.json](../../local/qa/WO-VISUAL-017/01-input-verification.json) independently verifies B manifest/map/staged hashes and frozen A manifest/map/staged files. B text minus ONLY U+200B equals A text literally, also equals diagnosticMap.underlying_text; font/UI bytes equal A. B has 47 mapped U+200B opportunities, no LF, unchanged underlying 237 codepoints. No build or asset/source/map edit during test.

| Identity | SHA-256 |
|---|---|
| B manifest | 59741713bbe3b2c6ca19c0568a16fa0695aae8e2214f62f14e2a088a462cf0e1 |
| B diagnostic map | b6177358db0a28b98076837e7e3e547c54d623dcaae526c5b0ea3ced8204dbf3 |
| Frozen A manifest | 7f83ea9073b7088bc3a22872efe87214eb9f29982a1f67c20d0ac85215fcc5a5 |
| Frozen A diagnostic map | e07ead50715dd447e24f69ecfce2209c8e26f479b217f0a8f07bac9055a9d7e3 |

Actual build 10.3.169253+2024-12-06.1241: [03-menu-build.jpg](../../local/qa/WO-VISUAL-017/03-menu-build.jpg). English / initial Medium: [04-medium-english.jpg](../../local/qa/WO-VISUAL-017/04-medium-english.jpg). Full Screen Window / unchanged 3840 x 2160 @60hz: [05-resolution-target.jpg](../../local/qa/WO-VISUAL-017/05-resolution-target.jpg). These match historical A's reported environment, so no build/resolution mismatch limitation is triggered. VSync On and Unlimited remained unchanged. Menu background differs, which does not obscure the opaque tooltip or change its measured bounds.

Only B ran; no A rerun. After successful separate install/check calls, launched through returned Steam game identifier in a later call. Fresh inventory found one Campus window, selected/activated it and verified a correct game capture before input. Main-menu Settings > Video only. Hovered Resolution LABEL at fresh-capture-derived (109,383), far from dropdown, using supported zero-delta placement. Held 1800 ms then took one fully appeared capture: [06-B-resolution.jpg](../../local/qa/WO-VISUAL-017/06-B-resolution.jpg). No recovery capture, prolonged chase or extra control test.

All images preserve original returned 1920x1080 compressed image bytes, without resize, sharpening, crop or annotation. Capture dimensions are not render-resolution evidence; fine native mark positioning remains unresolved.

## Exact B rows and literal accounting

~~~text
เมื่อถึงเวลาทุกคนต้องเดินทางไปเรียนที่โรงอาหารและ
เตรียมตัวเข้าห้องเรียนวิชาเคมีเมื่อถึงเวลาทุกคนต้อง
เดินทางไปเรียนที่โรงอาหารและเตรียมตัวเข้าห้องเรียนวิชา
เคมีเมื่อถึงเวลาทุกคนต้องเดินทางไปเรียนที่โรงอาหารและ
เตรียมตัวเข้าห้องเรียนวิชาเคมี
~~~

[93-rows-edges.json](../../local/qa/WO-VISUAL-017/93-rows-edges.json) preserves original transcribed rows, lengths and complete edge data. Row concatenation equals diagnosticMap.underlying_text and A text literally. Normalization **NONE**, except U+200B is omitted from B for the underlying comparison. No spaces/marks stripped, no Unicode normalization or spelling repair. Row lengths: 49/51/54/53/30, sum 237. First row begins เมื่อถึงเวลาทุกคน; final row exactly เตรียมตัวเข้าห้องเรียนวิชาเคมี. All three repeats accounted for.

Invisible U+200B positions cannot be located visually within a row; none is invented here. The cut offsets below count underlying Unicode codepoints using Array.from(), not UTF-16 units/glyphs. All four are runtime cuts, source LF count zero. Synthetic paragraph joins at 79 and 158 remain inside rows 2 and 4, respectively.

## Every actual B edge, independently graded

| After row | Underlying cut | Paragraph / local cut | Actual context | In proposed cut list | Actual boundary assessment |
|---|---:|---|---|---|---|
| 1 | 49 | 1 / 49 | และ / เตรียมตัว | Yes | Natural unit boundary here; no observed internal word/syllable cut or base/mark detachment |
| 2 | 100 | 2 / 21 | ต้อง / เดินทาง | Yes | Natural unit boundary here; no observed internal word/syllable cut or base/mark detachment |
| 3 | 154 | 2 / 75 | วิชา / เคมี | Yes | Natural unit boundary here; no observed internal word/syllable cut or base/mark detachment |
| 4 | 207 | 3 / 49 | และ / เตรียมตัว | Yes | Natural unit boundary here; no observed internal word/syllable cut or base/mark detachment |

Paragraph numbers are one-based; cut offsets count codepoints before the break. None is a synthetic join. Cuts 49 and 207 are the same paragraph-local context (49), so four edges provide **three distinct contexts**, not four independent cases.

| Cut | Four codepoints before / four after, original underlying offsets |
|---|---|
| 49 | 45: ร U+0E23; 46: แ U+0E41; 47: ล U+0E25; 48: ะ U+0E30; **/** 49: เ U+0E40; 50: ต U+0E15; 51: ร U+0E23; 52: ี U+0E35 |
| 100 | 96: ต U+0E15; 97: ้ U+0E49; 98: อ U+0E2D; 99: ง U+0E07; **/** 100: เ U+0E40; 101: ด U+0E14; 102: ิ U+0E34; 103: น U+0E19 |
| 154 | 150: ว U+0E27; 151: ิ U+0E34; 152: ช U+0E0A; 153: า U+0E32; **/** 154: เ U+0E40; 155: ค U+0E04; 156: ม U+0E21; 157: ี U+0E35 |
| 207 | 203: ร U+0E23; 204: แ U+0E41; 205: ล U+0E25; 206: ะ U+0E30; **/** 207: เ U+0E40; 208: ต U+0E15; 209: ร U+0E23; 210: ี U+0E35 |

Each row after a cut starts with เ followed by its base on the same row: เตรียมตัว, เดินทาง or เคมี. No preceding เ/แ/โ/ใ/ไ is stranded before the cut; no following combining mark begins a row detached from its preceding base. Upper/lower vowels and tones remain visibly associated at returned capture detail. No direct risky cut immediately after a leading vowel or before a combining mark is exercised: those forced-edge risks remain NOT_EXERCISED, not broadly passed. ใ is absent from this input. Fine native attachment/placement remains UNRESOLVED; no five-vowel or dictionary inference.

Proposed-list membership is a correspondence result, not the linguistic grade itself. Independently, และ / เตรียมตัว and ต้อง / เดินทาง divide complete units; วิชา / เคมี divides two complete units in วิชาเคมี without splitting letters inside either. No new internal word/syllable cut is observed among these edges.

## B versus historical A

Inspected original historical [A capture](../../local/qa/WO-VISUAL-016/06-resolution-paragraph.jpg) directly during analysis; A preserved unchanged. This is B against historical A, not a contemporaneous A rerun.

| Aspect | A: WO-016 | B: current WO-017 |
|---|---|---|
| Rows / underlying content | 5 / 237 codepoints | 5 / same 237 codepoints |
| Cuts | 55,113,172,227 | 49,100,154,207 |
| Known internal splits | เรีย / น; ทุ / ก; เรี / ยน | None of these; no เรียน or ทุก split at any new edge |
| Expression boundary | เตรียม / ตัว | เตรียมตัว stays on one row |
| Body bounds, capture pixels | approx (939,297)..(1356,470) | approx (939,297)..(1356,470) |
| Text bounds | approx x947..1345, y310..453 | approx x955..1335, y310..453 |
| Apparent Thai glyph scale | Baseline | Visually comparable; no observed shrinking/growth |
| Final row | ยนวิชาเคมี, very short | เตรียมตัวเข้าห้องเรียนวิชาเคมี, longer |
| Containment/readability | Complete, contained; bad word edges | Complete, contained; improved observed edges |

This conclusion checks every new B edge, not only disappearance of A's old offsets. All occurrences of เรียน (including within ห้องเรียน) and ทุก remain uncut by any B row boundary. No new bad boundary appears in the observed B rows. All four actual cuts correspond to proposed opportunities. Equal body width/apparent scale as well as font/UI byte equality support attribution to this experimental input change; exact native font metrics and internal layout measurements are not available.

Both bodies are opaque and fully on-screen with visible padding; no blankness, clipped final row, missing-glyph square, raw tag, visible U+200B symbol or conspicuous inserted spacing. B's final centered row still leaves unused side width, but is less extreme than A's ten-codepoint final row. No observed layout/readability regression at capture detail. **Observed experimental benefit is limited to this fixed paragraph/container/Medium configuration.** It does not close production wrapping, BUG scope, all-Thai segmentation or authorize automatic ZWSP.

![B original capture](../../local/qa/WO-VISUAL-017/06-B-resolution.jpg)

## Guarded lifecycle and restoration

Every manager call ran separately with explicit --probe probe-017, exit 0, states inspected before the next dependent step:

1. check — all THREE original.
2. Independent B/A identity, underlying equality, staged/font/UI verification.
3. install — all THREE probe.
4. check — all THREE probe; later Steam launch.
5. Medium-only observation; no UI Scale change needed.
6. Direct final Medium capture [07-final-medium.jpg](../../local/qa/WO-VISUAL-017/07-final-medium.jpg); Settings X then normal Quit. [90-after-quit.json](../../local/qa/WO-VISUAL-017/90-after-quit.json) confirms Campus absent.
7. restore — all THREE original.
8. check — all THREE original.
9. Independent [92-final-hashes.json](../../local/qa/WO-VISUAL-017/92-final-hashes.json) verifies installed originals/retained backups/staged B plus unchanged B/A manifests/maps. All match pre-install. Backups retained.

All commands above use python tools/manage_probe.py followed by their action and --probe probe-017. No guard/restore failure or bypass.

| Bundle | Installed original AND retained backup SHA-256 | Unchanged staged B SHA-256 |
|---|---|---|
| fonts_assets_all.bundle | 33aa34892719fbc7caaabd0a292c32bb135bc61978a4cd3ce73c6c40da8f4e6e | 588f15fad01635da3fb5b86d5c3946cbb7bd85b40304364294fb23d73c207f3e |
| localisation_assets_localisationenglish.bundle | c1e7ca97f260813ccc9a1cf463f20d066631f8e5616bf797fe8d5ae93227878f | f4832c361fc21513cd3f598a40a5714f7a8c40df56177b5523a5ad9d1bf61514 |
| ui-prefabs-general_assets_all.bundle | 2152e5ba289ccb0414c462371cfdfe05cc7ac589a10a75b8b46d359afd99786d | b8933a120178276ca8246b1494e881ec97a20a7b9b4804b3a16cf080efeb7e14 |

Final Medium directly observed, all THREE original verified. No persisted-restart assertion, graphics/preset/dropdown/slider/Apply/save/gameplay change, hidden-row activation, Small/Large/restart matrix, VOWEL-02 detail grading, font/layout rebuild, source/map/proposed-unit edit, branch switch, commit/push, asset/font upload or release approval. Frozen A and prior actual-tooltip acceptance remain intact.
