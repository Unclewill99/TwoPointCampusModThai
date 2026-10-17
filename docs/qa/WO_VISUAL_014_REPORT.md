# WO-VISUAL-014 REPORT

Date: 2026-10-17 (Asia/Bangkok). Status: **BLOCKED before installation; visual coverage NOT_RUN**. This is an incomplete attempt, not acceptance. probe-013 only; no probe-014 built.

## Blockers and evidence

Read WO_VISUAL_014.md, WO_VISUAL_013_REPORT.md, PROBE_013_ACCEPTANCE.md, manifest and tooltip-map. Available documented Windows sky API supports click/drag/scroll/key input but has no hover or move-pointer method. Required bounded hover cannot be performed through that interface. No click/drag on graphics settings was used as a substitute. No game launch or installation was attempted.

Window inventory: [00-window-inventory.json](../../local/qa/WO-VISUAL-014/00-window-inventory.json) reported Campus not running. A capture requested for the returned Steam window instead showed this ChatGPT conversation. Therefore the image below is **invalid target capture**, not Steam/game/tooltip evidence. Its original filename is misleading; content inspection takes precedence. This additional capture failure prevents reliable visual verification. No app input was issued.

![Invalid target capture: returned chat image, not Steam or Campus](../../local/qa/WO-VISUAL-014/00-steam-before-test.jpg)

## Coverage matrix

All suffixes use UI/Settings/Tooltips/. NR = NOT_RUN because UI testing could not start (hover API absent and target capture incorrect). NR does not mean control absent or tooltip absent. No NOT_OBSERVED classification is justified without an actual bounded hover. Previously accepted cells below are attributed to WO-013 and were not repeated.

| Key | Medium | Small | Large |
|---|---|---|---|
| MSAASamples | Previously accepted; not repeated | NR | NR |
| AntialiasingQuality | Previously accepted; not repeated | NR | NR |
| DepthOfField | Previously accepted; not repeated | NR | NR |
| AmbientOcclusionMode | Previously accepted; not repeated | NR | NR |
| AmbientOcclusionModeQuality | Previously accepted; not repeated | NR | NR |
| CharacterDrawDistance | Previously accepted; not repeated | NR | NR |
| AnisoTextures | NR | NR | NR |
| Bloom | NR | NR | NR |
| ShadowQuality | NR | NR | NR |
| TextureQuality | NR | NR | NR |
| WorldDetail | NR | NR | NR |
| QualityPresets | NR | NR | NR |
| AnimationSkinningQuality | NR | NR | NR |
| CharacterLimits | NR | NR | NR |
| RenderScale | NR | NR | NR |
| Resolution | Previously accepted; not repeated | Previously accepted; not repeated | Previously accepted; not repeated |
| FullScreenMode | Previously accepted; not repeated | Previously accepted; not repeated | Previously accepted; not repeated |
| MaxFPS | Previously accepted; not repeated | Previously accepted; not repeated | Previously accepted; not repeated |
| AntialiasingMode | Previously accepted; not repeated | Previously accepted; not repeated | Previously accepted; not repeated |
| Vsync | Previously accepted; not repeated | Previously accepted; not repeated | Previously accepted; not repeated |

QualityPresets heading/selected-preset hover attempts: zero; activation not established. Reachability of AnimationSkinningQuality, CharacterLimits and RenderScale not observed this run. No claim that these controls are absent. CharacterLimits variables/colour untested. All requested new text accounting, bounds, line counts, LF/extra breaks, clipping, readability, containment, marks and empty-space assessments remain NOT_RUN.

## Lifecycle and final state

Commands executed sequentially in separate calls, each exit 0:

1. `python tools/manage_probe.py check --probe probe-013` — original/original/original.
2. Preflight independent hash verification — map matches manifest; all staged and retained-backup hashes match.
3. `python tools/manage_probe.py restore --probe probe-013` — original/original/original; no-op because originals already installed.
4. `python tools/manage_probe.py check --probe probe-013` — original/original/original.

Install and installed-probe check were not run because UI prerequisites failed. Existing backups retained. No source/map/build/translation edits, gameplay, graphics changes, Apply, restart, force-close, branch change, commit or push. Only report/evidence files added.

UI Scale was not changed. Previous WO-013 reports final Medium; **current persisted Medium was not independently verified in this attempt**. Build/resolution/English likewise not observed this run; previous report records build 10.3.169253+2024-12-06.1241, 3840 x 2160 @ 60hz, English. These are historical values, not current visual evidence.

## Hashes

[Independent hash evidence](../../local/qa/WO-VISUAL-014/01-hashes.json). Manifest SHA-256: `459d7e9ebc2db1cc294c25e48996e0fb8fb59054b05682a98bd6d49ea48e0075`; map SHA-256: `81d596fed3d94cfff34b011fdd5c42e46a7127bf9cfd998759920000b9953fda`.

| Bundle | Installed original and retained backup SHA-256 | Staged probe-013 SHA-256 |
|---|---|---|
| fonts_assets_all.bundle | `33aa34892719fbc7caaabd0a292c32bb135bc61978a4cd3ce73c6c40da8f4e6e` | `588f15fad01635da3fb5b86d5c3946cbb7bd85b40304364294fb23d73c207f3e` |
| localisation_assets_localisationenglish.bundle | `c1e7ca97f260813ccc9a1cf463f20d066631f8e5616bf797fe8d5ae93227878f` | `78f4ef1f44bef0425934522c27542e4df767a4f5bad344528dfbe0b0f4ae6624` |
| ui-prefabs-general_assets_all.bundle | `2152e5ba289ccb0414c462371cfdfe05cc7ac589a10a75b8b46d359afd99786d` | `b8933a120178276ca8246b1494e881ec97a20a7b9b4804b3a16cf080efeb7e14` |

Final manager check independently rehashed all three staged, installed and existing backup files successfully after the no-op restore. No new visual PASS or release approval. Resume requires working target-window capture and a supported hover operation.
