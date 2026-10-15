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

| Owner | Work | State |
|---|---|---|
| Controller | Resolve Museum physical font bundles and inspect fallback/shaping configuration | Next engineering task; not completed |
| Controller | Extract Campus source IDs and confirm text/token format | Source extraction done; runtime token grammar/import validation pending |
| Controller | Reversible Thai rendering prototype | Pending investigation |
| Claude | 50-source-string PILOT-001 | r2 received and independently structurally checked; accepted for QA/prototype preparation; waiting for QA findings |
| Antigravity | Independent pilot language/token review; runtime rendering tests | Assigned r2 review in docs/PILOT_001_R2_REVIEW.md; runtime NOT_RUN pending prototype |

## Limits and handoff

No game files patched; no in-game Thai rendering validated. Catalog references are inventory evidence only. Agent messages are currently relayed by the user. Controller command-line access to the private remote remains unresolved; GitHub Desktop is available for the user to push local commits. Later local commits have not been independently verified on the remote.

Update this file on a completed handoff, meaningful finding, blocker or assignment change. Record tests as executed only with evidence; do not infer progress from elapsed time. Game binaries and local extracted assets remain outside version control.
