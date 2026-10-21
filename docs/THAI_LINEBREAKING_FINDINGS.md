# Thai line-breaking investigation and targeted control

Date: 2026-10-18. Controller continued from BUG-THAI-002. No game launch or installation. Static findings: ../reports/thai-linebreaking-investigation.json.

## What is established

The consumed tooltip TMP component (path_id 2671690608638065206) in the frozen probe-016 UI bundle still serializes m_TextWrappingMode=1, the build-decoded Normal value. m_wordWrappingRatios=0.40000000596, character/word spacing=0 and font size=34. These are defaults, not runtime property measurements. Do not repeat the prior raw 1-to-0 enum experiment or change spacing/ratio speculatively.

resources.assets contains LineBreaking Leading Characters (38 codepoints) and LineBreaking Following Characters (98); neither decoded asset contains Thai codepoints. This identifies those two tables only. It does not prove that no other Thai support or dictionary exists, or that these tables caused the three observed splits. Adding Thai letters to global forbidden-leading/following lists would affect many contexts and is not an evidence-backed repair.

Local token-to-native mapping identifies TMP_Settings.LoadLinebreakingRules, TMP_Text.CalculatePreferredValues and TextMeshProUGUI.GenerateTextMesh. Native excerpts contain explicit U+200B comparisons, including VA 0x183509750 and 0x18350b244. This provides a plausible code-supported test input, not a demonstrated runtime fix. GenerateTextMesh's very large unwind group includes a partially decoded tail/possible inline table data; no complete decompilation or absence-of-dictionary conclusion is claimed. Original native listings remain local.

## New test, distinct from WO-012

WO-012's A and B selected the same already-acceptable cuts in a different paragraph. Its no-improvement result stands. WO-016 now provides a different fixed input with actual internal-word failures, so it creates a new unanswered intervention question: can explicit proposed word-break opportunities prevent the splits within เรียน and ทุก without changing underlying text, font, width or apparent glyph size?

Probe-017 is B; frozen probe-016/WO-016 is baseline A. B differs only by 47 U+200B insertions across the three copies. Controller's explicit proposed units per paragraph are:

เมื่อ | ถึง | เวลา | ทุกคน | ต้อง | เดินทาง | ไป | เรียน | ที่ | โรงอาหาร | และ | เตรียมตัว | เข้า | ห้องเรียน | วิชา | เคมี

These are a manually specified experimental list for independent QA review, not an automatic tokenizer or approved production dictionary. Each paragraph's units concatenate literally to the original 79-codepoint source; stripping only U+200B from B yields the same 237-codepoint A. No proposed break falls at A's problematic underlying offsets 113,172,227. Repetition joins are separately mapped. No whitespace, manual LF, width tag, spelling change, font/layout mutation or translation-file edit is made.

tools/build_probe_017.py reload-verifies exactly one changed localisation segment and all other TextAssets/segments unchanged. Font/UI are byte-identical to probe-016. Manager now accepts probe-017; guarded check succeeds with all THREE originals. Candidate is staged, NOT installed/runtime NOT_RUN. Frozen baseline A/report are preserved, and no new A run is needed if current build/settings match WO-016. Historical A comparison must be qualified if environment or apparent width/font scale differs.

## Decision

WO-VISUAL-017 is ready for Antigravity/desktop QA via user relay, B-only at Medium, with independent review of the proposed units and exact B/A underlying boundary accounting. It is prepared locally, not sent. Observe whether the known internal splits disappear, whether new bad splits arise, and whether visible artifacts/containment worsen. Matching an inserted opportunity alone does not prove every Thai context is correct.

BUG-THAI-002 remains OPEN until a reviewed result; even a positive B test would establish an experimental workaround only. No automatic production ZWSP, global source rewrite, dictionary claim, invisible-character policy change or release approval. The 18/20 actual-tooltip acceptance and VOWEL-02 detail limitation remain unchanged.


## WO-017 acceptance — 2026-10-18

Completed and accepted as scoped experimental benefit for one paragraph/container/Medium, versus historical WO-016 A. Four edges / three contexts, all 237 codepoints, no observed cut inside เรียน/ทุก and no new bad edge. BUG-THAI-002 remains OPEN with experimental mitigation; no production ZWSP or dictionary/global wrapping approval. See PROBE_017_ACCEPTANCE.md. No unchanged repeat assigned.
