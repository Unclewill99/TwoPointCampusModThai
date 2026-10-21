# Native tooltip investigation — 2026-10-18

Controller continued WO-TOOLTIP-CONTEXT-001 without launching or modifying the game. This supersedes the earlier tooling boundary: the existing local LibCpp2IL library was successfully hosted through a small reflection tool, without installing another package. Metadata was detected as 27.1. Native listings and symbol maps stay under local/tools/native-inspection; no game executable or disassembly is added to version control.

## Validation

tools/NativeMap.cs maps managed tokens through the existing LibCpp2IL library and records native pointers, raw offsets and field offsets. tools/disassemble_tooltip_methods.py independently checks 65 pointers for the three target classes against TPS.Game.dll's codegen method table (token RID minus one), checks PE virtual/raw mapping, follows chained x64 unwind records, and requires complete Capstone byte consumption. Seven principal method bounds/hashes are recorded in reports/tooltip-native-inspection.json. GameAssembly SHA-256: e4276817dac20d34cd8b6d5a2b5dbc1f55b47575ee27c421a3130695cbd9b957. Metadata SHA-256: 375d924a38c559a10a90af600c609424d5a18a43018caadc29a441d50e0c51fb.

Shared native code may have several managed aliases. A printed alias alone is not proof of a specific generic instantiation; relevant generic references were resolved independently through metadata usages. Listings are static evidence, not observed runtime calls.

## QualityPresets: a new, bounded target is justified

TooltipManager.OnUpdate starts at VA 0x180b03d90. The mouse path enumerates InputManager.RaycastResults (field offset 0x68). For each raycast object it first tries GameObject.TryGetComponent<TooltipSpawner> at 0x180b04116, with the generic method reference resolved at 0x185863840. An enabled provider is recorded and scanning stops at 0x180b04181.

If that object has no enabled provider, the manager checks TryGetComponent<Image> at 0x180b04198 (generic reference 0x1858638b0). At 0x180b041f3 it calls virtual slot 24, Graphic.get_raycastTarget; a true result stops the scan at 0x180b041fd. It also stops on a CanvasGroup whose blocksRaycasts is true. This path does not climb ancestors to locate a parent TooltipSpawner.

The asset trace positively locates the QualityPresets provider on OptionsQuality, with an enabled TPS.Core.UI.UITouchable/raycast target. The title Image and all five button Background Images also have raycastTarget=1. Neither the title nor the button Background has that parent provider. Therefore a foreground Image hit can stop the scan before OptionsQuality's provider is considered. This is a source-backed explanation consistent with the two WO-014 negative observations; exact runtime hit order was not captured and remains an inference.

New diagnostic target: a visibly empty gap/padding area inside the preset BUTTON ROW, outside the heading and outside button/background/text/icon rectangles. This can expose the parent UITouchable rather than an opaque child Image. A real screenshot must establish a safe visible gap; do not calculate a screen coordinate from serialized Unity units. If no suitable gap exists, report NOT_RUN instead of blind pointer placement. See qa/WO_VISUAL_015.md. This is a distinct target, not another unchanged heading/Very High hover.

TooltipSpawner.CursorOver (0x180b077c0) accumulates unscaledDeltaTime into _cursorTime (+0x58), capped by _hoverTime (+0x18), and returns before the threshold. If _shouldShowFunc (+0x70) exists it must return true. Empty translation with no data provider hides the tooltip. CursorOut (0x180b08d30) resets elapsed hover time and hides it. These are additional possible gates; none was measured live in WO-014. Hold still for the bounded wait; do not infer success from the provider merely existing.

## Two hidden rows: keep their default-hidden disposition

PreferencesPanelVideo instance field offsets independently resolved from the binary: _animationSkinningQuality=0xb8, _renderScale=0xd8, _renderScaleDisplay=0x110. Awake, Show, RefreshDropDowns and SyncGUIToCurrentSettings were read as native code. Show subscribes the animation dropdown and render slider callbacks, sets render slider range, and calls SyncGUIToCurrentSettings; SyncGUI fills their values. No opening/quality-selection path that activates either row was established in these lifecycle methods.

Important distinction: SyncGUI has several GameObjectUtils.SetActive(false) calls, including 0x1809edb69 near the render slider reference. Resolved metadata usage 0x18586d160 identifies TryGetComponent<TPC.OverridenValueVisual>; these calls operate on override-indicator data, not proof that the setting row itself is dynamically hidden. Do not misreport them as a platform gate or hide-row condition.

The positive evidence remains: both rows start inactive in the prefab and the reviewed opening code does not establish a route to expose them. Their exact visibility policy elsewhere is not proven. Do not guess a GPU, platform, DLC or graphics dependency; do not force-enable the rows. Their runtime visual cells stay NOT_RUN/control not exposed. Further native call-site work is only useful if these settings become a product requirement; coverage completeness alone does not justify modifying the game's settings UI.

## Disposition and next handoff

Native mapping/inspection milestone complete. QualityPresets now has a source-backed, narrow parent-gap diagnostic ready for Antigravity in WO-VISUAL-015 using unchanged probe-013. That work order is prepared, NOT_RUN, and has not been sent to another chat. Hidden rows are explicitly excluded. Accepted coverage remains 17/20 until real captures add evidence. No new candidate, translation/layout change, production ZWSP or release approval.

## Reproduction

Use the local Windows Framework csc.exe to compile tools/NativeMap.cs into local/tools/native-inspection/NativeMap.exe. Place a .NET 6 runtimeconfig beside it, as already present locally. Run it through dotnet with GameAssembly.dll, global-metadata.dat and the local output directory as its three arguments, then run tools/disassemble_tooltip_methods.py. An optional fourth argument is a local file of hex virtual addresses for metadata-global resolution. LibCpp2IL and dependency DLLs are loaded from the existing UABEA installation path in the source; the tool does not execute game methods or load GameAssembly as a running module.


## Accepted WO-VISUAL-015 — 2026-10-18

QualityPresets parent-gap activation and scoped visual PASS accepted at Medium/Small/Large after Controller image inspection and text comparison. Combined accepted coverage 18/20 keys (54 scale cells). WO-015 complete; prior prepared/NOT_RUN status is historical. Two hidden rows remain NOT_RUN/control not exposed. All three originals independently checked, final Medium attributed to tester evidence. No new build/repeat WO or release approval. See docs/WO_VISUAL_015_ACCEPTANCE.md (repository-relative path) and current coverage tracker. Next consolidate candidate scope and known limits before expanding work.
