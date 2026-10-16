# WO-VISUAL-005 — exact reference gaps and same-slot wrapping experiment

Date: 2026-10-16. Controller: ChatGPT. This WO has a reference-only task and conditional game runs. No runtime result exists yet.

## A — Close two reference gaps without reinstalling probe-004

Open local/qa/references/WO-VISUAL-005/exact-reference.html. It contains the exact injected sequences ปิ ปี ปึ ปื ฝี ฟิ ปั ฟั and พ่อ แม่ ช้า น่า ป้า กู้. Its loading panel is in normal document flow, not a fixed overlay. Record browser zoom from its menu, custom FontFace loaded evidence and unobscured screenshots of every group. Respect browser security refusals; if file access is denied, have the user open the page directly rather than bypassing a tool refusal.

Compare matching groups against existing local/qa/WO-VISUAL-004/08-controls-unclipped.jpg and 06-game-medium.jpg. If source resolution/compression prevents a confident assessment, keep PARTIAL and say why; do not invent new runtime evidence. No need to reinstall probe-004 solely for these references. Browser text is comparison evidence, not new game coverage.

## B — Controlled wrapping preflight

Read reports/probe-005-build.json and each variant's local manifest/map. Game slot: Settings > Video > hover Resolution. Every variant changes ONLY UI/Settings/Tooltips/Resolution relative to probe-003 and uses byte-identical fonts. Requested `<width=400>` is a candidate runtime control, not a verified 400-native-pixel container. Text contains no manual newlines. Do not infer actual width or font size from the tag alone.

Variants, in order:

1. probe-005-control — repeated spaced English, tests whether the actual tooltip path parses the tag and wraps.
2. probe-005a — repeated continuous Thai baseline.
3. probe-005b — same underlying Thai content with mapped U+200B insertions; removing U+200B exactly reproduces 005a.

Use English, Medium, unchanged resolution; no gameplay or Apply. Before each install close Campus normally, verify original state and verify diagnostic-map hash against that variant manifest. Then use:

```
python tools/manage_probe.py check --probe VARIANT
python tools/manage_probe.py install --probe VARIANT
python tools/manage_probe.py check --probe VARIANT
```

Replace VARIANT with the exact name above. Launch via Steam, open the same page, hover the same Resolution control at a matched pointer position; do not select a resolution. Capture full screen plus readable tooltip. Record actual visible bounds, line count, clipping, apparent text scale, raw-tag visibility and dropdown regressions.

### Control gate

If control displays literal width tags, never wraps, shrinks to a single unreadable line, extends off screen or otherwise fails to establish a usable multi-line bounded area, mark the wrapping comparison BLOCKED, restore and STOP game runs. Do not install A/B or alter scripts to force success. Report this as a failed experiment setup, not a proven Thai breaker defect.

If control produces readable multiple lines, proceed to A and B, always restoring to original between runs. Runtime font size and bounds may still change with content. Record differences; equal key/tag alone is not sufficient to claim equal usable width. If equality cannot be established, describe observations without causal ZWSP conclusions.

For Thai runs, record exact visible line ends/starts, stranded leading vowels/combining marks, word/syllable splits, visible ZWSP boxes and clipping. Do not add manual breaks. No production ZWSP approval follows this experiment. Multiple lines do not establish dictionary-based breaking.

## Restore after EVERY variant

Quit normally, then use the same variant name:

```
python tools/manage_probe.py restore --probe VARIANT
python tools/manage_probe.py check --probe VARIANT
```

Both must be original before the next install. Never switch directly between installed probes. Keep backups. If restore fails, stop and notify Controller. Do not force-close unsaved gameplay or edit code/translations/catalogs. No branch switch, commit/push, binary/font upload, save load or settings changes beyond navigation.

## Deliver

docs/qa/WO_VISUAL_005_REPORT.md; inspected screenshots and exact command evidence under local/qa/WO-VISUAL-005/. Include A's two case dispositions separately from B's control gate and optional A/B results. Record build, variant/map hashes, resolution/scale, reference loading/zoom, actual measured bounds and limits, and final original hashes. If game control is unavailable, deliver reference-only findings and mark runtime BLOCKED.
