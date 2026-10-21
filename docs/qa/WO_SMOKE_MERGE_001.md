# WO-SMOKE-MERGE-001 — merged Thai mod, one-session screening

Date: 2026-10-21. Ready for Antigravity via user relay. Runtime NOT_RUN. Candidate community-merge-002. This brief supersedes community-merge-001 preparation. Do not rebuild. Working directory: D:/SteamLibrary/steamapps/common/Two Point Campus/ThaiCampusMod.

Goal: check whether the merged corpus opens and displays broadly readable Thai using our existing font/UI. No A/B matrix, no exhaustive translation review, no fine shaping claims.

## Boundaries and budget

One game session, Medium UI scale. Target 20 minutes active work. Three views maximum: main menu; Settings > general/audio with visible translated labels; Settings > Video with one naturally reachable translated tooltip. One screenshot per view, at most one recovery each. If target/capture or hover capability cannot be established, stop; no coordinate sweeps. Do not chase missing translations. Inspect the images once; note only obvious blank text, missing glyphs, raw placeholders/tags, clipping, or unreadable text. Unchanged English/proper names are not automatic failures. Record mixed-language examples for later triage.

Do not load an existing save, start a new game, change graphics/resolution, or overwrite saves. Gameplay coverage is DEFERRED for a separately selected save/context. Do not change preset/sliders; only set UI Scale to Medium if needed. No cache edits, force-close, source/candidate modifications, commit or push.

## Lifecycle

Establish a correct current game/capture target and supported UI controls before installation, then quit normally. With Campus closed, execute each command separately and inspect its result:

1. python tools/manage_probe.py check --probe community-merge-002 — require three original states.
2. python tools/manage_probe.py install --probe community-merge-002 — require three probe states. The manager checks staged hashes and completes original backups before writing.
3. python tools/manage_probe.py check --probe community-merge-002 — require three probe states.
4. Launch through Steam, inspect the three views only. If startup fails or any blocking defect appears, stop observation and restore. Do not attempt repairs.
5. Quit normally; confirm TPC.exe has exited.
6. python tools/manage_probe.py restore --probe community-merge-002
7. python tools/manage_probe.py check --probe community-merge-002 — require three original states. Retain backups.

Restoration is required after every installed path, even at time limit. If normal exit or restoration fails, report immediately; do not bypass guards. No need to reread all historical WOs, rehash separately, transcribe every row, or repeat existing scale tests.

## Deliverable

Write docs/qa/WO_SMOKE_MERGE_001_REPORT.md: three-row view/result table; links to original images under local/qa/WO-SMOKE-MERGE-001/; actual build/scale/capture dimensions and any resizing; blocking defects and up to five representative translation issues; compact install/restore output; approximate elapsed active time and screenshot/recovery counts. Verdict: USABLE_FOR_FURTHER_TRIAL / BLOCKED / INCONCLUSIVE. Distinguish NOT_RUN from observed PASS. Gameplay, language accuracy across corpus, fine shaping and release remain unverified. Stop and return report; no automatic follow-up testing.
