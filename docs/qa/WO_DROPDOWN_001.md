# WO-DROPDOWN-001 — one-caption font diagnostic

Date: 2026-10-21. Candidate: community-merge-003. Runtime NOT_RUN. Working directory D:/SteamLibrary/steamapps/common/Two Point Campus/ThaiCampusMod. Ready for Antigravity/user relay.

Purpose: test direct Thai primary-font/material on LogLevel selected caption only. Every other dropdown is intentionally unchanged and may remain blank. Do not claim broad fix or confirmed root cause from one positive result. Localisation and font bundle identical to merge-002. UI reload verification changed only caption object 295032210435112665; two fields m_fontAsset/m_sharedMaterial. No font size, wrapping, rect, translation or item-template change.

Budget: 10 minutes active observation; one session; Settings > Game only. Capture one primary image showing LogLevel plus adjacent unchanged dropdowns, one recovery maximum. No sweeps, no tooltip, no dropdown opening or selecting values, no save loading, no graphic/preset changes. If correct target/navigation cannot be established within recovery cap, stop and report INCONCLUSIVE. Use main menu Settings button identified by text, not remembered coordinates. Do not accidentally enter Mods. Medium is expected but do not infer it from blank UI Scale caption; report uncertainty if not directly verified.

With Campus closed, run each command separately and inspect output:

1. python tools/manage_probe.py check --probe community-merge-003 (require three original)
2. python tools/manage_probe.py install --probe community-merge-003 (require three probe; manager validates hashes/backups)
3. python tools/manage_probe.py check --probe community-merge-003
4. Launch via Steam. Open Settings > Game. Observe LogLevel selected caption: visible Thai/ASCII/blank; readability, clipping, apparent size versus labels. Note nearby unchanged dropdown state as within-screen comparison. Do not select an option or repair anything.
5. Quit normally; confirm TPC.exe exited.
6. python tools/manage_probe.py restore --probe community-merge-003
7. python tools/manage_probe.py check --probe community-merge-003 (require three original)

Always exit and restore after installation, including failure/time limit. Restoration is outside the observation cap and takes priority. Do not force-close or bypass guards; report inability to restore. Keep backups. No rebuild/source edits/commit/push. Do not expand to Video or all 19 controls.

Report docs/qa/WO_DROPDOWN_001_REPORT.md with original image links under local/qa/WO-DROPDOWN-001/, brief result DIRECT_FONT_VISIBLE / STILL_BLANK / INCONCLUSIVE, actual environment/capture dimensions/resizing, installed/restored states, elapsed time and capture count. Fine shaping remains unverified. Stop after report; Controller decides next patch.
