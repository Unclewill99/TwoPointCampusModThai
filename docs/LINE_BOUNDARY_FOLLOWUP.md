# Next line-boundary question — 2026-10-18

Controller audited the existing transcriptions against the unchanged actual-tooltip map with tools/audit_boundary_coverage.py. Source LF boundaries are excluded and repeated scales are deduplicated by key/offset. The actual-tooltip evidence supplies nine distinct additional runtime cut positions. WO-012's five paragraph cuts represent only two distinct contexts: เข้าศึกษา / ในหลักสูตร and ประสิทธิภาพ / มหาวิทยาลัย. This is useful positive evidence, not broad adversarial coverage.

CRP-WRAP-03 previously appeared in WO-004's Vsync tooltip as a single line; it did not exercise wrapping. It is absent from the WO-012 A/B paragraph. The unanswered question is what boundaries this different corpus paragraph produces at the established bounded width, and whether an observed cut detaches a leading vowel from its following base or a combining sequence from its base. No dictionary claim or ZWSP comparison is needed.

## Staged candidate

probe-016 is a NEW synthetic diagnostic, distinct from unchanged probe-013 used in WO-014/015. tools/build_probe_016.py copies probe-013 font/UI bytes exactly and replaces only UI/Settings/Tooltips/Resolution with three concatenated, unchanged copies of CRP-WRAP-03. Each paragraph has 79 Unicode codepoints; total 237. No LF, separators, width tags, ZWSP or spelling changes. Exact source, repetition boundaries and hashes are in local/prototype/probe-016/diagnostic-map.json. Three repeats help expose several cuts, but are not three independent source contexts.

The paragraph contains เ, แ, โ and ไ; it does not contain ใ. Existing ใ coverage in WO-012 is separate. Combining vowels/tone marks are present inside the paragraph, but their presence does not guarantee that a boundary tests their attachment. Do not claim every target was exercised unless an actual observed edge provides evidence. This is a bounded sample, not an exhaustive forced-edge sweep.

Build/reload assertions verify exactly one changed decoded source segment, all other TextAssets/segments identical, font/UI hashes unchanged, original installed bundles matching before staging, and no production translation edits. Guarded manager check --probe probe-016 passes with all THREE originals. Candidate is staged, not installed; runtime NOT_RUN. reports/probe-016-build.json records build identity. probe-013 acceptance remains unchanged at 18/20.

## Handoff

WO-VISUAL-016 is ready for Antigravity/desktop QA, Medium only, same bounded Resolution slot. No repeat of the 18-key scale matrix, no new high-detail VOWEL-02 claim, no hidden-control, gameplay or graphics experiment. Record exact rows, completeness and every actual boundary; assign uncertainty rather than guessing tiny marks. If the paragraph does not wrap, the boundary question is NOT_EXERCISED, not PASS. If it wraps cleanly, accept only observed boundaries; unresolved forced-edge cases remain backlog.

The brief is prepared locally and has not been sent to another chat. User relay remains the coordination workflow. No game asset/font upload, commit/push or release approval is implied.


## WO-016 result — 2026-10-18

Completed and reviewed: complete/contained content, but internal word splits observed in เรียน and ทุก (BUG-THAI-002). Do not promote to Thai wrapping PASS. Direct leading-vowel/combining edge risks remain unexercised; native detail unresolved. See PROBE_016_DISPOSITION.md. Next Controller researches line-breaking behavior before any new control; no unchanged repeat or production ZWSP. All three originals independently verified.
