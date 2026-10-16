# WO-VISUAL-008 REPORT

Date: 2026-10-16 (Asia/Bangkok). **Probe-008 layout trace experiment result: Tooltip content width remains UNBOUNDED (viewport-spanning horizontal expansion identical to probe-007-long); English automatic wrapping NOT_ESTABLISHED.** Serialized prefab edits (`ContentSizeFitter.m_HorizontalFit = Unconstrained` and `_rootContent.m_SizeDelta.x = 800`) did not constrain runtime width or induce wrapping. Other shared tooltips remain intact without observed regressions. English-only observation; no Thai, dictionary-breaking or ZWSP conclusion.

---

## 1. Preflight and Environment

- **Investigation Plan & Documentation:** Read [docs/qa/WO_VISUAL_008.md](file:///d:/SteamLibrary/steamapps/common/Two%20Point%20Campus/ThaiCampusMod/docs/qa/WO_VISUAL_008.md), [reports/probe-008-layout-trace.json](file:///d:/SteamLibrary/steamapps/common/Two%20Point%20Campus/ThaiCampusMod/reports/probe-008-layout-trace.json), [reports/probe-008-build.json](file:///d:/SteamLibrary/steamapps/common/Two%20Point%20Campus/ThaiCampusMod/reports/probe-008-build.json), and [local/prototype/probe-008/manifest.json](file:///d:/SteamLibrary/steamapps/common/Two%20Point%20Campus/ThaiCampusMod/local/prototype/probe-008/manifest.json) before execution.
- **Probe Composition:** Three bundles (`fonts_assets_all.bundle`, `localisation_assets_localisationenglish.bundle`, and `ui-prefabs-general_assets_all.bundle`).
- **Desktop Access & Interactive Verification:** Confirmed active interactive desktop session on `console` (`udomp`).
- **Preflight Manager Check:** `python tools/manage_probe.py check --probe probe-008` returned `original` for ALL THREE bundles (`01-check-original.txt`).
- **Installation:** `python tools/manage_probe.py install --probe probe-008` completed cleanly; post-install check confirmed `probe` state for all three files (`02-install.txt`, `03-check-installed.txt`).
- **Game Runtime Environment:**
  - Launch via Steam (`steam://run/1649080`).
  - Game build: `10.3.169253+2024-12-06.1241` (`04-english-medium.jpg`).
  - Language: English (Game & Audio).
  - UI Scale: Medium.
  - Display: Full Screen Window, native `3840 x 2160 @ 60Hz` (`05-video-resolution.jpg`).
  - Interactions strictly confined to main-menu Settings > Video; zero gameplay/save load, zero slider manipulation, zero setting modification, and zero Apply clicks.

---

## 2. Experimental Observations — Probe-008 Tooltip Layout

### 2.1 Resolution Tooltip (Long English Stimulus)
- **Evidence:** `06-resolution-tooltip.jpg` (capture resolution 1920x1080) and `06-resolution-tooltip-native.jpg` (native 3840x2160).
- **Placement:** Pointer positioned at logical window-relative coordinates `(110, 355-382)` on the Resolution row with zero-delta scroll; captured after full fade-in.
- **White Background Dimensions:**
  - Capture pixels (1920x1080): approximately `(0, 343) - (1919, 424)`, height 82 px.
  - Native pixels (3840x2160): approximately `(0, 686) - (3839, 848)`, height 163 px.
  - **Horizontal Bounding Assessment: NOT BOUNDED.** The tooltip background box continues to expand across the entire horizontal viewport width from screen edge to screen edge, exactly mirroring probe-007-long (`17-long-tooltip.jpg`). The requested 800 Unity-unit width had no visible effect on limiting the container width.
- **Text Line Count & Starts/Ends:**
  - **Observed Line Count:** Exactly 1 line of visible text at `y ≈ 382` (1920x1080).
  - **Line Start:** Left viewport boundary clips mid-sentence at `...nce with ordinary spaces.`.
  - **Middle Sequence:** Four complete visible repetitions of `This is a readable English sentence with ordinary spaces.`.
  - **Line End:** Right viewport boundary clips mid-sentence at `...with ordinary spaces.`.
  - **Automatic Wrapping Assessment: NOT_ESTABLISHED.** Zero (0) extra line breaks occurred inside the newline-free repeated middle segment.
- **Missing Source Lines:**
  - The first line (`Sets window resolution.`) and third line (`Reduce resolution to increase CPU and graphics performance.`) remain completely unrendered or pushed outside the single-line vertical bounding box, identical to probe-007-long.
- **Text Scale & Legibility:**
  - English glyph size remains standard body text size (no auto-downscaling / text squishing observed); text that falls within viewport boundaries is sharp and readable, but truncated at both horizontal extremes.

### 2.2 Shared Prefab Regressions Check (Other Settings Tooltips)
- **VSync Tooltip (`06-resolution-tooltip.jpg` / `07-maxfps-tooltip.jpg`):**
  - Text: `Synchronises the game framerate with your display's refresh rate.\nReduces screen tearing, but may increase input delay.`
  - 2 lines, bounded to content width (~270 capture px). Intact.
- **Quality Presets Tooltip (`07-maxfps-tooltip.jpg`):**
  - Text: 3 lines corresponding to explicit source newlines. Bounded to content width (~320 capture px). Intact.
- **Antialiasing Mode Tooltip (`08-antialiasing-tooltip.jpg`):**
  - Text: 4 lines corresponding to explicit source newlines. Bounded to content width (~399 capture px). Intact.
- **Regression Assessment: NO REGRESSION OBSERVED.** The serialized edits on the shared prefab did not disrupt the baseline appearance or sizing of standard multi-line tooltips using explicit newlines.

---

## 3. Comparison Between Probe-007-long and Probe-008

| Metric | Probe-007-long (`17-long-tooltip.jpg`) | Probe-008 (`06-resolution-tooltip.jpg`) | Assessment |
| :--- | :--- | :--- | :--- |
| **Prefab Modification** | None (original UI prefab) | `ContentSizeFitter.m_HorizontalFit = 0`<br>`_rootContent.m_SizeDelta.x = 800` | Applied in staged bundle |
| **White Body Bounds (1080p)** | `(0, 342) - (1919, 425)` | `(0, 343) - (1919, 424)` | **Identical (Unbounded viewport expansion)** |
| **Visible Line Count** | 1 single line | 1 single line | **Identical (No wrapping)** |
| **Repeated Middle Segment Breaks** | 0 extra breaks | 0 extra breaks | **Automatic wrapping NOT_ESTABLISHED** |
| **First/Last Source Lines** | Not visible | Not visible | **Identical** |
| **Other Tooltips Behavior** | Normal | Normal (VSync, Quality Presets, Antialiasing) | **No regression** |

---

## 4. Root-Cause Analysis & Technical Deductions

1. **Serialized Edits Overridden by Runtime Code:**
   - As documented in `reports/probe-008-layout-trace.json`, modifying serialized fields in `ui-prefabs-general_assets_all.bundle` does not prevent custom C# scripts in `GameAssembly.dll` (e.g. `TooltipController`, `LayoutWrapper`, or custom layout recalculations) from overriding `m_SizeDelta` or enabling preferred sizing at runtime.
2. **TMP Text Container Dependency:**
   - In TextMeshPro, text wrapping requires either a fixed-width RectTransform on the text component itself (`TMP_Text`), or an active layout element/container with defined maximum/preferred widths that enforces wrapping flags (`enableWordWrapping = true`). Because `_text` itself was not modified and its wrapping mode remains unchanged, the TMP component continues to calculate an unbounded single-line horizontal extent for unbroken strings.
3. **Implications for Localization:**
   - Serialized prefab tweaks to `_rootContent` alone are insufficient to enforce a maximum tooltip width.
   - Any long string without explicit newlines (including Thai text) will continue to expand horizontally off-screen unless:
     (a) Runtime C# layout logic is modified/hooked, or  
     (b) Pre-segmented text with explicit line breaks (`\n`) is provided by translation/import tooling.

---

## 5. Restoration and Hash Integrity

- **Clean Exit:** Game was closed via Settings Red X > Main Menu Quit; process termination confirmed (`TPC.exe` absent from tasklist).
- **Restoration Execution:** `python tools/manage_probe.py restore --probe probe-008` executed with 0 errors (`09-restore.txt`).
- **Post-Restoration Check:** `python tools/manage_probe.py check --probe probe-008` confirmed `original` state for ALL THREE bundles (`10-final-check.txt`).
- **Cryptographic Hash Verification (`11-final-hashes.json`):**

| Bundle Name | Manifest Original SHA-256 | Actual Installed SHA-256 | Retained Backup SHA-256 | Verification Status |
| :--- | :--- | :--- | :--- | :--- |
| `fonts_assets_all.bundle` | `33aa34892719fbc7caaabd0a292c32bb135bc61978a4cd3ce73c6c40da8f4e6e` | `33aa34892719fbc7caaabd0a292c32bb135bc61978a4cd3ce73c6c40da8f4e6e` | `33aa34892719fbc7caaabd0a292c32bb135bc61978a4cd3ce73c6c40da8f4e6e` | **MATCH (PASS)** |
| `localisation_assets_localisationenglish.bundle` | `c1e7ca97f260813ccc9a1cf463f20d066631f8e5616bf797fe8d5ae93227878f` | `c1e7ca97f260813ccc9a1cf463f20d066631f8e5616bf797fe8d5ae93227878f` | `c1e7ca97f260813ccc9a1cf463f20d066631f8e5616bf797fe8d5ae93227878f` | **MATCH (PASS)** |
| `ui-prefabs-general_assets_all.bundle` | `2152e5ba289ccb0414c462371cfdfe05cc7ac589a10a75b8b46d359afd99786d` | `2152e5ba289ccb0414c462371cfdfe05cc7ac589a10a75b8b46d359afd99786d` | `2152e5ba289ccb0414c462371cfdfe05cc7ac589a10a75b8b46d359afd99786d` | **MATCH (PASS)** |

- **Manifest SHA-256:** `df1e2cc770299d08119c37df4b50f911d146509d1ac792177c6bd70125f55199`.

---

## 6. Scope Boundaries & Compliance

- **No Code or Translation Edits:** No source JSON, scripts, or translations were modified during this run.
- **No Git Mutations:** No branch switching, commits, or pushes were performed in the shared checkout.
- **Safe Working State:** All game files are restored to clean original state. Probe backups are safely preserved in `local/backups/probe-008/`.
