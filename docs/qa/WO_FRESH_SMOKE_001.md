# WO-FRESH-SMOKE-001 — full fresh corpus, bounded practical sample

2026-10-22. Candidate fresh-translation-004. First runtime of full fresh translation; NOT_RUN. Workdir D:/SteamLibrary/steamapps/common/Two Point Campus/ThaiCampusMod.

## Scope

One session,15-minute active observation target, max3 primary images, at most one recovery per view. Settings and campus original imported text evidence is historical, not fresh-text approval. No full matrix, no word-by-word transcription, no coordinate sweeps, tooltip hunting, on-the-fly edits or extra tests.

1. Main-menu Settings > Game: capture fresh translated selected values/labels. Check no new blank dropdowns, clipping, arrow overlap or raw tags. Record actual UI scale if visible without changing it. No dropdown opening/selection or settings change. Return to main menu.
2. Continue existing Slot1 / Freshleigh Meadows (8000.sav now exists). Capture the initial campus modal if present: heading/body/course name/dynamic number. If absent, capture paused initial HUD instead. Record exact text only for failures. Known ต่ำ mark collision and word splitting remain open: note whether seen, do not claim fixed or chase higher-detail imagery.
3. If initial modal is present, this brief permits dismissing it once using visible OK/ตกลง to expose HUD (supersedes earlier no-dismiss rule for this step only). Immediately pause with a visible control; record evidence. While paused, inspect one clearly visible read-only staff/recruitment overview showing categories อาจารย์/ผู้ช่วย/ภารโรง if naturally available, otherwise capture HUD/objective. Do not press Hire, choose a candidate, build/spend/start year, or dismiss additional tutorial chains. If pause cannot be established promptly or a modal blocks access, stop; view3 UNRESOLVED/NOT_RUN rather than forced coverage. Minor simulation time while locating pause is possible; no deliberate progression.

## Save and bundle safeguards

With Campus closed, run python tools/backup_gameplay_saves.py; require verified=true, record fresh ZIP/manifest. Existing Slot1 progress and normal auto/profile saves may update; keep live saves and backup, record changes, no automatic rollback or slot overwrite. No new career/campus/reset, save deletion or Cloud settings changes.

Then run each command separately, inspect output:
1. python tools/manage_probe.py check --probe fresh-translation-004 (three original)
2. python tools/manage_probe.py install --probe fresh-translation-004 (three probe)
3. python tools/manage_probe.py check --probe fresh-translation-004
4. Launch through Steam and perform bounded views above.
5. Exit normally using visible controls; saving current Slot1 is allowed, overwriting another slot is not. Confirm TPC.exe absent.
6. python tools/manage_probe.py restore --probe fresh-translation-004
7. python tools/manage_probe.py check --probe fresh-translation-004 (three original)

Always exit/restore after installed paths, even failures/time limit. Exit/restoration takes priority over observation budget. Retain backups. No force-close/guard bypass/font/source edits/commit/push. If normal exit/restore is blocked, report immediately rather than guessing.

## Report

Write docs/qa/WO_FRESH_SMOKE_001_REPORT.md with original images under local/qa/WO-FRESH-SMOKE-001/. Up to3 view/result rows, actual build/settings/capture resizing/pause/campus, visible failures and at most5 language issues, elapsed time/counts, fresh save backup and changed/new/missing file hash summary, compact three-bundle lifecycle results. Unreached UI stays NOT_RUN. Verdict NO_NEW_BLOCKER_IN_SAMPLE / NEW_BLOCKER / SETUP_LIMIT / INCONCLUSIVE. Known renderer defects and pending terminology must remain explicit even if no NEW blocker. No full corpus/gameplay/fine-shaping approval from this sample. Stop after report.
