# WO-VISUAL-010 retry — same probe, repaired process check

Date: 2026-10-16. Follow original WO_VISUAL_010.md with these amendments. Previous attempt BLOCKED before mutation; no rendering result. Probe bundles/manifest unchanged.

manage_probe.py now uses Windows Toolhelp process enumeration instead of tasklist. It aborts on enumeration errors and still refuses mutation if TPC.exe is present. Controller verified enumeration succeeds while Campus is closed, and all three originals. Do not remove this guard or force-close unsaved gameplay.

Run every step sequentially and inspect the exit code AND returned three-file states before proceeding. In particular, never dispatch Steam launch in the same orchestration block as installation: wait for successful install and installed hash check first. If a command fails, stop; do not launch game or run restore blindly. Read-only check determines actual file state; unchanged originals do not require restoration.

Use --probe probe-010 throughout. Follow original English test and three-file restore steps. Save retry evidence separately under local/qa/WO-VISUAL-010/retry/ and append a dated retry section to WO_VISUAL_010_REPORT.md; preserve the previous BLOCKED history. Record original for all three after successful restore. No commit/push or in-session experiment edits. If environment still blocks process enumeration, report BLOCKED rather than using a bypass.
