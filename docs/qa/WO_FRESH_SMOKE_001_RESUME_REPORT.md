# Fresh smoke resume — 2026-10-22 (Asia/Bangkok)

Candidate: fresh-translation-004, unchanged. Verdict: NO_NEW_BLOCKER_IN_SAMPLE, with staff coverage NOT_RUN. This is a bounded sample, not full corpus, gameplay or shaping approval.

## Original-game capability gate

Three originals verified with manage_probe.py. Game initially closed. Launched via Steam Library Play. Computer Use selected the unique returned window owned by process:D:\SteamLibrary\steamapps\common\Two Point Campus\TPC.exe, activated it, and observed actual game pixels. Settings > Game reached on first navigation attempt; Medium UI scale, English language. No values changed. Evidence: local/qa/WO-FRESH-SMOKE-001-RESUME/original-settings.png. No input recovery needed; minimized Steam was activated before inspection. qa_driver.py was not used, so this does not establish its live verification.

Original game exited via Quit. Backup guard confirmed no TPC process, then saved and verified 10 files in local/backups/gameplay-save-snapshots/20261022T141412624342Z.zip with matching JSON manifest.

## Installed sample

Install and separate check confirmed all three probe bundles. Relaunched via Steam, selected fresh process-owned window (new window ID). Build visible: 10.3.169253+2024-12-06.1241. Captures returned at 1920x1080; no additional resizing. Observation approximately four minutes, below 15-minute cap; three retained primary images. No coordinate sweeps, setting changes, recruitment, building, spending or year start.

| View | Observation | Evidence |
|---|---|---|
| Settings > Game | Medium scale; selected dropdown values and labels visible. No blank selected values, arrow overlap, raw tags or obvious clipping in sampled area. Dropdowns not opened. | 01-thai-settings.png |
| Freshleigh Meadows initial modal | Heading/body/course and intake 10 visible; no obvious blank text or raw tags. Known ต่ำ shaping remains open; no fine-shaping clearance. | 02-campus-modal.png |
| Paused HUD | Dismissed initial modal once using ตกลง. Clicked visible pause; red border and pause indicator confirmed. Albert Crank tutorial appeared and blocked staff access. Staff categories NOT_RUN; tutorial chain not advanced. | 03-paused-tutorial-hud.png |

Evidence directory: local/qa/WO-FRESH-SMOKE-001-RESUME/.

Menu still uses ม็อด and ต่อไป: known pending Mod integration and Continue wording review, not new blockers. No new language issue assigned from this sample. BUG-THAI-002/003 remain OPEN; BUG-THAI-001 broader regression tracking remains open.

## Exit, restore and save comparison

Escape did not open menu while tutorial was present. Alt+F4 requested normal window closure (no force termination); subsequent manager process guard allowed restoration. Restore and independent check confirmed original/original/original. No automatic save rollback.

Compared all snapshot files with live files: six changed (career.csav, career.csav.2.bak through .5.bak, userprofile.sav); one new career.csav.6.bak; none missing. Campus 8000.sav unchanged. Full machine-readable comparison retained at evidence directory/save-comparison.json. Minor simulation time occurred between modal dismissal and pause. Retain live saves and verified backup.

No candidate edits, commit, push or external agent dispatch. Work stopped after this bounded report as required by the brief.
