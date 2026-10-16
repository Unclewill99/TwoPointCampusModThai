# WO-VISUAL-011 REPORT

Date: 2026-10-16 (Asia/Bangkok). **Observed width containment PASS; additional English wrapping PASS; complete readability PASS in this tested case. Antialiasing Mode remains readable with a slightly wider box. Restoration PASS for ALL THREE bundles.** This is a paired constraint experiment, not a single-factor result or a general fix claim.

## Scope and environment

Read WO_VISUAL_011.md, reports/probe-011-build.json and local/prototype/probe-011/manifest.json. Supplied candidate sets text RectTransform m_SizeDelta.x from 0 to 800 and parent layout m_ChildControlWidth from 1 to 0. Original Normal wrapping, fitter and long English stimulus retained. Requested 800 units is not a measured native or capture width. No experimental values, scripts or translations changed during testing.

Windows desktop, launched through the visible Steam Two Point Campus Play button only after successful install AND installed hash check in separate calls. Build 10.3.169253+2024-12-06.1241 (04-main-menu.jpg), English/Medium UI Scale (05-en-medium.jpg), Full Screen Window and unchanged 3840 x 2160 @ 60hz (06-video.jpg), matching WO-007. Returned captures are 1920 x 1080 JPG. Used computer-use skill, inspected returned screenshots and saved their original bytes without crop, rescale or annotation. Bounds below are approximate capture pixels, not native game pixels.

Only main-menu Settings visited. No Apply, settings selection/change, gameplay/save load, forced closure, branch change, commit/push, loader installation or asset upload. No Quality Presets chase. No Thai, ZWSP, dictionary or atlas conclusion.

## Resolution: actual bounds, wrapping and completeness

Evidence: local/qa/WO-VISUAL-011/07-resolution-tooltip.jpg. Hovered the same (110,382) as WO-007 using zero-delta scroll; captured after tooltip appeared fully. Compared with the previously inspected local/qa/WO-VISUAL-007/17-long-tooltip.jpg: the reference spans the viewport horizontally at approximately (0,342)-(1919,425), showing only a clipped single middle row, with first/last segments unreadable.

Probe-011 white background is approximately (939,174)-(1355,593), about 416 x 419 capture pixels, with turquoise left edge around x=936 and left-pointing triangle extending to about x=914 at y=383. All body edges are visible within the viewport. Text ink occupies approximately x=947..1345, y=185..581. The longest lines retain a small visible side margin; no text crosses the white border. This is an observed bounded box, not an assertion that its displayed width equals 800 pixels. Background is not blank and contains no oversized unused region; normal small padding remains.

There are **17 readable visual rows**: first source segment on one row, middle source segment across 14 rows, and last source segment across two rows. Exact visible row transcription (newlines here represent visual rows):

```text
Sets window resolution.
This is a readable English sentence with ordinary
spaces. This is a readable English sentence with
ordinary spaces. This is a readable English sentence
with ordinary spaces. This is a readable English
sentence with ordinary spaces. This is a readable
English sentence with ordinary spaces. This is a
readable English sentence with ordinary spaces. This
is a readable English sentence with ordinary spaces.
This is a readable English sentence with ordinary
spaces. This is a readable English sentence with
ordinary spaces. This is a readable English sentence
with ordinary spaces. This is a readable English
sentence with ordinary spaces. This is a readable
English sentence with ordinary spaces.
Reduce resolution to increase CPU and graphics
performance.
```

The reference diagnostic-map has only two LF separators, at zero-based indexes 23 and 719. Those manual boundaries occur after visual row 1 and visual row 15. The 14-row middle segment has **13 additional breaks within its newline-free source**, and the final source segment has one additional break before `performance.`. These observations establish additional wrapping for this stimulus rather than inferring it from a smaller box or enum name.

All first/middle/last source segments are visible and readable. The middle transcription, joined with ordinary spaces, contains all 12 repeated sentences in order; no visible omission or truncation. Final period visible. No clipping, blankness or raw tags observed. English glyph scale appears broadly similar to WO-007 long / WO-010 retry, with readable roughly 15-pixel-high glyphs; exact native point size and pixel-perfect scale equality were not measured. Height grows to accommodate the text rather than displaying a single tiny row. Scoped result: containment, extra wrapping and completeness PASS at these settings.

## Antialiasing Mode shared-path impact

Evidence: 08-antialiasing-mode-tooltip.jpg, actual original Antialiasing Mode content. Hovered (151,850), SMAA unchanged. White body approximately (939,795)-(1355,902), about 416 x 107 capture pixels, excluding turquoise border and left pointer. Text approximately x=955..1336, y=806..890. Four complete readable rows:

```text
Enables anti-aliasing, which reduces jagged edges.
SMAA is higher quality that FXAA.
SMAA is also slower to run than FXAA.
Disable to increase graphics performance.
```

`that` in row 2 is transcribed as displayed. Compared with WO-010 retry/08-antialiasing-mode-tooltip.jpg (approximately x=939..1337, y=795..902), the right edge moves about 18 capture pixels farther right; height and left placement are broadly unchanged, and centered text shifts slightly right. No additional visual rows, clipping, blankness, unreadable shrink or unexpected large empty space. The patch therefore has a visible shared-layout width effect here, while preserving the inspected tooltip's readability. This is not a comprehensive regression pass.

## Sequential command evidence and final hashes

Each command below ran in its own call; exit code and all THREE states inspected before proceeding. Every invocation used the explicit target `--probe probe-011`:

1. `python tools/manage_probe.py check --probe probe-011`: exit 0, all original (01-original.txt).
2. `python tools/manage_probe.py install --probe probe-011`: exit 0, all probe (02-install.txt).
3. `python tools/manage_probe.py check --probe probe-011`: exit 0, all probe (03-installed.txt). Manager validated staged and installed SHA-256 plus original backups. Steam launch occurred only afterward in a separate orchestration call.
4. Normal exit through Settings X > main-menu Quit. Fresh window inventory confirmed Campus absent.
5. `python tools/manage_probe.py restore --probe probe-011`: exit 0, all original (09-restore.txt).
6. `python tools/manage_probe.py check --probe probe-011`: exit 0, all original (10-final-original.txt).

Independent actual installed/backup/staged SHA-256 values recorded in 11-final-hashes.json. ALL THREE installed hashes and retained backups match original; staged candidates match the unchanged manifest:

| Bundle | Final installed AND retained backup SHA-256 | Staged probe-011 SHA-256 |
|---|---|---|
| fonts_assets_all.bundle | 33aa34892719fbc7caaabd0a292c32bb135bc61978a4cd3ce73c6c40da8f4e6e | 588f15fad01635da3fb5b86d5c3946cbb7bd85b40304364294fb23d73c207f3e |
| localisation_assets_localisationenglish.bundle | c1e7ca97f260813ccc9a1cf463f20d066631f8e5616bf797fe8d5ae93227878f | fb3719a4f431e259340d51537395c3077ad5372968635139a69a3402723053c0 |
| ui-prefabs-general_assets_all.bundle | 2152e5ba289ccb0414c462371cfdfe05cc7ac589a10a75b8b46d359afd99786d | b8933a120178276ca8246b1494e881ec97a20a7b9b4804b3a16cf080efeb7e14 |

Manifest/build/reference diagnostic-map hashes in 12-source-hashes.json. All inspected screenshots and exact manager outputs, including exit codes, saved under local/qa/WO-VISUAL-011/. Final state **original/original/original**, backups retained. No commit/push.
