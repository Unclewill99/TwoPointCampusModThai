# WO-SARA-AM-002-AB — atomic/decomposed text × mark pair

2026-10-22. Assigned Antigravity Desktop QA. READY_FOR_HANDOFF; execution/receipt not confirmed. Controller does no screen testing.

## Question and staged inputs

Workdir D:/SteamLibrary/steamapps/common/Two Point Campus/ThaiCampusMod. Read BUG_THAI_003.md, ../SARA_AM_001_REFERENCE_ACCEPTANCE.md, ../SARA_AM_002_NATIVE_FINDINGS.md. Base fresh-translation-005 frozen. Two diagnostic-only candidates:

- probe-sara-am-001a: unchanged 005 font/UI, one intro text record replaced with three short diagnostic lines.
- probe-sara-am-001b: identical diagnostic localisation/UI, plus one TMP MarkToMark record for nikkhahit glyph59 -> mai-ek glyph42 using embedded font GPOS anchors. No global glyph shift, source-font-byte change, or production corpus edit.

Use reports/sara-am-001-build.json and each local/prototype/<candidate>/manifest.json for all three expected hashes. Manager supports both exact names. Do not rebuild or alter specimens.

Both variants show these rows in I2LS_Levels segment533:

| Row | Specimen | Exact codepoints of target word |
|---|---|---|
| A | atomic ต่ำ then ถี่ control | 0E15 0E48 0E33 |
| B | reordered decomposed then ถี่ | 0E15 0E4D 0E48 0E32 |
| C | original-order decomposed then ถี่ | 0E15 0E48 0E4D 0E32 |

These are explicitly temporary Unicode diagnostic specimens, NOT approved replacement translations. Preserve original ต่ำ case. Browser reference establishes expected atomic/reordered separation; original-order browser stacking differs. Do not silently rename/swap row labels.

## Execution scope

Maximum 15 minutes active across both variants, max two primary native PNG images (one initial modal per variant), one recovery total. No extra original-game reproduction. Backup before each variant with game closed. Launch via Steam, verify unique owner path TPC.exe in Campus folder, foreground and fresh actual pixels. Use explicit capture/input coordinate mapping and visually identified Continue, not color-band indexes or prior coordinates. Do not change Settings, UI scale, build/spend/hire/start year or advance tutorials.

Continue existing Slot1 / Freshleigh Meadows only; on campaign card select visible Continue, never Restart/New Game. Allow intro cutscene to complete naturally. Capture opening course-information modal without pressing OK. Confirm diagnostic A/B/C lines actually appear before interpreting font result. If they do not, mark BINDING_UNCONFIRMED and stop, no hunting other UI. Modal has not yet been proven to use these specific prefab instances at runtime.

Record scale if known without changing it; native screenshot dimensions. Inspect target mark separation/stacking per row and ถี่ control; note absent marks/tofu, overlap, clipping. No automatic PASS from readable body. Compare exact row across variants and to existing same-font reference. Keep original full images; labeled native crops/enlargements allowed only as derived analysis with interpolation/scale noted, no extra game captures. Different engines/sizes prohibit pixel-equality claims.

Do not dismiss initial modal. End each variant using normal close request Alt+F4/WM_CLOSE. If normal close is blocked, stop/report immediately; no forced termination or guard bypass.

## Bundle/save lifecycle — separately for a then b

With game closed, run commands separately, inspect each output (substitute exact variant name):

1. `python tools/manage_probe.py check --probe probe-sara-am-001a` requires original/original/original.
2. `python tools/backup_gameplay_saves.py` requires verified=true; record ZIP/manifest.
3. `python tools/manage_probe.py install --probe probe-sara-am-001a`.
4. `python tools/manage_probe.py check --probe probe-sara-am-001a` requires probe/probe/probe.
5. Launch/observe/normal exit as above; confirm TPC.exe absent.
6. `python tools/manage_probe.py restore --probe probe-sara-am-001a`.
7. `python tools/manage_probe.py check --probe probe-sara-am-001a` requires three originals.

Repeat with probe-sara-am-001b only after successful restore/check and capability remains usable. Never install b over a. Exit/restore always takes priority, including time/setup failures. Compare save hashes changed/new/missing after each variant; retain live saves and backup, no rollback, deletion or Steam Cloud changes. No commit/push.

## Report and interpretation

Deliver docs/qa/WO_SARA_AM_002_AB_REPORT.md, native PNGs local/qa/WO-SARA-AM-002-AB/. Include candidate/hash, exact row codepoints, build/scale/dimensions/mapping, 2×3 row observations plus ถี่ control, elapsed/recovery, bundle lifecycle and save comparison. Verdict DIAGNOSTIC_RESULT / SETUP_LIMIT / BINDING_UNCONFIRMED / INCONCLUSIVE. No fix/global-font/full-corpus approval.

If only decomposed row B improves with added pair, that supports placement-table contribution for decomposed sequence, not an atomic ต่ำ fix or permission to rewrite corpus. If atomic row A improves, record result for Controller without inferring engine internals. No effect is useful data, not reason to keep tweaking during run. Stop after report.
