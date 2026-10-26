# Initial handoff briefs

Latest 2026-10-26 (PM): fresh-translation-006 INSTALLED in the live game by the user's authorization (reports/fresh-translation-006-install-20261026T0835Z.json). Installed state probe/probe/probe (candidate hashes match manifest); originals backed up in local/backups/fresh-translation-006 (hashes match manifest originals); save backup 20261026T083508277171Z verified. No active WO. Revert: close game, manage_probe restore --probe fresh-translation-006, then check.

Latest 2026-10-26 (PM): FRESH006-001 accepted PASS_SCOPED (SARA_AM_FRESH006_001_ACCEPTANCE.md): candidate 006 shows correct ต่ำ on Settings Game, Video tooltip and the real opening modal at Medium scale. BUG-THAI-003 FIX_VERIFIED_SCOPED (not closed). No active WO; originals installed. Next steps await user decision (install 006 live / more coverage).

Latest 2026-10-26 (PM): WO-SARA-AM-008 accepted (SARA_AM_008_ACCEPTANCE.md): candidate fresh-translation-006 (fonts-only) BUILD_READY; regression narrowed. Runtime WO docs/qa/WO_SARA_AM_FRESH006_001.md READY_FOR_HANDOFF: menu Settings surfaces + real opening modal (original defect site), Medium scale, read-only; tester Antigravity or user-authorized; not confirmed. Originals installed. BUG-THAI-003 OPEN.

Latest 2026-10-26 (PM): GLYPH-002 accepted ALL_STACKED_OK (timing deviation recorded, SARA_AM_GLYPH_002_ACCEPTANCE.md). WO-SARA-AM-008 to ChatGPT (offline): production candidate fresh-translation-006 (fonts bundle only, text unchanged) + real-screen regression plan. READY_FOR_HANDOFF via user; not confirmed. Originals installed; no runtime WO active. BUG-THAI-003 OPEN.

Latest 2026-10-26 (PM): WO-SARA-AM-007 accepted BUILD_READY (SARA_AM_007_ACCEPTANCE.md). Runtime WO docs/qa/WO_SARA_AM_GLYPH_002.md READY_FOR_HANDOFF: single-run 15-cluster probe (probe-sara-am-glyph-002); tester Antigravity or user-authorized; not confirmed. Originals installed. BUG-THAI-003 OPEN.

Latest 2026-10-26 (PM): GLYPH-001 accepted STACKED_OK (SARA_AM_GLYPH_001_ACCEPTANCE.md). Scope decision: D+B for the 15 census clusters, fix only in fonts bundle (text unchanged). WO-SARA-AM-007 to ChatGPT (offline build of 15-cluster probe) READY_FOR_HANDOFF via user; not confirmed. Originals installed; no runtime WO active. BUG-THAI-003 OPEN.

Latest 2026-10-26 (PM): WO-SARA-AM-006 accepted BUILD_READY (SARA_AM_006_ACCEPTANCE.md). Runtime WO docs/qa/WO_SARA_AM_GLYPH_001.md READY_FOR_HANDOFF: single-run appended-glyph probe (probe-sara-am-glyph-001); tester is Antigravity or user-authorized; receipt/execution not confirmed. Originals installed. BUG-THAI-003 OPEN.

Latest 2026-10-26 (PM): WO-SARA-AM-LIG-001 accepted EXECUTED (SARA_AM_LIG_001_ACCEPTANCE.md): game executes exact [118,42,82] ligature. Next WO-SARA-AM-006 to ChatGPT (offline): corpus census + one appended composite-glyph probe build. READY_FOR_HANDOFF via user; not confirmed. Originals installed; no runtime WO active. BUG-THAI-003 OPEN.

Latest 2026-10-26 (PM): WO-SARA-AM-005 build accepted (SARA_AM_005_ACCEPTANCE.md). Antigravity WO docs/qa/WO_SARA_AM_LIG_001.md READY_FOR_HANDOFF: single-run ligature-executor probe (probe-sara-am-lig-001); receipt/execution not confirmed. Diagnostic only, BUG-THAI-003 OPEN.

Latest 2026-10-26 (PM): WO-SARA-AM-004 accepted as INCONCLUSIVE (SARA_AM_004_ACCEPTANCE.md). Next: WO-SARA-AM-005 to ChatGPT, build/verify-only ligature-executor probe (probe-sara-am-lig-001). READY_FOR_HANDOFF via user; not confirmed. No Antigravity WO until the build is accepted.

Latest 2026-10-26: PM role transferred to Claude (user decision). WO-SARA-AM-004 issued to ChatGPT: offline analysis only for an atomic-text-preserving fix of atomic ต่ำ (BUG-THAI-003). READY_FOR_HANDOFF via user; receipt/execution not confirmed. No Antigravity runtime WO active. See docs/WO_SARA_AM_004_OFFLINE_SOLUTION_ANALYSIS.md.

Latest: WO-SARA-AM-002-AB-R2 accepted as diagnostic result. No active Antigravity rerun; atomic ต่ำ remains broken, only decomposed row improves. Controller next evaluates atomic-text-preserving solution offline. See docs/SARA_AM_002_AB_R2_ACCEPTANCE.md.

Current: control-gate navigation evidence accepted; flyover reached, modal not observed. Next Antigravity WO docs/qa/WO_SARA_AM_002_AB_R2.md resumes unchanged A/B with 60-second natural load/flyover wait and correct desktop/query ordering. READY_FOR_HANDOFF. See docs/SARA_AM_003_CONTROL_DISPOSITION.md. No extra originals rerun.

Latest: sara-am A/B returned SETUP_LIMIT; font cells NOT_RUN. Antigravity next WO docs/qa/WO_SARA_AM_003_CONTROL_GATE.md, originals only; no candidate installation. See docs/SARA_AM_002_AB_DISPOSITION.md. READY_FOR_HANDOFF.

Current assignment: Antigravity WO docs/qa/WO_SARA_AM_002_AB.md. Two staged diagnostic candidates, one intro modal each; no tutorial advancement. READY_FOR_HANDOFF, not yet received/executed. Controller static trace/build complete; see docs/SARA_AM_003_EXPERIMENT.md.

Latest: WO-SARA-AM-001-REFERENCE delivered and accepted (REFERENCE_ESTABLISHED); no further offline rerun. Controller next investigates native TMP handling/modal binding before any new Antigravity runtime WO. BUG-THAI-003 OPEN. See docs/SARA_AM_001_REFERENCE_ACCEPTANCE.md.

Next Antigravity WO: docs/qa/WO_SARA_AM_001_REFERENCE.md — browser reference versus existing evidence only; no game launch/install. READY_FOR_HANDOFF. Mod-menu work remains complete.

Latest 2026-10-22: Antigravity delivered WO-FRESH-MENU-005-R2; Controller accepted destination PASS. Mod menu work complete; no active menu retest assignment. See docs/FRESH_MENU_005_R2_ACCEPTANCE.md. Earlier READY_FOR_HANDOFF notes are superseded.

## Current assignment — 2026-10-22

Latest: first menu WO accepted partially (Mod label PASS; destination NOT_RUN). Next Antigravity assignment is docs/qa/WO_FRESH_MENU_005_R2.md, destination only with explicit coordinate mapping and visually verified target. READY_FOR_HANDOFF; execution not confirmed.

User directs all screen testing to Antigravity. Controller handles builds, structural checks, work orders and report acceptance; no Controller desktop testing. Antigravity next WO: docs/qa/WO_FRESH_MENU_005.md, candidate fresh-translation-005, main-menu Mod and its destination only. READY_FOR_HANDOFF; receipt/execution not yet confirmed.

These are prepared briefs, not evidence of agent execution.

## Claude — Translator

Read README.md and the Controller's approved source schema. Propose a glossary and style guide for Thai campus management UI: concise, natural, humorous where appropriate. Translate only assigned stable IDs. Keep all tokens, tags and escapes intact. Flag ambiguity and length concerns. Do not invent source strings or translate Museum text as Campus content. Return a branch/PR plus unresolved questions.

First task when source extraction is available: propose terminology from a small representative batch for Controller approval before bulk translation.

## Antigravity — QA

Independently review extraction round-trip and the Thai rendering prototype. Test upper/lower vowels and stacked tone marks, Thai/Latin/numeric mixtures, punctuation, multiline text, narrow buttons, tooltips and scaling. Record build, screen, string ID, reproduction steps, expected/actual result, screenshot and severity. Check placeholders and duplicate/missing IDs. Do not approve rendering from asset names alone.

First task: review reports/initial-inspection.json and propose a reproducible rendering test matrix. In-game tests remain pending a working prototype.

## Controller — Next engineering tasks

1. Resolve Museum logical bundle IDs to physical hashed bundle paths via catalog location data.
2. Inspect Thai TMP font assets, fallback chains and localisation font mappings.
3. Identify actual shaping and line-break behavior; metadata names alone are insufficient.
4. Inspect Campus English TextAsset format and establish stable ID extraction/import.
5. Build an isolated reversible prototype and hand it to QA.
