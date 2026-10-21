# WO-VISUAL-016 — new corpus paragraph at established bounded width

Date: 2026-10-18. Ready for Antigravity / desktop QA. Runtime NOT_RUN. Target **probe-016**, a new synthetic candidate; do not install probe-013 for this WO. Read ../LINE_BOUNDARY_FOLLOWUP.md, ../PROBE_013_MILESTONE.md, WO_VISUAL_012_REPORT.md and local/prototype/probe-016/{manifest,diagnostic-map}.json.

## One question and fixed scope

At Medium UI Scale, what actual runtime breaks occur in the unchanged CRP-WRAP-03 paragraph, and do any observed breaks detach a Thai leading vowel or combining sequence from its base? Text is three exact copies without separators, 237 codepoints, no LF/ZWSP/tags. Font/UI are byte-identical to probe-013. Only Resolution's tooltip body differs. This is synthetic text, not the translated Resolution description or a playable release candidate.

No Small/Large/restart matrix, actual-tooltip repeat, high-detail VOWEL-02 grading, hidden-row activation, preset/graphics changes, gameplay/save load, font/layout rebuild or ZWSP experiment. The paragraph lacks ใ; do not claim five-vowel coverage or dictionary support.

## Capability and guarded lifecycle

Verify real current Windows target capture and supported non-mutating pointer placement before installation. Reject wrong-target images and recover by fresh selection/activation; if current capability cannot be established, stop before install. Campus must be closed normally. Run each command separately and inspect exit code and states before continuing:

1. `python tools/manage_probe.py check --probe probe-016` — require all THREE original.
2. Independently verify manifest/map/staged hashes; font/UI must match probe-013. Never rebuild a candidate during this test.
3. `python tools/manage_probe.py install --probe probe-016` — all THREE probe.
4. `python tools/manage_probe.py check --probe probe-016` — all THREE probe.
5. Only then launch through Steam in a later call; fresh target inventory and visually correct game capture required before input.

Record build, English, actual resolution/display mode and initial scale. Main-menu Settings only. If necessary change ONLY UI Scale to Medium and record it; do not change sliders, toggle values, dropdown graphics values, resolution, Apply or save state. The prior game setting is not current evidence. Capture dimensions are not render resolution.

## Observation

Open Settings > Video and hover the identifying Resolution LABEL with supported non-mutating pointer placement, away from its dropdown. Derive coordinates from a fresh correct screenshot. Hold 1.8 seconds and capture once after the tooltip appears. One additional capture is allowed only for incomplete appearance/occlusion after moving onto known empty background and re-observing the target. No prolonged chase or settings edits to force wrapping.

Transcribe every visible row exactly, retaining uncertainty explicitly. Match their concatenation against all three map paragraphs; do not silently drop marks/spaces or repair source spelling. Record raw observed rows and the exact normalization used for any automated accounting. This input has no whitespace, so literal row concatenation should equal the map without normalization. Record first/last text, all three repeats and final row. Unaccounted text is not a complete PASS.

For every actual boundary, record the count of original Unicode codepoints before the break (zero-based string cut offset; not UTF-16/glyph count), left/right context and nearby codepoints. Check separately:

- A preceding เ/แ/โ/ใ/ไ separated from its following base.
- A following combining upper/lower vowel, tone mark or other combining mark detached from its preceding base.
- Apparent internal word/syllable splits. Record exact text for linguistic review; do not infer a dictionary or approve segmentation merely because marks remain together.

Distinguish boundaries inside each paragraph from the synthetic joins at offsets 79 and 158. Repeated same-context cuts are not additional distinct cases. A target simply occurring within a row is not targeted edge coverage. If the evidence cannot resolve a mark, record UNRESOLVED at that boundary; the current capture cannot certify fine native shaping.

Record approximate box/text bounds in capture pixels, visible line count, clipping/containment/readability, missing glyphs and unused-space effects. Preserve original screenshot bytes with no resize, sharpening or annotation. No forced expected line count or line boundaries: measure what actually appears.

If no automatic break occurs, classify boundary behavior NOT_EXERCISED and stop. If blank, clipped or unreadable, record setup failure and restore. If readable and wrapped, classify only the observed edges, with per-edge failures/uncertainties retained. Do not call this a full adversarial or all-Thai PASS. No extra control/primary-key testing is required because font/UI bytes are unchanged.

## Final restoration and delivery

Capture Medium before normal Quit. After the game is confirmed closed, run separately:

1. `python tools/manage_probe.py restore --probe probe-016`
2. `python tools/manage_probe.py check --probe probe-016`

Require all THREE original and independently verify installed/staged/retained-backup and map/manifest hashes. Keep backups. Every path after installation requires normal exit/restoration, including a failed observation. Stop/report guard or restore failure without bypass; no force-close.

Write docs/qa/WO_VISUAL_016_REPORT.md with evidence in local/qa/WO-VISUAL-016/. Include exact candidate identity, environment, target/capture, original rows, literal map comparison, per-edge offsets/codepoints/outcomes, image-detail limits and final Medium/original state. This is not an A/B test or a new acceptance of the actual-tooltip translations. No branch switch, commit/push, asset upload or release approval by tester.
