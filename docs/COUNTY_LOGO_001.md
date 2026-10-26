# TWO POINT เคาน์ตี — 26 October 2026

User requested replacing COUNTY with Thai while retaining TWO POINT in English. Used the Thai transliteration **เคาน์ตี**, cyan/blue fill and black outline. `county-logo-001` is installed independently of translation 007, thai-logo-001 and news-thai-001.

- Source: `local/review/county-logo-001/TwoPointCounty-thai.png` (built-in imagegen, genuine alpha transparency).
- Target: `ui-art-mainmenu_assets_all.bundle`, Texture2D `TwoPointCounty_logo`, path ID `-3724424202125531811`, 512 × 186.
- Built with `tools/build_county_logo_001.py`; exact decoded-pixel readback passed. Only the target texture object changed; every other serialized object, including sprite metadata, is byte-identical. RGBA32, one mip.
- Original bundle backed up under `local/backups/county-logo-001/`. Installed bundle hash matches the candidate manifest. Full hashes are recorded in `reports/county-logo-001-build.json`.
- Runtime PASS_SCOPED: main-menu account panel shows TWO POINT เคาน์ตี, readable, contained, transparent background. Status and logout button remain visible. Evidence `local/qa/county-logo-001/main-menu.png`. No account action, gameplay or UI scale change. Game exited normally after capture. Other account screens and UI scales not tested.
- Verified 24-file save snapshot before launch: `local/backups/gameplay-save-snapshots/20261026T123446907756Z.zip`.

Close the game before changing files. From ThaiCampusMod:

```powershell
python tools/manage_probe.py check --probe county-logo-001
python tools/manage_probe.py install --probe county-logo-001
python tools/manage_probe.py restore --probe county-logo-001
```

Restore affects only this logo bundle. Install_Thai_Mod.bat / Uninstall_Thai_Mod.bat (updated 2026-10-26 evening) also install/restore this candidate together with 007, thai-logo-001 and news-thai-001. Retain local prototype, original backup and generated image; they are not in Git.

Imagegen prompt: replace only COUNTY with exactly เคาน์ตี, retaining TWO POINT and the mountain/2 emblem in white; match chunky cyan/blue letters, pale cyan bevel, dark blue lower shadow, thick black outline; wide two-row layout, readable diacritics, genuine transparent background, no extra elements.
