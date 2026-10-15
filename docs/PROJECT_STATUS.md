# Project status

Updated: 2026-10-15 (Asia/Bangkok)
Owner: ChatGPT — Project Controller

## Completed

- Central GitHub repository established; initial commit 5d27e6c visible in the user's GitHub screenshot.
- Read-only initial Campus/Museum inventory and reproducible inspection tool completed.
- Translation editorial baseline v0.2 and provisional glossary approved with Controller clarifications (c2f4238).
- Antigravity QA matrix, report template and synthetic corpus reviewed and accepted for prototype planning, with corrections in docs/qa/CONTROLLER_ACCEPTANCE.md.
- Extracted 15,677 English records from 25 Campus TextAssets; exact decoded-text roundtrip passed. Two duplicate keys retained with segment-qualified IDs. Full corpus is local-only.
- Prepared 50-source-record PILOT-001 and docs/PILOT_001_HANDOFF.md for Claude.
- Received Claude's 50-record translation draft; independent structural checks passed with zero errors, including observed square-bracket marker preservation. Editorial review requests a focused revision (docs/PILOT_001_REVIEW.md); 21 contextual ambiguities and 3 humor flags remain.
- Audited 23 serialized Campus TMP font character tables; no Thai-range entries in those tables, zero read errors. Dynamic/runtime coverage remains unknown.

## Current assignments

**Open rendering defect: BUG-THAI-001** — ผู้ใช้พบสระอีและไม้เอกทับกันใน “ความถี่” ของ probe-002 (Settings > Game). Mark positioning ของกลุ่ม `ถี่` เป็น observed FAIL; dropdown comparison ยังคง PASS เฉพาะขอบเขต ต้องแก้และทดสอบซ้ำก่อนรับรอง shaping.

| Owner | Work | State |
|---|---|---|
| Controller | Resolve Museum physical font bundles and inspect fallback/shaping configuration | Named Thai bundles found; mapping, feature counts and fallback references inspected; runtime behavior unverified |
| Controller | Extract Campus source IDs and confirm text/token format | Source extraction done; runtime token grammar/import validation pending |
| Controller | Reversible Thai rendering prototype | Probe-001 FAIL; probe-002 PASS for paired Settings/dropdown comparison and reported restart. Fallback strategy accepted for next diagnostic build; originals restored |
| Claude | 50-source-string PILOT-001 | Linguistic review integrated into local r3; four selected wording changes structurally validated; no further revision assigned |
| Antigravity | Independent pilot language/token review; diagnostic QA planning | Linguistic review integrated; synthetic shaping/wrapping matrix remains unexecuted |
| Desktop visual agent | Settings comparison | WO-VISUAL-002 completed, scoped PASS; originals restored; waiting for diagnostic probe |

## Limits and handoff

Probe-001 failed with blank selected dropdown values. Probe-002 passed the original/probe Settings comparison with Thai labels retained, including reported restart checks. Both original bundles restored and independently hash-checked. Full Thai shaping, wrapping, all scales and runtime coverage remain unvalidated. Next: separate synthetic diagnostic probe and trusted font reference before a new visual work order. Museum catalog references and serialized features are asset evidence only. Agent messages are currently relayed by the user. Controller command-line access to the private remote remains unresolved; GitHub Desktop is available for the user to push local commits. Later local commits have not been independently verified on the remote.

Update this file on a completed handoff, meaningful finding, blocker or assignment change. Record tests as executed only with evidence; do not infer progress from elapsed time. Game binaries and local extracted assets remain outside version control.
