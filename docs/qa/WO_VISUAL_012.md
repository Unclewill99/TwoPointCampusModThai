# WO-VISUAL-012 — bounded Thai A/B wrapping

Date: 2026-10-16. Controller: ChatGPT. A=probe-012a unmodified Thai; B=probe-012b same text plus mapped U+200B. Both repeat the synthetic paragraph three times, no manual newline. Font/UI bundles byte-identical to accepted probe-011. Read reports/probe-012-build.json and both local manifests/maps; verify map hashes before testing.

## Execution

Run A then B, separately. With Campus closed normally, replace VARIANT below with the exact name:

```
python tools/manage_probe.py check --probe VARIANT
python tools/manage_probe.py install --probe VARIANT
python tools/manage_probe.py check --probe VARIANT
```

Run each step in separate inspected calls. Require original for all THREE before install and probe for all THREE after, then launch via Steam in a later call. Stop on error. English/Medium, unchanged resolution; no gameplay/save loading, Apply or settings changes. Hover Settings > Video > Resolution at the same location as WO-011.

Capture full tooltip and, if supported, original high-detail capture rather than merely enlarged compressed pixels. Record actual bounds, readable line count, first/last text, glyph scale, clipping/blankness/ZWSP artifacts. Transcribe each visible row exactly; mark uncertainty rather than guessing glyphs. Align rows with map text (ignoring U+200B only for comparison), accounting for all three repeats. No manual breaks means each visible break is runtime behavior.

Check every boundary for stranded leading vowels, split base/combining marks, word/syllable splits and whether B breaks coincide with inserted opportunities. Treat corpus insertion positions as proposed break opportunities, not independently approved linguistic segmentation. A continuous Thai paragraph can wrap character-wise without dictionary support; do not infer a dictionary. Inspect source-preserved spelling; do not fix text in-session.

Capture original Antialiasing tooltip separately for shared-layout readability. If A is unreadable, blank or offscreen, record setup/coverage limit; restore and report before proceeding with B if meaningful comparison is impossible. Do not alter settings to force success.

After EACH variant, Quit normally, then:

```
python tools/manage_probe.py restore --probe VARIANT
python tools/manage_probe.py check --probe VARIANT
```

Require ALL THREE original before next install. No direct A-to-B overlay; retain backups. After B, final originals must be verified. No code/map/translation edits, branch changes, commit/push, loader install, force-close or asset uploads.

## Comparison and report

Write docs/qa/WO_VISUAL_012_REPORT.md; inspected images/exact commands and hashes under local/qa/WO-VISUAL-012/. Compare actual widths and apparent glyph scale between A/B: byte-identical UI alone does not establish runtime equality. If bounds differ, qualify causal conclusions. Grade readability/completeness, mark integrity, line-boundary quality and invisible-character artifacts separately. Do not issue global Thai wrapping PASS from this paragraph. No production ZWSP or fixed-width rollout approval follows. Record final restoration for all THREE files.
