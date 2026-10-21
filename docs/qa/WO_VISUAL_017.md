# WO-VISUAL-017 — proposed break opportunities against observed internal splits

Date: 2026-10-18. Ready for Antigravity / desktop QA. Runtime NOT_RUN. Install **probe-017 (B)**. Baseline A is the unchanged probe-016 / WO-VISUAL-016 original capture. Read ../THAI_LINEBREAKING_FINDINGS.md, ../PROBE_016_DISPOSITION.md, BUG_THAI_002.md, WO_VISUAL_016_REPORT.md and local/prototype/probe-017/{manifest,diagnostic-map}.json.

## Question and preflight

Does B eliminate the observed เรีย / น, ทุ / ก and เรี / ยน internal cuts without text loss, new bad cuts, visible U+200B artifacts or layout/readability regressions? B adds only 47 explicitly mapped U+200B opportunities; removing ONLY U+200B must reproduce A literally. Font/UI bytes must match A. Underlying text is three exact original paragraphs, no LF; do not edit text, proposed units, maps or assets during testing.

Before installation, independently review the proposed per-paragraph units in the map as natural Thai break opportunities. Report any objection explicitly. If a proposed opportunity is itself clearly invalid, stop before install and return linguistic findings; do not silently revise it. Proposal review is separate from observed runtime boundary assessment.

Verify current working native Windows target capture and documented non-mutating pointer placement. If either cannot be established, stop before install. With Campus closed normally, execute separately and inspect successful exits/states:

1. `python tools/manage_probe.py check --probe probe-017` — all THREE original.
2. Independently verify B manifest/map/staged hashes, A's unchanged manifest/map and exact B-minus-U+200B=A equality; font/UI byte equality. Keep A intact.
3. `python tools/manage_probe.py install --probe probe-017` — all THREE probe.
4. `python tools/manage_probe.py check --probe probe-017` — all THREE probe.
5. Launch through Steam in a later call; fresh unique game target and actual game capture before input.

## Observation at Medium only

Record actual build, English, Medium and unchanged resolution/display mode. Baseline reports build 10.3.169253+2024-12-06.1241, Full Screen Window, 3840x2160 @60hz; compare these as evidence, not assumptions. Main-menu Settings > Video, Resolution LABEL only. Derive hover from fresh capture; supported non-mutating placement, hold 1.8 seconds and take one fully appeared original image. One recovery capture allowed for incomplete appearance/occlusion, with fresh target observation. No prolonged chase.

No graphics/preset/dropdown/slider/Apply/save/gameplay changes, hidden rows, Small/Large/restart matrix, high-detail VOWEL-02 grading, font/layout rebuild or production translation edits. If necessary only UI Scale may be set to Medium and recorded. If build/resolution differs from baseline, do not change graphics to reproduce it: record the comparison limitation, restore and report without claiming a controlled A/B result. No A rerun is assigned.

Transcribe every B visible row exactly. Concatenate visible row text and compare literally with diagnosticMap.underlying_text / A text. Normalization NONE except that U+200B is omitted for underlying comparison; do not strip marks/spaces or correct spelling. Invisible characters cannot be assigned visually to a row: report underlying cut offsets, not invented visible ZWSP positions.

For each actual B edge, record underlying Unicode-codepoint cut offset, paragraph/local offset, left/right context and nearby codepoints. Check membership in diagnosticMap.zwsp_underlying_cut_offsets, but grade the actual boundary independently for internal word/syllable splits, detached leading vowels, detached combining marks and uncertainty. Distinguish synthetic joins at 79/158. Mark non-exercised target risks accurately; no full five-vowel/dictionary claim.

Compare with original A evidence local/qa/WO-VISUAL-016/06-resolution-paragraph.jpg: A rows=5; underlying cuts=55,113,172,227. B need not have five rows or the same cuts. Assess whether any cut still splits เรียน or ทุก anywhere, including at a different offset, and whether any new bad edge appears. Do not score success solely because the three old offsets disappear. Capture-detail limits on fine mark positioning remain.

Measure actual B box/text bounds, containment, readability, apparent glyph size, clipped/blank/missing-glyph behavior, short-row whitespace and visible invisible-character artifacts. Compare approximate width/apparent text scale with A (A body approximately x939..1356, y297..470). Height/row count may legitimately differ because wrapping changes. If width or apparent font scale differs, qualify attribution; font/UI byte identity alone does not establish equal runtime bounds. Preserve original screenshots without resizing, sharpening or annotation.

If B is unreadable, blank, clipped or incomplete, stop observation and restore; no secondary experiments. If known bad cuts remain or new bad cuts appear, report NO IMPROVEMENT/REGRESSION with exact edges. If boundaries improve, report only observed experimental benefit, with proposed-opportunity correspondence and limitations. A positive result does not close production wrapping or authorize automatic ZWSP.

## Exit and delivery

Return/verify Medium, capture it and Quit normally. After game closure run separately:

1. `python tools/manage_probe.py restore --probe probe-017`
2. `python tools/manage_probe.py check --probe probe-017`

All THREE originals required; independently verify installed/backup/staged plus unchanged map/manifest hashes, retain backups. Restore on every path after installation. Stop/report guard or restoration failure without bypass or force-close.

Write docs/qa/WO_VISUAL_017_REPORT.md with original evidence under local/qa/WO-VISUAL-017/. Include proposed-unit review, identity/environment, visible rows/literal accounting, per-edge offsets/outcomes, B-versus-historical-A comparison and limits, final Medium/original state. No branch switch, commit/push, asset/font upload, source changes or release approval by tester.
