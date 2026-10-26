# WO-SARA-AM-005 — build accepted (BUILD_READY)

2026-10-26. PM (Claude): ACCEPT_BUILD. Diagnostic probe only; not a fix; BUG-THAI-003 OPEN.

PM checks: (1) probe bundles re-hashed against manifest probe_sha256 — all three match; parent hashes match local frozen005 files — match. (2) Local protected files from reports/sara-am-004-preservation-before.json re-hashed — none changed. (3) Report content reviewed: one record [118,42,82] -> glyph 29 (ก); nine original ligatures kept, none starting with 118; no serialized lookup to update; only I2LS_Levels533 localisation changed; font object/hash f9855a70... unchanged; UI bundle identical to 005. Fonts bundle is 16 bytes larger than 005, consistent with one added record (PM did not independently parse the bundle: UnityPy not available to PM; structural readback relies on the analyst's check). (4) tools/manage_probe.py: real change is one added choice 'probe-sara-am-lig-001'; the whole-file diff is a line-ending change (LF to CRLF), no logic change (git diff --ignore-space-at-eol). Installed originals and the other 5 game-folder files were not independently re-hashed by PM (outside PM mount); accepted from analyst record and re-checked by the QA lifecycle in the runtime WO.

Interpretation rules accepted: a positive needs L1 replaced by one ก-shaped glyph matching L5 while L2-L4 intact. Negative or unchanged L1 is INCONCLUSIVE about the executor (liga flag, lookup init, fallback, record override are unresolved), not proof of absence; a result of "not executed" still removes this probe's route to D+B and moves the decision to option A (code plugin), which needs a user scope decision.

Next: runtime WO docs/qa/WO_SARA_AM_LIG_001.md for Antigravity, single variant, one run.
