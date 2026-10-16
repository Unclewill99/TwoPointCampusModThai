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

**Open rendering defect: BUG-THAI-001** — ผู้ใช้พบสระอีและไม้เอกทับกันใน “ความถี่” ของ probe-002 (Settings > Game). Mark positioning ของกลุ่ม `ถี่` เป็น observed FAIL; dropdown comparison ยังคง PASS เฉพาะขอบเขต ต้องแก้และทดสอบซ้ำก่อนรับรอง shaping.

| Owner | Work | State |
|---|---|---|
| Controller | Resolve Museum physical font bundles and inspect fallback/shaping configuration | Named Thai bundles found; mapping, feature counts and fallback references inspected; runtime behavior unverified |
| Controller | Extract Campus source IDs and confirm text/token format | Source extraction done; runtime token grammar/import validation pending |
| Controller | Reversible Thai rendering prototype | Probe-003 built/reloaded with Thai feature records; localisation unchanged from probe-002; not installed. WO-VISUAL-003 ready for stacked-mark comparison |
| Claude | 50-source-string PILOT-001 | Linguistic review integrated into local r3; four selected wording changes structurally validated; no further revision assigned |
| Antigravity | Independent pilot language/token review; diagnostic QA planning | Linguistic review integrated; synthetic shaping/wrapping matrix remains unexecuted |
| Desktop visual agent | Stacked-mark comparison | WO-VISUAL-003 ready; verify browser same-font reference and ความถี่ in probe-003, retain dropdown checks; runtime NOT_RUN |

## Limits and handoff

Probe-001 failed with blank selected dropdown values. Probe-002 passed the original/probe Settings comparison with Thai labels retained, including reported restart checks, but BUG-THAI-001 remains open. On 2026-10-16 both installed originals and staged probe-003 bundle hashes were independently checked successfully. No WO_VISUAL_003_REPORT.md is present: probe-003 runtime remains NOT_RUN. Next: execute the existing WO-VISUAL-003 and inspect its same-font browser reference; synthetic in-game corpus coverage comes later. Full Thai shaping, wrapping, all scales and runtime coverage remain unvalidated. Agent messages are relayed by the user. Remote GitHub synchronization has not been freshly verified; local commits alone do not establish upload success.

Update this file on a completed handoff, meaningful finding, blocker or assignment change. Record tests as executed only with evidence; do not infer progress from elapsed time. Game binaries and local extracted assets remain outside version control.
