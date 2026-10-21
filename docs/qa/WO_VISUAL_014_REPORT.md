> Latest result (2026-10-18): desktop run completed; 27 new Video cells observed, plus CharacterLimits at all scales. QualityPresets NOT_OBSERVED; AnimationSkinningQuality/RenderScale NOT_RUN. Final Medium and all THREE original verified. See “Completed desktop run” below; earlier BLOCKED entries are preserved history.

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

## Resume retry — 2026-10-17 (Asia/Bangkok)

**Capability BLOCKED before installation; all new WO-014 visual cells remain NOT_RUN.** Previous history above preserved. Read WO_VISUAL_014_RESUME.md and WO_VISUAL_014.md before attempting the capability gate.

Current computer-use skill read from `C:/Users/udomp/.codex/plugins/cache/openai-bundled/computer-use/26.1013.40934/skills/computer-use/SKILL.md`, together with its current docs/api.md, guidance.md and confirmations.md. The documented sky window2 interface supports Windows native windows (`target: windows`), so browser-only access was not used. Current API documents coordinate-based scroll input; it does not document an explicit hover/move method. No assumption was made that previous zero-delta scroll behavior proves current non-mutating pointer placement. That capability remains UNVERIFIED because capture verification failed first; no pointer-placement test was attempted.

Fresh inventory in `local/qa/WO-VISUAL-014/retry/00-window-inventory.json` returned exactly one Steam window: id 133146, process steamwebhelper.exe. No Campus window was returned. Selected that returned window via get_window and requested get_window_state. Inspected image content: the returned image shows this ChatGPT conversation, NOT Steam. Requested id/title are therefore insufficient evidence of correct target capture. Saved original returned image as `retry/01-invalid-target-chat-not-steam.jpg`; it is explicitly invalid target evidence, not a tooltip screenshot.

Gate status:

| Gate | Retry observation |
|---|---|
| Documented Windows native support | Present in current API |
| Fresh target inventory | Obtained, unique Steam window |
| Screenshot content matches selected Steam | FAIL: chat content returned |
| Documented non-mutating pointer placement established | UNVERIFIED; no input attempted after failed capture |
| Permission to proceed to installation under resume gate | Not reached |

Stopped at the user's required capability gate. No activate/click/scroll/key/drag/other app input, game launch, install or restore issued in this retry. No blind control operation or native-script bypass. No need for no-op restore: originals were unchanged and verified read-only. No scale change; current English/Medium/build/resolution were NOT observed. Historical WO-013 settings are not asserted as current facts.

All requested new Medium/Small/Large cells in the earlier coverage matrix remain NOT_RUN due to failed preflight, including both QualityPresets bounded attempts (zero attempts this retry). No NOT_OBSERVED tooltip/control-absence claim follows. No primary matrix repetition, new visual PASS, text-boundary/mark/readability assessment, reachability or variable-substitution conclusion.

`python tools/manage_probe.py check --probe probe-013` ran after stopped UI preflight: exit 0, original/original/original (`retry/02-original-check.txt`). Independent actual SHA-256 checks in `retry/03-final-hashes.json` confirm all THREE installed originals, retained original backups and staged probe-013 candidates against manifest; map also matches. Original hashes are the same three listed in the original Hashes section. Manifest remains `459d7e9ebc2db1cc294c25e48996e0fb8fb59054b05682a98bd6d49ea48e0075`; map remains `81d596fed3d94cfff34b011fdd5c42e46a7127bf9cfd998759920000b9953fda`.

Final state **original/original/original**, backups retained. No commit/push, branch switch, code/map/translation edit or asset upload. Retry evidence is separate under `local/qa/WO-VISUAL-014/retry/`. Resume still requires correct current Steam capture and established supported non-mutating pointer placement, or user-performed documented manual hover/capture on a capable desktop.


## Controller-session capability retry — 2026-10-17

BLOCKED before installation. Read current computer-use skill/guidance/API/confirmations and WO_VISUAL_014_RESUME.md. Initialized @oai/sky via node_repl; list_windows returned Steam and ChatGPT. Selected the unique returned Steam window (id 133146), obtained a fresh get_window binding and captured state. Image showed the current ChatGPT conversation instead of Steam. Repeated fresh inventory/selection/capture once: same wrong-target image. Images were inspected directly in tool results, not reused as game evidence. No input, activation, pointer placement, launch, install or restore performed. Stopped per capability gate.

Current documented API includes coordinate-based scroll, but no non-mutating hover capability was exercised/verified because correct capture failed first. This retry does not establish universal absence of hover. No UI Scale/build/resolution observed. Read-only manage_probe check --probe probe-013 independently returns original for all THREE. No files required restoration. New visual coverage remains NOT_RUN, prior WO-013 acceptance unchanged. Machine-readable observations: local/qa/WO-VISUAL-014/retry/controller-capability-retry.json. No commit/push.


## Completed desktop run — 2026-10-18 (Asia/Bangkok)

**Coverage follow-up executed with unchanged probe-013. Restoration PASS: all THREE original; UI Scale returned to Medium.** Earlier BLOCKED attempts above remain historical. This run adds 27 requested Video tooltip cells (5 Medium + 11 Small + 11 Large), plus naturally exposed CharacterLimits observations at all scales. QualityPresets remains NOT_OBSERVED at Medium; AnimationSkinningQuality and RenderScale remain NOT_RUN/control not exposed. No all-20 or release approval.

### Capability and actual environment

Read current Computer Use skill, guidance/API/confirmations, WO-014/resume, WO-013 report, PROBE_013_ACCEPTANCE, manifest and tooltip-map. Windows native API worked. A capture initially included the foreground chat over the game; fresh inventory/get_window/activate_window recovered a correct unobscured game capture before any game control input. Steam was separately selected and visually verified ([02-steam-verified.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/02-steam-verified.jpg)). Non-mutating pointer placement was established this session using the documented coordinate-based sky.scroll API with scrollX=0 and scrollY=0 on empty game background: pointer visibly moved to (800,150), no control activated ([00-pointer-placement-game.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/00-pointer-placement-game.jpg)). Subsequent bounded label hovers produced actual Thai tooltips; no guessed hover API or native-input script was used.

The game opened during the preceding user-requested launch capability check with originals. It was closed normally using Quit before installation. Launcher calls sometimes reported no targetable window before the app appeared; fresh inventory found it, and visual selection/activation was used. These messages were not treated as launch success or permission to send blind input.

Current build 10.3.169253+2024-12-06.1241 ([03-menu-build.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/03-menu-build.jpg)); English, initial Medium ([M-setting.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/M-setting.jpg)); Full Screen Window, 3840 x 2160 @ 60hz, VSync On, Unlimited, SMAA ([M-video.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/M-video.jpg)). These are current observations. Returned screenshots are 1920 x 1080, saved as original returned image bytes, without cropping, resizing or annotation. Capture size does not prove render resolution. Fine native-resolution shaping/mark attachment remains outside evidence detail.

Scale path Medium -> Small -> Large -> Medium, proven by [M-setting.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/M-setting.jpg), [S-setting.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/S-setting.jpg), [L-setting.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/L-setting.jpg), [R-medium.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/R-medium.jpg). Main-menu Settings only. No Apply, graphics dropdown selection, slider/limit toggle, gameplay, save load, force-close, restart experiment or repeated primary tooltip test. Only UI Scale changed. No code, source, map, build or staged candidate edits during testing; only evidence saved. Report written after normal exit/restoration.

### Requested coverage matrix

Exact prefix is UI/Settings/Tooltips/. P13 = accepted previously in WO-013, deliberately not repeated. PASS = complete source content, readable, contained box, no visible missing glyph or isolated base/mark/leading-vowel boundary at available capture detail. It is not native shaping or glossary approval.

| Key | Medium | Small | Large |
|---|---|---|---|
| MSAASamples | P13; not repeated | PASS [S-MSAASamples.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/S-MSAASamples.jpg) | PASS [L-MSAASamples.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/L-MSAASamples.jpg) |
| AntialiasingQuality | P13; not repeated | PASS [S-AntialiasingQuality.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/S-AntialiasingQuality.jpg) | PASS [L-AntialiasingQuality.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/L-AntialiasingQuality.jpg) |
| DepthOfField | P13; not repeated | PASS [S-DepthOfField.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/S-DepthOfField.jpg) | PASS [L-DepthOfField.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/L-DepthOfField.jpg) |
| AmbientOcclusionMode | P13; not repeated | PASS [S-AmbientOcclusionMode.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/S-AmbientOcclusionMode.jpg) | PASS [L-AmbientOcclusionMode.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/L-AmbientOcclusionMode.jpg) |
| AmbientOcclusionModeQuality | P13; not repeated | PASS [S-AmbientOcclusionModeQuality.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/S-AmbientOcclusionModeQuality.jpg) | PASS [L-AmbientOcclusionModeQuality.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/L-AmbientOcclusionModeQuality.jpg) |
| CharacterDrawDistance | P13; not repeated | PASS [S-CharacterDrawDistance.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/S-CharacterDrawDistance.jpg) | PASS [L-CharacterDrawDistance.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/L-CharacterDrawDistance.jpg) |
| AnisoTextures | PASS [M-AnisoTextures.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/M-AnisoTextures.jpg) | PASS [S-AnisoTextures.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/S-AnisoTextures.jpg) | PASS [L-AnisoTextures.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/L-AnisoTextures.jpg) |
| Bloom | PASS [M-Bloom.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/M-Bloom.jpg) | PASS [S-Bloom.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/S-Bloom.jpg) | PASS [L-Bloom.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/L-Bloom.jpg) |
| ShadowQuality | PASS [M-ShadowQuality.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/M-ShadowQuality.jpg) | PASS [S-ShadowQuality.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/S-ShadowQuality.jpg) | PASS [L-ShadowQuality.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/L-ShadowQuality.jpg) |
| TextureQuality | PASS [M-TextureQuality.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/M-TextureQuality.jpg) | PASS [S-TextureQuality.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/S-TextureQuality.jpg) | PASS [L-TextureQuality.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/L-TextureQuality.jpg) |
| WorldDetail | PASS [M-WorldDetail.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/M-WorldDetail.jpg) | PASS [S-WorldDetail.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/S-WorldDetail.jpg) | PASS [L-WorldDetail.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/L-WorldDetail.jpg) |
| QualityPresets | NOT_OBSERVED; heading and selected Very High each hovered once | NOT_RUN; activation not established at Medium | NOT_RUN; activation not established at Medium |
| AnimationSkinningQuality | NOT_RUN/control not exposed | NOT_RUN/control not exposed | NOT_RUN/control not exposed |
| CharacterLimits | Observed naturally; see below | Observed naturally; see below | Observed naturally; see below |
| RenderScale | NOT_RUN/control not exposed | NOT_RUN/control not exposed | NOT_RUN/control not exposed |
| Resolution | P13 | P13 | P13 |
| FullScreenMode | P13 | P13 | P13 |
| MaxFPS | P13 | P13 | P13 |
| AntialiasingMode | P13 | P13 | P13 |
| Vsync | P13 | P13 | P13 |

QualityPresets: heading hover/wait then one fresh capture ([M-QualityPresets-heading-NOT_OBSERVED.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/M-QualityPresets-heading-NOT_OBSERVED.jpg)); existing selected Very High hover for 1.8s then one capture ([M-QualityPresets-selected-NOT_OBSERVED.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/M-QualityPresets-selected-NOT_OBSERVED.jpg)). Neither shows a tooltip. No click, preset change or prolonged chase. Small/Large intentionally not attempted under the conditional requirement.

Video was scrolled from initial Basic Settings through Advanced Settings to the bottom (World Detail); no AnimationSkinningQuality or RenderScale control naturally appeared. This is scoped main-menu reachability only, not proof those controls never exist. [M-video.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/M-video.jpg), [S-bottom-controls.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/S-bottom-controls.jpg), and the per-key lower-list images document the exposed list. No graphics changes were made to reveal additional controls.

### Per-cell text and bounds

Bounds are approximate capture pixels, body excluding triangle, expressed x range; y range. Actual scroll positions differ. Rows / source LF / extra runtime breaks are separate. Each image was inspected for content and identifying label, not accepted from its filename.

| Key | Scale | Image | Rows / LF / extra | Approximate body bounds | Result |
|---|---|---|---|---|---|
| MSAASamples | S | [S-MSAASamples.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/S-MSAASamples.jpg) | 2 / 0 / 1 | 783..1129; 369..431 | PASS |
| MSAASamples | L | [L-MSAASamples.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/L-MSAASamples.jpg) | 2 / 0 / 1 | 1043..1505; 443..525 | PASS |
| AntialiasingQuality | S | [S-AntialiasingQuality.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/S-AntialiasingQuality.jpg) | 2 / 1 / 0 | 783..1129; 314..379 | PASS |
| AntialiasingQuality | L | [L-AntialiasingQuality.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/L-AntialiasingQuality.jpg) | 2 / 1 / 0 | 1043..1505; 370..456 | PASS |
| DepthOfField | S | [S-DepthOfField.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/S-DepthOfField.jpg) | 3 / 1 / 1 | 783..1129; 621..710 | PASS |
| DepthOfField | L | [L-DepthOfField.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/L-DepthOfField.jpg) | 3 / 1 / 1 | 1043..1505; 780..899 | PASS |
| AmbientOcclusionMode | S | [S-AmbientOcclusionMode.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/S-AmbientOcclusionMode.jpg) | 5 / 3 / 1 | 783..1129; 439..573 | PASS |
| AmbientOcclusionMode | L | [L-AmbientOcclusionMode.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/L-AmbientOcclusionMode.jpg) | 5 / 3 / 1 | 1043..1505; 537..716 | PASS |
| AmbientOcclusionModeQuality | S | [S-AmbientOcclusionModeQuality.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/S-AmbientOcclusionModeQuality.jpg) | 4 / 2 / 1 | 783..1129; 505..614 | PASS |
| AmbientOcclusionModeQuality | L | [L-AmbientOcclusionModeQuality.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/L-AmbientOcclusionModeQuality.jpg) | 4 / 2 / 1 | 1043..1505; 624..771 | PASS |
| CharacterDrawDistance | S | [S-CharacterDrawDistance.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/S-CharacterDrawDistance.jpg) | 4 / 2 / 1 | 783..1129; 765..886 | PASS |
| CharacterDrawDistance | L | [L-CharacterDrawDistance.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/L-CharacterDrawDistance.jpg) | 4 / 2 / 1 | 1043..1505; 714..874 | PASS |
| AnisoTextures | M | [M-AnisoTextures.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/M-AnisoTextures.jpg) | 4 / 2 / 1 | 939..1356; 655..797 | PASS |
| AnisoTextures | S | [S-AnisoTextures.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/S-AnisoTextures.jpg) | 4 / 2 / 1 | 783..1129; 660..779 | PASS |
| AnisoTextures | L | [L-AnisoTextures.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/L-AnisoTextures.jpg) | 4 / 2 / 1 | 1043..1505; 573..731 | PASS |
| Bloom | M | [M-Bloom.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/M-Bloom.jpg) | 2 / 1 / 0 | 939..1356; 834..912 | PASS |
| Bloom | S | [S-Bloom.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/S-Bloom.jpg) | 2 / 1 / 0 | 783..1129; 580..645 | PASS |
| Bloom | L | [L-Bloom.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/L-Bloom.jpg) | 2 / 1 / 0 | 1043..1505; 725..812 | PASS |
| ShadowQuality | M | [M-ShadowQuality.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/M-ShadowQuality.jpg) | 3 / 2 / 0 | 939..1356; 627..735 | PASS |
| ShadowQuality | S | [S-ShadowQuality.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/S-ShadowQuality.jpg) | 3 / 2 / 0 | 783..1129; 409..499 | PASS |
| ShadowQuality | L | [L-ShadowQuality.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/L-ShadowQuality.jpg) | 3 / 2 / 0 | 1043..1505; 496..615 | PASS |
| TextureQuality | M | [M-TextureQuality.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/M-TextureQuality.jpg) | 3 / 1 / 1 | 939..1356; 736..843 | PASS |
| TextureQuality | S | [S-TextureQuality.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/S-TextureQuality.jpg) | 3 / 1 / 1 | 783..1129; 728..817 | PASS |
| TextureQuality | L | [L-TextureQuality.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/L-TextureQuality.jpg) | 3 / 1 / 1 | 1043..1505; 664..783 | PASS |
| WorldDetail | M | [M-WorldDetail.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/M-WorldDetail.jpg) | 4 / 2 / 1 | 939..1356; 800..941 | PASS |
| WorldDetail | S | [S-WorldDetail.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/S-WorldDetail.jpg) | 4 / 2 / 1 | 783..1129; 820..937 | PASS |
| WorldDetail | L | [L-WorldDetail.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/L-WorldDetail.jpg) | 4 / 2 / 1 | 1043..1505; 787..943 | PASS |

All 27 Video cells account for first, middle and last source segments. The actual observed rows are recorded in [93-observed-rows.json](../../local/qa/WO-VISUAL-014/retry/2026-10-18/93-observed-rows.json), manually transcribed from the inspected captures then compared against the map ignoring whitespace only. All comparisons matched; trailing source spaces cannot be visually distinguished. Observed segmentation is the same at the tested scales for each key; Medium of the six previously accepted keys was not retested.

Exact extra runtime boundaries (slash denotes the observed line boundary, not a source LF):

- MSAASamples: รอยหยัก / หรือลดจำนวนลงเพื่อเพิ่มประสิทธิภาพกราฟิก
- DepthOfField: เปิด Depth of Field / ซึ่งจะทำให้ส่วนใกล้และส่วนไกลของฉากเบลอเล็กน้อย
- AmbientOcclusionMode: เปิด Ambient Occlusion / เพื่อเพิ่มคุณภาพของแสงในมุมมืด
- AmbientOcclusionModeQuality: คุณภาพระดับต่ำทำให้ภาพดูดีไม่เท่า / แต่จะช่วยเพิ่มประสิทธิภาพ
- CharacterDrawDistance: ระยะแสดงผลที่สูงขึ้นทำให้ตัวละครยังอยู่ในมุมมองได้ในระยะ / ไกลขึ้น
- AnisoTextures: เปิด Anisotropic Filtering กับเท็กซ์เจอร์ทั้งหมด / หรือเลือกเปิดกับบางเท็กซ์เจอร์เท่านั้นก็ได้
- TextureQuality: ลดรายละเอียดเท็กซ์เจอร์เพื่อเพิ่มประสิทธิภาพกราฟิก / โดยเฉพาะหากหน่วยความจำวิดีโอมีน้อย
- WorldDetail: ระดับรายละเอียดฉากที่สูงขึ้นจะคงรายละเอียดไว้ในระยะมอง / ที่ไกลขึ้น

Bloom, ShadowQuality and AntialiasingQuality use source LF only, not new automatic-wrap evidence. No observed line boundary strands เ/แ/โ/ใ/ไ or a combining mark. ไกลขึ้น and ที่ไกลขึ้น retain their vowels/consonants. No missing-glyph square or cut last row observed. All Video bodies remain inside the viewport, with readable identifying controls and visible box padding; no text overlaps the white border. Small text remains readable at capture detail. Short centered continuation rows (especially CharacterDrawDistance and WorldDetail) leave conspicuous unused width; short Bloom/AntialiasingQuality rows also leave side padding. This is a shared-width layout tradeoff, not lost content. No ZWSP or manual newline edit was made.

### Naturally exposed CharacterLimits

The Game settings list was scrolled normally to its bottom; Increase Character Limits appeared with Off selected. No toggle was clicked. Evidence: [S-game-bottom.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/S-game-bottom.jpg), [S-CharacterLimits.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/S-CharacterLimits.jpg), [L-CharacterLimits.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/L-CharacterLimits.jpg), [M-CharacterLimits.jpg](../../local/qa/WO-VISUAL-014/retry/2026-10-18/M-CharacterLimits.jpg). Medium observation was taken on the return to Medium, after Small/Large, because the control was discovered during the Small reachability observation.

Actual variable substitutions visible at all scales: STAFF_COUNT_LIMIT=150, STUDENT_COUNT_LIMIT=300, STAFF_COUNT_UNLIMITED=300, STUDENT_COUNT_UNLIMITED=600. No literal brace token or raw color tag appears. The warning is visibly red; preceding descriptions/counts are black. These are displayed values, not functional limit tests or fabricated substitutions.

All source descriptive/count/warning text is accounted for after those substitutions; source blank/tab rows create vertical spacing. There are 8 non-empty rendered lines: closed-state introduction; two counts; open-state introduction; two counts; warning label; remaining warning sentence. The final warning source segment wraps after “คำเตือน:” at every scale; this is one extra break beyond source formatting, not an inserted LF. The displayed final row is “การเกินขีดจำกัดปกติจะส่งผลเสียต่อประสิทธิภาพของเกม”. Bounds approximately Small (767,734)..(1113,1023), Medium (924,696)..(1340,1046), Large (1027,671)..(1489,1059). All fit on screen, Large ending about 21 capture pixels above the bottom. No clipping/missing glyph/isolated mark observed at capture detail. Large blank vertical gaps reflect source formatting; no claim of ideal space efficiency. Medium requested reachability observation is fulfilled; the additional naturally visible tooltip is recorded without expanding into gameplay.

### Lifecycle, hashes and final state

Every manager command ran separately with --probe probe-013, exit 0, with its result inspected before proceeding:

1. check: original/original/original.
2. Independent manifest/map/staged verification: [01-input-hashes.json](../../local/qa/WO-VISUAL-014/retry/2026-10-18/01-input-hashes.json).
3. install: probe/probe/probe.
4. check: probe/probe/probe; only afterward launched via the returned Steam game app identifier in a later call.
5. After Medium return, Settings X then Quit; [90-after-quit-windows.json](../../local/qa/WO-VISUAL-014/retry/2026-10-18/90-after-quit-windows.json) confirms Campus window absent.
6. restore: original/original/original.
7. check: original/original/original.
8. Independent SHA-256 verification of all three installed files, retained backups and staged candidates: [92-final-hashes.json](../../local/qa/WO-VISUAL-014/retry/2026-10-18/92-final-hashes.json), all matched manifest. Map/manifest hashes remain identical to the original Hashes section above. Existing backups retained.

Final installed original hashes:

| Bundle | Installed original and retained backup SHA-256 |
|---|---|
| fonts_assets_all.bundle | 33aa34892719fbc7caaabd0a292c32bb135bc61978a4cd3ce73c6c40da8f4e6e |
| localisation_assets_localisationenglish.bundle | c1e7ca97f260813ccc9a1cf463f20d066631f8e5616bf797fe8d5ae93227878f |
| ui-prefabs-general_assets_all.bundle | 2152e5ba289ccb0414c462371cfdfe05cc7ac589a10a75b8b46d359afd99786d |

No branch switch, commit/push, binary/font upload, source/map/translation/build change or release approval. Primary five tooltip matrix and restart matrix were not repeated. Current final UI Scale Medium is directly evidenced before normal exit; no new persisted-restart claim.

![Large Anisotropic Filtering actual tooltip](../../local/qa/WO-VISUAL-014/retry/2026-10-18/L-AnisoTextures.jpg)

![Naturally exposed Character Limits, unchanged Off at Large](../../local/qa/WO-VISUAL-014/retry/2026-10-18/L-CharacterLimits.jpg)

![Final Medium before normal Quit](../../local/qa/WO-VISUAL-014/retry/2026-10-18/R-medium.jpg)
