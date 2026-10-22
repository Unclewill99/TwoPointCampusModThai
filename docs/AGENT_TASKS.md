# Initial handoff briefs

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
