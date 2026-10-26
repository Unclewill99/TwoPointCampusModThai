# Thai logo 001 — 26 October 2026

User approved the generated preview retaining TWO POINT and replacing CAMPUS with แคมปัส, then authorized proceeding. Candidate `thai-logo-001` is installed alongside the unchanged `fresh-translation-007` translation files.

## Scope and checks

- `ui-tpc-logos_assets_all.bundle`: replace `TPC_Logo_ENG_HALF` (512 × 186).
- `ui-frontend-art_assets_all.bundle`: replace the complete large and small logos in the frontend atlas (1162 × 422 and 512 × 186). Letter animation fragments, seasonal logos and other brands remain unchanged.
- Exactly one Texture2D object changes in each bundle. All other serialized objects are byte-identical. Reloaded decoded pixels match the expected packed image exactly; unrelated atlas pixels retain their decoded values. RGBA32 avoids recompression damage; mip count is one.
- Original bundles backed up and verified under `local/backups/thai-logo-001/`. Installed hashes match the candidate manifest. The three installed translation bundles still match 007.
- Runtime: main menu directly observed with Thai logo, readable and contained, with no opaque background rectangle. Evidence: `local/qa/thai-logo-001/main-menu.png`. Initial loading screen was not captured; animation and seasonal variants have no runtime approval.
- Before launch: verified 24-file save snapshot `local/backups/gameplay-save-snapshots/20261026T121316500293Z.zip`. No campus entered or gameplay performed. Game left at main menu after user interaction was detected. No save rollback.

## Reproduce / restore

Build source: `tools/build_thai_logo_001.py`; approved PNG: `local/review/thai-logo-001/TPC_Logo_THAI-preview-001.png`; report: `reports/thai-logo-001-build.json`. The builder refuses to overwrite an existing manifest. Local inputs and bundles are not in Git.

Close the game before installing or restoring. From this project folder:

```powershell
python tools/manage_probe.py check --probe thai-logo-001
python tools/manage_probe.py install --probe thai-logo-001
# Restore just the logo bundles, preserving translation 007:
python tools/manage_probe.py restore --probe thai-logo-001
```

Existing Install_Thai_Mod.bat and Uninstall_Thai_Mod.bat still target translation 006 and do not manage the separate logo candidate. Use the commands above for this logo.
