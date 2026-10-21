# WO-TOOLTIP-CONTEXT-001 — remaining tooltip binding and visibility

Date: 2026-10-18. Controller engineering follow-up; read-only, no desktop test or installation assigned.

WO-014 is complete within its bounded scope. Keep probe-013 and all translations unchanged. Do not repeat the accepted 17-key scale matrix or chase QualityPresets through more identical hovers.

Initial investigation executed by tools/inspect_remaining_tooltips.py; results in reports/remaining-tooltip-context.json. Original general UI bundle SHA-256 is 2152e5ba289ccb0414c462371cfdfe05cc7ac589a10a75b8b46d359afd99786d. Recursive MonoBehaviour/GameObject string inspection found QualityPresets title/localisation and named objects, RenderScale object/localisation, and AnimationSkinningQuality localisation. Read error path_id 820722457322749657 remains unresolved. No absence conclusion is permitted.

Next deliverable: trace each matching object through owner/parent hierarchy, provider components and script references. Establish whether QualityPresets has a tooltip provider/activation target and which serialized or code conditions govern RenderScale and AnimationSkinningQuality visibility in this build. Record exact IDs/fields, unresolved external references and decode failures. Inspect local metadata/code only where needed; distinguish serialized defaults from runtime behavior.

Stop this engineering milestone with a source-backed disposition for each key, or explicit unresolved conditions. Issue another narrow visual WO only if a supported new activation/context is established. Any test requiring graphics changes or gameplay needs its own defined scope; current assignment does not authorize those experiments. No build/source/binary/font modification or upload, no invented runtime PASS, and no release approval.


## Initial context disposition — executed 2026-10-18

Recursive hierarchy tracing confirms RenderScale (GameObject -5379194925153222951) is serialized inactive under AdvanceSettings. AnimationSkinningQuality localisation component 8130776820718468825 belongs to TextOptionName under ContainerBG / Animation Quality (GameObject -2261707471542190375), also serialized inactive under AdvanceSettings. QualityPresets object -2354921750532096295 and its title are serialized active. All belong to the generic Settings hierarchy; VideoContainer itself starts inactive, demonstrating why serialized activity alone cannot establish current runtime visibility.

This supports investigating initialization/visibility code for the two hidden rows; it does not justify force-enabling them. The QualityPresets title/key presence does not identify a working tooltip activation target. Component script references are external (m_FileID=1); type/visibility/provider behavior remains unresolved until those references and initialization logic are traced. One unrelated undecoded object also prevents exhaustive absence claims. No fresh UI test is warranted from these static defaults alone.

The initial read-only milestone is complete with explicit unresolved activation/visibility conditions. Follow-up engineering must resolve external scripts before proposing a narrow runtime work order. Re-running tools/inspect_remaining_tooltips.py reproduces hierarchy/component references and preserves decode errors in the report.


## Binding trace completed — 2026-10-18

See TOOLTIP_GAP_BINDING_FINDINGS.md and reports/tooltip-gap-binding-trace.json. All three providers positively resolved to TPC.TooltipSpawner. QualityPresets provider is on OptionsQuality with an enabled raycast graphic; event dispatch/runtime gating remains unresolved. Both hidden rows retain PreferencesPanelVideo references. Exact visibility predicates require native method bodies, beyond serialized/metadata evidence. No new supported activation established, so no new visual WO/rebuild is issued; 17/20 acceptance unchanged.


## Native milestone completed — 2026-10-18

Earlier native-tool boundary resolved with existing local LibCpp2IL plus Capstone. See TOOLTIP_NATIVE_FINDINGS.md and reports/tooltip-native-inspection.json. Parent-provider versus foreground Image raycast behavior supports WO-VISUAL-015, a distinct parent-gap target, prepared NOT_RUN. Hidden-row opening code retains callbacks/value sync but no supported activation path was established. Preserve NOT_RUN for both; no force-enable or graphics experiments.
