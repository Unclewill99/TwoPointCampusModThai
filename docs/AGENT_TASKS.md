# Initial handoff briefs

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
