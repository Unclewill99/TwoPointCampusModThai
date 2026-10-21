# Controller disposition — WO-VISUAL-016

Date: 2026-10-18 (Asia/Bangkok). Work order execution accepted as complete. Result is mixed: content/containment scoped PASS, word segmentation OBSERVED FAIL, direct risky leading-vowel/combining edges NOT_EXERCISED. Do not summarize this as Thai wrapping PASS.

Controller read the report, inspected original 06-resolution-paragraph.jpg and independently verified literal row concatenation against the frozen map, all four codepoint offsets, report-linked evidence existence and installed/backup/staged hashes. No new Controller game session. Verification: ../reports/probe-016-controller-review.json.

All 237 codepoints / three paragraphs are accounted for, with no normalization, in five rows of lengths 55/58/59/55/10. Four cuts at 55,113,172,227 are inside paragraph copies, not the synthetic joins at 79/158. The body and final row are visibly contained at Medium within returned capture detail.

Observed internal splits เรีย / น, ทุ / ก and เรี / ยน establish a word-segmentation problem for this synthetic input/container. เตรียม / ตัว is separately retained as an expression-level boundary observation rather than graded identically to a cut inside ทุก. Record BUG-THAI-002; no evidence establishes the defect's extent in other contexts or which algorithm caused it.

No cut immediately follows เ/แ/โ/ใ/ไ or starts with a combining mark. Thus absence of detachment at these four edges does not close the direct adversarial cases. The leading-vowel/base plus combining units that remain together do not make เรี / ยน a valid Thai word/syllable boundary. Fine mark placement remains unresolved by compressed captures; VOWEL-02 is unchanged.

Original three bundles and probe-016 retained backups are independently verified; candidate/map/manifest unchanged. Final Medium and normal Quit are tester evidence. No new restart claim. probe-013's 18/20 scoped actual-tooltip acceptance remains unchanged, but broad dictionary/production wrapping approval is explicitly blocked by this finding.

Next Controller engineering question: inspect the build's TMP/text line-breaking configuration and relevant behavior before choosing a narrow segmentation control. A future comparison may test explicitly reviewed Thai break opportunities with exactly the same underlying text, font and layout; it must answer the newly observed internal splits, not repeat WO-012's already-equal paragraph. This is a planning option, not production ZWSP approval, a new build or a runtime assignment. Do not insert invisible characters automatically, edit translations to conceal the failure, change spelling or widen the shared layout speculatively. No unchanged desktop repeat is justified.
