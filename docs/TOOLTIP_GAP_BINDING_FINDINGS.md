# Remaining tooltip binding findings

Date: 2026-10-18. Read-only Controller investigation, unchanged original game bundles. Reproduce with `python tools/trace_tooltip_gaps.py`; evidence: reports/tooltip-gap-binding-trace.json. Script bundle CAB identity is checked against UI external file 1 before resolving MonoScript references. Metadata v27 tables are bounds/alignment checked; method declaring-type indices are verified. No native method body or runtime property inspection was performed.

## QualityPresets

The provider exists and resolves to TPC.TooltipSpawner, component -7832899213058408743, on OptionsQuality GameObject -5932648878914634023 within the QualityPresets subtree. It is not attached to QualityPresetsTitle. It is enabled, hoverTime=0.5, termID=-1661906351 and uses the same arrowLeft tooltip controller 5202969347434510902 as the accepted tooltip configuration. Its local owner rectangle is 1801.8973 x 93.9 Unity units; these are serialized dimensions, not screen coordinates. The owner has an enabled graphic with raycast target enabled and a five-button collection. PreferencesPanelVideo references that collection through _overallQualityCollection and all five buttons through _qualityLevelOverridden.

The WO-014 selected-value screenshot was independently inspected: pointer lies on Very High; no tooltip is visible. Heading and selected-value attempts are valid negative observations for those targets. A provider and raycast graphic being present does not prove that CursorOver reaches the parent or that runtime gating permits display. Other preset buttons, parent padding and event dispatch remain unverified. Do not label this a missing translation/provider or a confirmed rendering defect. No new activation has been established, so no repeat-hover visual WO is issued from these static findings alone.

## RenderScale and AnimationSkinningQuality

RenderScale row -5379194925153222951 and Animation Quality row -2261707471542190375 are serialized inactive. Both have enabled TPC.TooltipSpawner components, respectively -8609264033478443303 (termID=-1643057496) and 4219367355955511001 (termID=-1170698466), hoverTime=0.5 and the same arrowLeft controller. The local termIDs are recorded as serialized references; this investigation does not independently decode the termID hash algorithm.

TPC.PreferencesPanelVideo component 7433931642048839385 retains _renderScale -> -5388204712286978343, _renderScaleDisplay -> -1030755862089138471 and _animationSkinningQuality -> -30038423797137703. PreferencesMenu also lists the animation dropdown in _childDropdowns[18]. These controls are present and wired in the asset, even though not exposed in the observed main-menu context. This does not identify the condition that activates them or prove that any supported context enables them.

## Exact code investigation boundary

Build metadata identifies PreferencesPanelVideo.Awake (0x60088d5), Show (0x60088d6), SyncGUIToCurrentSettings (0x60088de), RefreshDropDowns (0x60088e3), ChangeRenderScale (0x60088f4), ChangeAnimationSkinningQuality (0x60088f9) and UpdateRenderScaleDisplay (0x60088fb). TooltipSpawner exposes SetShouldShowFunc (0x6008b34), CursorOver (0x6008b36) and CursorOut (0x6008b39), with runtime fields _shouldShowFunc, _dataProvider and _cursorTime. These names narrow further inspection; they do not establish actual predicates, call flow or event propagation.

Exact visibility predicates and QualityPresets event/gating cause remain unresolved: the available trace covers serialized data and metadata declarations, not IL2CPP native method bodies. No standalone native disassembler/IL2CPP mapping command was found in the inspected tool paths; existing LibCpp2IL DLLs alone were not treated as decoded method evidence. Further code work needs a verified metadata-token-to-native-address mapping and method-body/call-site inspection, or an explicitly scoped read-only runtime observation facility. Do not guess platform/quality/DLC conditions from method names, change graphics, force-enable rows or inject a loader.

One MonoBehaviour at path_id 820722457322749657 fails typetree decoding (expected 476 bytes, read 352). The trace preserves this known limitation; absence claims are restricted to decoded components. All three providers were positively decoded, so the failure does not negate their presence.

## Disposition

WO-TOOLTIP-CONTEXT-001 static binding milestone completed with explicit unresolved native/runtime conditions. Keep QualityPresets NOT_OBSERVED and the two hidden rows NOT_RUN/control not exposed. Accepted coverage remains 17/20; no build, translation, layout or release change is justified. Continue native/event-gating investigation before a new runtime assignment. Game originals and retained backups are verified with manage_probe check --probe probe-013 after this work.


## Superseding native investigation — 2026-10-18

The prior native tooling boundary above is now resolved. See TOOLTIP_NATIVE_FINDINGS.md for validated pointer mapping, raycast dispatch analysis and the explicitly limited hidden-row findings. A new parent-gap diagnostic is prepared in qa/WO_VISUAL_015.md; no runtime activation/PASS is claimed yet.
