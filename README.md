# Two Point Campus Thai Mod

Resume from [22 Oct session checkpoint](docs/SESSION_CHECKPOINT_2026-10-22.md).

Project started 2026-10-15. Controller: ChatGPT. Translator: Claude. QA: Antigravity.

## Current direction — full fresh corpus runtime sample

2026-10-22: [Claude round5 scoped corrections integrated](docs/CLAUDE_REVIEW_R5_RECEIPT.md):321 rows/62 batches verified, no removed flags. Full15,677 records retained;12,710 translated and2,967 justified source identities pending review. fresh-translation-004 built/reload-verified; font/UI unchanged from merge-006; Main menu observed, requested target views NOT_RUN after [setup failure](docs/FRESH_SMOKE_001_DISPOSITION.md). Driver target guard patched and mock-checked; [original-game control preflight](docs/qa/WO_FRESH_SMOKE_001_RESUME.md) required before any reinstall. Good Friends, Pastoral Support, disease names and joke backlog remain; BUG-THAI-002/003 OPEN. Older counts below are historical.

## Current state

Updated 2026-10-21. Central repository: https://github.com/Unclewill99/TwoPointCampusModThai . Probe-013 has scoped visual acceptance for 18 of 20 actual Settings tooltips at Small/Medium/Large. The two hidden rows remain untested. Temporary tests have restored all three original game bundles; the candidate is not approved for release or permanent installation.

Read [the milestone and next work](docs/PROBE_013_MILESTONE.md) and [current project status](docs/PROJECT_STATUS.md) first. Exact shaping input/reference/font preparation is complete; improved detailed game capture remains unresolved. [WO-VISUAL-016](docs/PROBE_016_DISPOSITION.md) is completed: text remains complete/contained, but internal Thai word splits were observed (BUG-THAI-002). WO-017 demonstrates a scoped experimental mitigation using explicit break opportunities; production transformation remains unapproved and BUG-THAI-002 stays open. [Independent review of two break maps is accepted](docs/SEGMENTATION_001_ACCEPTANCE.md). [WO-018 screening is accepted](docs/PROBE_018_ACCEPTANCE.md): four 800/Medium cells show a later clean MSAASamples break and unchanged WorldDetail wrapping. Width 600 is deferred; no further desktop run is assigned. All three installed bundles were freshly checked as original. No new translator batch is assigned. Full source, binaries, font files and screenshots remain local. Git synchronization is separate from local milestone acceptance.

Run `python tools/inspect_games.py` from this folder to regenerate `reports/initial-inspection.json`. Requires Python and UnityPy (already available on the inspected machine). Game installations are expected in sibling folders as on this machine.

## Workflow

Controller owns extraction, string IDs, integration, task assignment and release decisions. Claude owns Thai translation and terminology proposals. Antigravity owns independent linguistic, placeholder and in-game visual QA. Work through branches and pull requests after the central remote is configured. Do not overwrite another agent's assigned batch.

Translation records will contain stable source ID, source text, Thai text, context, batch and review status. Preserve placeholders, markup, escapes and line breaks. Source extraction and format identification must precede translation batches.

Keep game binaries, extracted corpora and font files local. Commit original tools, project documentation and mod-authored changes only; assess individual assets before publication.

Rendering prototypes have established scoped mark/layout results and actual-tooltip wrapping. Full translation still requires the remaining shaping, runtime token/context and wider UI evidence tracked in the milestone; structural import checks alone are insufficient.
