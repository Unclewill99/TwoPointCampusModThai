# WO-VISUAL-018 — reviewed maps across two effective widths

Date: 2026-10-18. Ready for Antigravity / desktop QA. Runtime NOT_RUN. **This work requires opening the game.** Read ../PROBE_018_HANDOFF.md, ../SEGMENTATION_EVIDENCE_GATE.md, ../SEGMENTATION_001_ACCEPTANCE.md, SEGMENTATION_001_REVIEW.md and frozen manifests/maps for all four candidates. Do not rebuild or revise a candidate during testing.

## Active scope revision — 2026-10-21

This section supersedes the full matrix and reporting requirements below for the next run. Historical instructions remain as reference only. Purpose: decide whether reviewed break opportunities warrant further work, using two actual texts at ONE requested width.

- Execute only probe-018-800a then probe-018-800b, Medium: four cells total (two keys x A/B), two separate game sessions. Do not run either 600 variant in this assignment; record those four cells DEFERRED, not failed or passed. A second effective width remains untested.
- Reuse accepted source/map/font isolation checks and SEGMENTATION-001 linguistic review by reference. Do not reread historical WOs, re-review all 34 proposed cuts, rerun builds, or repeat the accepted 18-key scale matrix. Existing manager checks still validate staged/installed hashes; preserve per-run install/exit/restore/check safeguards.
- Capture one readable original image per key per variant (four tooltip images), plus only the minimum settings evidence needed to establish Medium/environment. Reuse a screenshot for multiple observations. Allow at most one recovery capture per key/variant. If still unusable, record UNRESOLVED and stop that cell; do not chase additional captures.
- For each cell record complete/contained text, obvious glyph/mark defects, visible word splits and U+200B artifacts. Compare A/B box width and apparent scale from the same images, with measurement uncertainty. Transcribe and align only rows needed to substantiate a changed or bad boundary; full manual codepoint accounting of every unchanged row is deferred. If completeness cannot be established, mark it UNRESOLVED. Static source equality does not prove runtime completeness.
- Assess each visible B line boundary for obvious internal-word splits or detached vowels/marks. Report uncertainty where detail is insufficient. Detailed Unicode offsets and independent second review are required only for a disputed finding that affects the decision, and may be a separate bounded follow-up.
- Stop after the two runs and restoration, regardless of outcome. No automatic expansion to another width, another text, repairs, or shaping investigation. If the A baseline is unusable, skip its dependent B observation. If neither baseline is usable, restore and end before B. Capture/install/restore safety failures stop the assignment.
- Budget target: 45 minutes of active work, not a promise about tokens or quota. At the budget boundary, stop collecting evidence, exit normally and restore first; report unfinished cells. Report meaningful new findings only; avoid narrating repeated checks.

Deliver docs/qa/WO_VISUAL_018_REPORT.md with a four-row result table, links to original images, a short A/B conclusion, unresolved points, and compact installation/restoration results. Refer to existing validation files rather than copying their contents. Choose BENEFIT_OBSERVED / NO_CLEAR_BENEFIT / REGRESSION / INCONCLUSIVE; this is a screening result, not acceptance of the original eight-cell experiment. No production ZWSP, global width, bug closure or release approval follows automatically.

## Exact matrix and run order

| Run | Exact probe name | Medium MSAASamples | Medium WorldDetail |
|---|---|---|---|
| 1 | probe-018-800a | Plain A baseline | Plain A baseline |
| 2 | probe-018-800b | Reviewed marked B | Reviewed marked B |
| 3 | probe-018-600a | Narrow plain A | Narrow plain A |
| 4 | probe-018-600b | Narrow reviewed marked B | Narrow reviewed marked B |

Exact keys have prefix UI/Settings/Tooltips/. These are their actual control tooltips, not Resolution-slot substitutions. Source spelling/units reviewed; B differs only by mapped U+200B. Font identical throughout. A/B at each requested width have identical UI bytes; 600 differs from 800 only in one shared text-child width field. Eight cells are planned, not pre-approved passes or independent source contexts. Medium only; no Small/Large/restart/18-key regression matrix.

## Capability and sequential lifecycle for EACH run

Before the first install, establish current correct Windows target capture and documented non-mutating pointer placement. Reject wrong-target images; recover with fresh unique selection/activation or stop before install. Only main-menu Settings, English/Medium, unchanged actual resolution/display mode. Record actual build/settings/capture dimensions. Steam startup messages do not establish a usable window; obtain a fresh unique game window and inspect actual game content before input.

For EACH exact variant in order, with Campus closed normally, run separately and inspect exit code/states:

1. `python tools/manage_probe.py check --probe EXACT_VARIANT` — all THREE original.
2. Independently verify that variant's manifest/map/staged hashes. Verify per-width A/B UI/font equality and cross-width same-input localisation equality from manifests/actual files.
3. `python tools/manage_probe.py install --probe EXACT_VARIANT` — all THREE probe.
4. `python tools/manage_probe.py check --probe EXACT_VARIANT` — all THREE probe.
5. Only afterward launch through Steam in a later call. Test the two naturally visible labels; ordinary scrolling is allowed. Change only UI Scale to Medium if needed; no graphics/preset/slider/toggle/dropdown value, Apply, resolution or save/gameplay change.
6. Verify/capture final Medium, Quit normally and confirm Campus absent.
7. `python tools/manage_probe.py restore --probe EXACT_VARIANT` — all THREE original.
8. `python tools/manage_probe.py check --probe EXACT_VARIANT` — all THREE original. Independently verify installed originals/staged/retained backups and frozen map/manifest. Retain backups.

Never overlay one probe directly with another, even when their fonts/UI match. Complete normal exit/restore/check before the next install. Stop/report guard or restoration failure without bypass or force-close. Restore on every path after installation, including failed/incomplete observations. No gameplay/save load, cache deletion, loader, code/source/map edit, hidden-row experiment, branch switch, commit/push or asset/font upload.

## Per-cell observation

Locate MSAASamples and WorldDetail in Settings > Video using fresh real screenshots and ordinary scroll. Hover the LABEL away from sliders/arrows/dropdowns using documented non-mutating placement; hold 1.8 seconds and capture one fully appeared tooltip with its identifying control. One recovery capture per key/run is allowed for incomplete appearance/occlusion after moving to known empty background and refreshing target evidence. No prolonged chase or control changes to reveal unavailable rows.

Record exact visible rows, complete source content/Latin text, first/last text, missing glyphs, blankness/clipping, box/text bounds in capture pixels, row count, apparent glyph size, containment, unused-width/short-row effects and visible U+200B/gap artifacts. Preserve original screenshot bytes without cropping/resizing/sharpening/annotation. Fine native mark positioning remains outside compressed-detail claims.

Preserve raw row transcriptions and exact comparison rules. Static B-minus-only-U+200B must equal A literally, including original LF/spaces. Runtime visible rows may not expose original space/LF ownership: account for every NON-WHITESPACE source character without normalization or mark stripping, explicitly documenting any whitespace-only comparison. Keep source LF counts separately (MSAASamples 0, WorldDetail 2). Do not confuse source LF or natural spaces with newly inserted breaks. Do not invent raw marked-text indices for invisible characters.

For every extra runtime edge, align to ORIGINAL underlying Unicode-codepoint coordinates, record left/right context and nearby codepoints, classify source LF/natural whitespace/inserted-opportunity/other. When whitespace yields an ambiguous cut coordinate, report its source interval and uncertainty, not a made-up exact point. Assess word/syllable boundaries independently of proposed-map membership; check all actual new edges for new internal splits, stranded leading vowels or detached marks. Record UNRESOLVED if capture detail is insufficient. A target merely present within a row is not forced-edge coverage; no automatic dictionary/five-vowel/full-cluster PASS.

## Controlled comparisons and stop rules

- Pair 800a with 800b and 600a with 600b, recording whether B improves, matches or worsens actual edges while preserving content and layout/readability. No improvement is a valid finding; disappearance of old cut offsets alone is insufficient if new bad cuts appear.
- Measure actual width and apparent glyph size for BOTH keys in each pair. UI/font identity alone does not establish runtime equality. If A/B body widths or apparent scale differ beyond measurement uncertainty, retain data but qualify attribution; do not claim a clean input-only comparison.
- Compare 600a with 800a. The narrow candidate must be materially narrower in observed body/text bounds to establish a second effective width. If both appear the same within uncertainty, record WIDTH_FACTOR_NOT_ESTABLISHED, restore after run 3 and skip run 4. Do not guess a different width, edit UI or change graphics mid-test.
- If an A cell is blank/unreadable/clipped/incomplete, record the setup limit and skip its dependent B cell; the other key may continue if safely observable. If neither key has a viable baseline, restore and stop dependent runs. Installation/capture safety/restore failures stop the assignment.
- If a B cell regresses, record exact failure and restore that run; no in-session repair. Further planned runs can proceed only if baseline/layout remain safely observable. Incomplete matrix cells stay NOT_RUN/qualified, never inferred from another key or width.

## Report

Write docs/qa/WO_VISUAL_018_REPORT.md; original evidence under local/qa/WO-VISUAL-018/, segregated by exact probe name. Include executed/skipped eight-cell matrix, hashes and input identities, actual environment per run, actual widths/equality evidence, raw rows/accounting, every extra edge/context/outcome, pairwise benefit/regression/uncertainty and all four restoration states/backups. Record tests only when executed, no repeated prior evidence as new results.

This assignment can support or weaken the explicit-map experimental approach across these two texts/widths. It does not authorize production ZWSP, automatic tokenization, global width deployment, source rewrites, BUG closure, full shaping or release. Controller reviews the complete result before choosing a policy or further work.
