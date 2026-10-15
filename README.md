# Two Point Campus Thai Mod

Project started 2026-10-15. Controller: ChatGPT. Translator: Claude. QA: Antigravity.

## Current state

Initial read-only inspection completed. No game files patched. Central repository: https://github.com/Unclewill99/TwoPointCampusModThai . Remote configured locally; initial upload is pending authenticated access. External agents have not yet been contacted.

Run `python tools/inspect_games.py` from this folder to regenerate `reports/initial-inspection.json`. Requires Python and UnityPy (already available on the inspected machine). Game installations are expected in sibling folders as on this machine.

## Workflow

Controller owns extraction, string IDs, integration, task assignment and release decisions. Claude owns Thai translation and terminology proposals. Antigravity owns independent linguistic, placeholder and in-game visual QA. Work through branches and pull requests after the central remote is configured. Do not overwrite another agent's assigned batch.

Translation records will contain stable source ID, source text, Thai text, context, batch and review status. Preserve placeholders, markup, escapes and line breaks. Source extraction and format identification must precede translation batches.

Keep game binaries, extracted corpora and font files local. Commit original tools, project documentation and mod-authored changes only; assess individual assets before publication.

First milestone: a reversible Thai rendering prototype covering combining marks, wrapping, fallback fonts and UI clipping. Full translation starts after source IDs and import round-trip are verified.
