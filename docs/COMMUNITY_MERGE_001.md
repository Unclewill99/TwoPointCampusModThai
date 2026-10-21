# Community translation merge — 2026-10-21

User supplied Two Point Campus MOD Thai AI-1-MODV1-0-1742896937.zip to reuse existing translations. Archive contains localisation and fonts only; no README/license supplied. Imported text stays local; publication permissions not established.

Built local/prototype/community-merge-001 using the project's probe-013 font/UI unchanged. Reloaded and exactly compared all 15,677 records. Preserved 70 project translation records; imported 15,602 records (15,314 contain Thai, 286 exactly equal English source). Five records use English fallback: one token/tag mismatch and four ambiguous duplicate-key records. The mismatch translates a color attribute to Thai; quarantined in local/imports/community-ai-v1/quarantine.json. Existing project review flags remain authoritative in their source translation files; import status is not language approval.

Draft: local/imports/community-ai-v1/merged-draft.json. Audit: reports/community-import-audit.json. Build: reports/community-merge-001-build.json. Third-party font was not adopted. No global ZWSP insertion, installation, game run, commit or push. Candidate is NOT_RUN and is not yet registered with manage_probe.py. Existing experimental fixed-width UI and shaping limitations remain.

Next bounded work: inspect/fix the five fallback records against source and prepare a short main-menu/gameplay smoke test using the existing guarded installation lifecycle. Avoid full retranslation and exhaustive screenshot matrices. Existing source corpus is retained as authority; imported language quality and compatibility remain unverified beyond structural checks.


## Corrected candidate ready — 2026-10-21

community-merge-002 resolves all five fallbacks: restores <color=green> while preserving damage variables, and verifies identical imported translations at both occurrences of each duplicate key. All 15,677 values reload-match. Fonts/UI remain byte-identical to probe-013; manager now supports this candidate and read-only check reports three originals. No installation. Next: qa/WO_SMOKE_MERGE_001.md, bounded three-view single-session screening. Gameplay deferred to a selected safe context.
