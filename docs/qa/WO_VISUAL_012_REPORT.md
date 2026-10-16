# WO-VISUAL-012 REPORT

Date: 2026-10-16 (Asia/Bangkok). **A and B both show a bounded, readable six-row tooltip with all three repeats. NO OBSERVED A/B IMPROVEMENT in line boundaries, completeness or mark integrity.** No global Thai wrapping PASS, dictionary inference, production ZWSP approval or fixed-width rollout approval follows from this synthetic paragraph.

## Inputs, gates and environment

Read WO_VISUAL_012.md, reports/probe-012-build.json and both manifests/maps. Verified map SHA-256 against each manifest before install (00-map-hashes.json):

| Variant | Diagnostic-map SHA-256 |
|---|---|
| probe-012a | 7821f43b82188d94c5fda585a06705aec7143f0bc5a20e1d1bd61197f130ee16 |
| probe-012b | 31500cf8853a6e436759e5c85025911c716f951a5857b88900367ff06864eca7 |

A has the continuous Thai paragraph repeated three times; B differs only by mapped U+200B insertions. No manual LF in either. Font and UI staged hashes match accepted probe-011; actual bounds and apparent glyph scale were also inspected independently. Source spelling preserved; no code/map/translation/value edit in-session.

Used computer-use skill. Each variant launched independently through Steam Play only after separate successful install and installed check calls. Build 10.3.169253+2024-12-06.1241 visible in 04-a-menu.jpg / 15-b-menu.jpg. English/Medium verified in 05/16; Full Screen Window, unchanged 3840 x 2160 @ 60hz in 06/17. Main-menu Settings only; no Apply/settings changes, gameplay/save load, force-close, branch changes, commit/push, loader installation or asset upload.

All saved screenshots are original returned 1920 x 1080 JPG bytes. The supported computer-use capture API exposes no native-resolution/high-detail capture option; no higher-detail source was acquired, and no enlarged compressed image is presented as extra evidence. Fine mark positioning is therefore scoped to visible capture detail; this is not native-resolution typography certification. Approximate bounds below are capture pixels, not native or Unity layout units.

## Actual Resolution bounds and A/B comparison

Evidence: 07-a-resolution.jpg and 18-b-resolution.jpg. Same hover (110,382) using zero-delta pointer placement, followed by a fresh capture after full appearance. Both white bodies approximately (939,284)-(1355,483), about 416 x 199 pixels; turquoise left edge around x=936, pointer extending to about x=914 at y=383. Text approximately x=947..1345, y=297..469. Six ink rows, arranged as three pairs with slightly larger vertical gaps between pairs. No manual newline exists in source, so all five visual boundaries are runtime behavior; the visual gaps are not evidence of source LF.

All background edges visible and all text stays inside them, with small padding. No clipped edge, blank tooltip, oversized unused background, raw tag, missing-glyph square, visible ZWSP symbol or conspicuous inserted gap. First text starts `มหาวิทยาลัย`; last ends `ประสิทธิภาพ`. Apparent Thai glyph scale and row placement are broadly the same between A/B, with no observed shrink/growth; exact native font point size and pixel-perfect equality unmeasured. Same-width observation supports comparison, but does not establish internal layout identity from pixels alone.

### Exact observed rows

A (07-a-resolution.jpg):

```text
มหาวิทยาลัยทูพอยต์เปิดรับสมัครนักศึกษาใหม่เพื่อเข้าศึกษา
ในหลักสูตรการบริหารจัดการสถานศึกษาอย่างมีประสิทธิภาพ
มหาวิทยาลัยทูพอยต์เปิดรับสมัครนักศึกษาใหม่เพื่อเข้าศึกษา
ในหลักสูตรการบริหารจัดการสถานศึกษาอย่างมีประสิทธิภาพ
มหาวิทยาลัยทูพอยต์เปิดรับสมัครนักศึกษาใหม่เพื่อเข้าศึกษา
ในหลักสูตรการบริหารจัดการสถานศึกษาอย่างมีประสิทธิภาพ
```

B (18-b-resolution.jpg), transcribed as visible text; invisible U+200B is omitted only for comparison:

```text
มหาวิทยาลัยทูพอยต์เปิดรับสมัครนักศึกษาใหม่เพื่อเข้าศึกษา
ในหลักสูตรการบริหารจัดการสถานศึกษาอย่างมีประสิทธิภาพ
มหาวิทยาลัยทูพอยต์เปิดรับสมัครนักศึกษาใหม่เพื่อเข้าศึกษา
ในหลักสูตรการบริหารจัดการสถานศึกษาอย่างมีประสิทธิภาพ
มหาวิทยาลัยทูพอยต์เปิดรับสมัครนักศึกษาใหม่เพื่อเข้าศึกษา
ในหลักสูตรการบริหารจัดการสถานศึกษาอย่างมีประสิทธิภาพ
```

Joining each transcription without a separator matches the complete A map and B map after removing only U+200B, including all 324 underlying codepoints / three repeats (23-row-alignment.json). This confirms textual accounting; it does not independently prove fine raster mark fidelity. Source-preserved `ทูพอยต์` was not corrected. No unresolved row-text uncertainty at the readable capture level; subpixel attachment/positioning remains outside capture coverage.

### Every boundary and mark check

Offsets are counts of underlying Unicode codepoints before the break, ignoring U+200B; they are not UTF-16 or glyph indices.

| After row | Underlying offset | Actual end / next start in BOTH | B inserted opportunity at this boundary | Visible integrity |
|---|---:|---|---|---|
| 1 | 56 | เข้าศึกษา / ในหลักสูตร | Yes | No stranded leading vowel or combining mark |
| 2 | 108 | ประสิทธิภาพ / มหาวิทยาลัย | Yes | Repeat boundary; no base/mark split |
| 3 | 164 | เข้าศึกษา / ในหลักสูตร | Yes | Same as row 1 |
| 4 | 216 | ประสิทธิภาพ / มหาวิทยาลัย | Yes | Same as row 2 |
| 5 | 272 | เข้าศึกษา / ในหลักสูตร | Yes | Same as row 1 |

Rows 1/3/5 finish the complete `เข้าศึกษา`; rows 2/4/6 begin with `ใน`, whose leading vowel ใ and consonant น remain together on the same row. No trailing เ/แ/โ/ใ/ไ stranded before the next consonant, and no new row begins with an isolated upper/lower vowel or tone mark. At the other two boundaries, final พ in `ภาพ` and initial ม of `มหาวิทยาลัย` have no intervening detached combining mark. None of the five observed boundaries splits a word/syllable internally in this paragraph; they occur between the displayed units above. This is a scoped visual/linguistic observation, not independent approval of every proposed corpus segmentation.

Marks inside rows (e.g. ั, ึ, ู and ่ in the displayed text) appear associated with their bases, with no visible floating row-start mark or clipping. Fine positioning cannot be fully graded from the returned compressed capture. Grade separately:

| Aspect | A | B |
|---|---|---|
| Box containment | Observed intact | Observed intact; same approximate bounds |
| Readability/completeness | Six readable rows, all repeats accounted | Same |
| Boundary base/mark integrity | No visible split at any of five boundaries | Same |
| Word/syllable boundary quality | No observed internal split at these boundaries | Same |
| Invisible-character artifacts | No visible artifact | No visible ZWSP artifact |
| Improvement from B | Baseline | NO OBSERVED IMPROVEMENT |

B boundaries coincide with inserted opportunities, but A independently chooses identical boundaries without U+200B. Therefore coincidence does not establish that ZWSP caused these breaks or improved them. Continuous Thai can wrap without a dictionary; dictionary support is NOT established. Do not generalize this favorable paragraph to arbitrary Thai text, fonts, widths, scales or marks. **Production ZWSP remains unapproved.**

## Original Antialiasing Mode tooltip

Evidence 08-a-antialiasing.jpg and 19-b-antialiasing.jpg, actual original Antialiasing Mode content, not Quality Presets. Hover (151,850), unchanged SMAA. Both white bodies approximately (939,795)-(1355,902), about 416 x 107 pixels excluding pointer; text approximately x=955..1336, y=806..890. Four complete readable rows in both:

```text
Enables anti-aliasing, which reduces jagged edges.
SMAA is higher quality that FXAA.
SMAA is also slower to run than FXAA.
Disable to increase graphics performance.
```

`that` copied as displayed. No clipping, blankness, unexpected large empty space, unreadable shrinking or observed A/B placement/scale difference. Comparable to probe-011. Scoped shared-layout readability check only.

## Sequential lifecycle, originals between variants and hashes

Every manager command ran alone in its own inspected call; each exited 0 and returned all three expected file states. Every invocation included the exact variant via `--probe`:

- A: `check --probe probe-012a` all original (01), `install --probe probe-012a` all probe (02), `check --probe probe-012a` all probe (03). Only then Steam Play in a later call. Normal Settings X > Quit; fresh inventory showed Campus absent. `restore --probe probe-012a` all original (09), `check --probe probe-012a` all original (10).
- Independent SHA-256 checks between variants verified ALL THREE originals (11-between-original-hashes.json), before B install. No A-to-B overlay.
- B: `check --probe probe-012b` all original (12), `install --probe probe-012b` all probe (13), `check --probe probe-012b` all probe (14). Only then Steam Play in a later call. Normal Settings X > Quit; fresh inventory showed Campus absent. `restore --probe probe-012b` all original (20), `check --probe probe-012b` all original (21).

Commands use `python tools/manage_probe.py` before each action above. Exact output files with those prefixes include inspected exit codes. Both install/check operations validate staged and installed manifest hashes and original backups. Final independent hashes in 22-final-hashes.json verify actual installed originals and retained backups for BOTH variants (six backup files), plus unchanged staged candidates:

| Bundle | Installed original AND each retained A/B backup SHA-256 |
|---|---|
| fonts_assets_all.bundle | 33aa34892719fbc7caaabd0a292c32bb135bc61978a4cd3ce73c6c40da8f4e6e |
| localisation_assets_localisationenglish.bundle | c1e7ca97f260813ccc9a1cf463f20d066631f8e5616bf797fe8d5ae93227878f |
| ui-prefabs-general_assets_all.bundle | 2152e5ba289ccb0414c462371cfdfe05cc7ac589a10a75b8b46d359afd99786d |

| Candidate | Font SHA-256 | Localisation SHA-256 | UI SHA-256 |
|---|---|---|---|
| A | 588f15fad01635da3fb5b86d5c3946cbb7bd85b40304364294fb23d73c207f3e | 354ec6b25ef4a285d7a097353f2fb78b08882d0ea26feab91b4840d1f3b43344 | b8933a120178276ca8246b1494e881ec97a20a7b9b4804b3a16cf080efeb7e14 |
| B | 588f15fad01635da3fb5b86d5c3946cbb7bd85b40304364294fb23d73c207f3e | 4f90a4474c175aa831fef090747a8a9a55e68dc39ef7f4600c7e4b10984d0b0f | b8933a120178276ca8246b1494e881ec97a20a7b9b4804b3a16cf080efeb7e14 |

Post-test evidence analysis initially used an unresolved relative parent for independent hashes, then a console Thai encoding print failed after successful hash-file writing; these affected only read-only reporting, not any manager step or game lifecycle. Corrected absolute-root hash verification and inspected saved row-alignment JSON confirm the evidence above. No probe operation failed.

Evidence stored under local/qa/WO-VISUAL-012/. Final state **original/original/original**, all backups retained. No commit/push.
