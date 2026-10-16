# WO-VISUAL-005 REPORT

Date: 2026-10-16, Asia/Bangkok. Result: reference evidence supplied for both gaps; wrapping comparison BLOCKED by failed control setup. probe-005a and probe-005b were NOT_RUN and never installed. Original bundles restored and verified.

## A — Exact reference comparison using existing game evidence

Opened `local/qa/references/WO-VISUAL-005/exact-reference.html` without editing it or reinstalling probe-004. Loading panel was in document flow and showed family ProbeThai, loadCount 1, face status loaded, weight 500, check=true. `02-exact-vowel-font.jpg` records loading evidence. `03-exact-both.jpg` shows every group unobscured. Chrome menu showed 100% zoom (`04-zoom100.jpg`). Used the computer-use skill and real Windows screenshots.

Compared directly with the existing, unmodified `local/qa/WO-VISUAL-004/08-controls-unclipped.jpg` and `06-game-medium.jpg`, inspected again during this WO. Those are prior game coverage, not a new runtime test. Browser captures are approximately 1073x771; prior game captures 1920x1080. JPG evidence is saved as returned by the capture tool, without subsequent crop, scaling or annotation.

| Case | Exact groups and assessment | Disposition |
|---|---|---|
| CRP-VOWEL-02 | ปิ ปี ปึ ปื ฝี ฟิ ปั ฟั. Exact reference now available for all eight. All game groups are present and unclipped. Broad upper-mark arrangement is consistent with reference, but the game row has small marks only a few captured pixels high; distinctions among ิ/ี/ึ/ื and clearance at ascenders cannot all be confidently resolved from this compressed source. | Reference availability gap CLOSED; detailed shaping remains PARTIAL due to existing game image resolution/compression. No invented runtime evidence or full shaping PASS. |
| CRP-STACK-02 | พ่อ แม่ ช้า น่า ป้า กู้. All six game groups and all reference groups visible. Tone marks remain distinct above their bases; กู้ shows lower vowel and upper tone mark, without panel clipping or visible overlap. Relative arrangement agrees at the legibility level supported by the existing screenshot. | PASS for this injected subset, closing the prior obscured-reference comparison gap. Not a pixel-identical comparison or full-corpus approval. |

The WO-VISUAL-004 report was not edited; this table records the follow-up dispositions.

## B — Control gate

Read reports/probe-005-build.json and all three variant manifests/maps. Verified each diagnostic-map SHA-256 against its manifest before control installation. Verified that removing U+200B from 005b text exactly reproduces 005a; B contains 30 insertions. No manual newlines were added. Exact computed evidence: `01-preflight-hashes.json`. The build describes identical probe-003 font bytes and only the Resolution tooltip key changed for each variant; this does not prove runtime tag support or equal bounds.

With Campus closed, check returned original/original, install returned probe/probe, and installed check returned probe/probe. All manager commands used the exact `--probe probe-005-control` name; outputs are saved in 05-original-check.txt, 06-control-install.txt, 07-control-check.txt.

Launched through Steam Play. Visited only main-menu Settings. English and Medium confirmed (`08-control-en-medium.jpg`). Resolution unchanged: 3840 x 2160 @ 60hz, Full Screen Window (`09-control-video.jpg`). Game version: 10.3.169253+2024-12-06.1241. No save/gameplay loaded, no settings selections or Apply. Returned game captures are 1920x1080; coordinates below refer to those captures, not native 4K coordinates.

Hovered Resolution label at window-relative (110,382), using zero-delta pointer scroll without clicking a value. After at least two seconds, the tooltip became a large blank white horizontal region. Waited two additional seconds and recaptured: unchanged (`10-control-tooltip-failed.jpg`, `11-control-tooltip-confirmed.jpg`).

| Control measurement | Observation |
|---|---|
| Visible white body bounds | Approximately x=0 through right screen edge x=1919, y=186 to 580; about 1920x395 visible pixels. Both horizontal edges reach the viewport boundary; full intended bounds cannot be measured and off-screen extent cannot be excluded. |
| Readable line count | 0. No readable English lines established. |
| Text scale | Not assessable because text is not visible/readable. |
| Raw width tag visibility | No readable literal tag visible; absence does not establish successful parsing. |
| Clipping/occlusion | White area spans the viewport and obscures the upper Settings controls. This is not a usable bounded text area. |
| Dropdown regression | Closed values were readable before hover. During hover the tooltip obscured them; open-dropdown interaction was NOT_RUN after the gate failure. No value selection made. |

Control gate FAILED. Wrapping comparison BLOCKED. This is a failed experiment setup, not evidence of a Thai line-breaker defect. The requested `<width=400>` has not been verified as any actual 400-pixel container. Per WO and user instructions, stopped game runs immediately after recording the failed control; 005a/005b were neither installed nor launched. Thai line starts/ends, syllable splits, stranded marks, ZWSP artifacts and A/B causal conclusions are NOT_RUN. No production ZWSP approval.

## Restoration and hashes

Exited Settings and selected Quit normally. Guarded restore returned original/original (`12-control-restore.txt`); independent check returned original/original (`13-final-check.txt`). Retained control backups. Installed and backup hashes are recorded in `14-final-hashes.json` and match manifest original hashes:

- fonts_assets_all.bundle: `33aa34892719fbc7caaabd0a292c32bb135bc61978a4cd3ce73c6c40da8f4e6e`
- localisation_assets_localisationenglish.bundle: `c1e7ca97f260813ccc9a1cf463f20d066631f8e5616bf797fe8d5ae93227878f`

No direct probe-to-probe switching occurred. Lifecycle: original → control → original. A/B skipped by gate.

Build report SHA-256: `e84553c7ca4afde7edaee46fbdb7d8c77f1a59dac88b59065ad252c12f1bc184`.

| Variant | Manifest SHA-256 | Map SHA-256 (matched) |
|---|---|---|
| probe-005-control | 3e130a5d3339becef3c2268948c4d5e6da95c9a11f58bd8662c95a524f4028ac | 3aeffad8451f0c67a49249057827af70bbd82b376a5edd47b6cc4a2860911adc |
| probe-005a | 19ccff5df02042c245ccfba1b3516572296021647fccd25ea318dccd449e62c1 | 799c809a4c3f5914cc307ffb33fff42912b80b814843bc9c598b78b574e54b52 |
| probe-005b | 0b09b6fc627139c93bc761aaa21cae5e57ae5476988618aa8294cedb5d5ecf82 | c9c58874d64d87686328b0192e9bf7fcfa3435f56e578f2ec7546d5e1589e513 |

Installed control bundle hashes were verified by manager: fonts `588f15fad01635da3fb5b86d5c3946cbb7bd85b40304364294fb23d73c207f3e`; localisation `ccc2af9adc5b95f18876e0e993ec234595172dc37541563979e3cd672226df74`.

Evidence saved under `local/qa/WO-VISUAL-005/`. No source, script, translation, manifest, map or reference edits during testing; only authorized temporary installation/restoration and evidence/report creation. No commit/push, branch switch, binary/font uploads, forced termination or cache deletion.
