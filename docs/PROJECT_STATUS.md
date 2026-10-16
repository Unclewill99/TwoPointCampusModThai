# Project status

Updated: 2026-10-16 (Asia/Bangkok)
Owner: ChatGPT — Project Controller

## Completed

- Central GitHub repository established; initial commit 5d27e6c visible in the user's GitHub screenshot.
- Read-only initial Campus/Museum inventory and reproducible inspection tool completed.
- Translation editorial baseline v0.2 and provisional glossary approved with Controller clarifications (c2f4238).
- Antigravity QA matrix, report template and synthetic corpus reviewed and accepted for prototype planning, with corrections in docs/qa/CONTROLLER_ACCEPTANCE.md.
- Extracted 15,677 English records from 25 Campus TextAssets; exact decoded-text roundtrip passed. Two duplicate keys retained with segment-qualified IDs. Full corpus is local-only.
- Prepared 50-source-record PILOT-001 and docs/PILOT_001_HANDOFF.md for Claude.
- Received and reviewed Claude's pilot through local r3; independent structural checks passed with zero errors. Selected linguistic QA edits integrated; 21 contextual ambiguities and 3 humor flags remain. On 2026-10-16 the r3 file hash still matches its validation report.
- Audited 23 serialized Campus TMP font character tables; no Thai-range entries in those tables, zero read errors. Dynamic/runtime coverage remains unknown.

## Current assignments

**BUG-THAI-001: MITIGATED / TARGET-WORD VERIFIED ใน probe-003** — คำว่า “ความถี่” แยกสระอี/ไม้เอกสอดคล้อง reference ตาม WO-VISUAL-003 พร้อมผล Small/Large/restart/dropdown ตามขอบเขตที่ตรวจ ยังเปิดเพื่อ regression ของอักษรซ้อนอื่น ไม่ใช่ full shaping PASS.

| Owner | Work | State |
|---|---|---|
| Controller | Resolve Museum physical font bundles and inspect fallback/shaping configuration | Named Thai bundles found; mapping, feature counts and fallback references inspected; runtime behavior unverified |
| Controller | Extract Campus source IDs and confirm text/token format | Source extraction done; runtime token grammar/import validation pending |
| Controller | Reversible Thai rendering prototype | Probe-004 runtime report accepted: 5 scoped PASS, 2 PARTIAL, 2 diagnostic observations, 3 single-line wrapping observations; originals independently verified |
| Claude | 50-source-string PILOT-001 | Linguistic review integrated into local r3; four selected wording changes structurally validated; no further revision assigned |
| Antigravity | Independent pilot language/token review; diagnostic QA planning | Linguistic review integrated; synthetic shaping/wrapping matrix remains unexecuted |
| Desktop visual agent | Broader synthetic diagnostics | WO-VISUAL-004 completed; next needs exact unobscured references for 2 partial cases and a controlled wrapping build |

## Limits and handoff

Probe-001 failed with blank dropdown values; probe-002 recovered dropdowns but exposed stacked-mark overlap. Probe-003 passed the target-word/reference test. Probe-004 exercised 12 mapped synthetic cases; five scoped passes, two reference gaps, malformed/decomposed observations and three single-line tooltip observations. Wrapping remains NOT_EXERCISED. Originals independently hash-checked after restoration. Next: exact reference views for two partial cases, then a same-container forced-width wrapping experiment. Full shaping, atlas stress, token/plural semantics and gameplay coverage remain pending. Agent messages are relayed by the user. Remote GitHub synchronization has not been freshly verified; local commits alone do not establish upload success.

Update this file on a completed handoff, meaningful finding, blocker or assignment change. Record tests as executed only with evidence; do not infer progress from elapsed time. Game binaries and local extracted assets remain outside version control.
