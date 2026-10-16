# Campus tooltip layout investigation

Date: 2026-10-16. Read-only inspection; no game bundles modified.

tools/inspect_tooltip_layout.py inventories eight PC arrow tooltip prefabs from ui-prefabs-general_assets_all.bundle, recording exact root/component IDs, TMP settings, rects, custom layout data and referenced fitter settings. Reproducible report: reports/tooltip-layout-audit.json, with original bundle hash.

For UI_General_P_Tooltip_Main_PC_arrowLeft, the root rect's serialized size delta is x=500/y=0, while its text rect size delta is zero. TMP has m_fontSize=34, m_enableAutoSizing=0, m_TextWrappingMode=1, m_isRichText=1 and m_overflowMode=0. The controller references a custom layout with resize modes and a ContentSizeFitter storing horizontal/vertical fit=2. The separately named arrowDownWithWrapping prefab also stores m_TextWrappingMode=1. Numeric values are recorded raw: neither naming nor enums alone prove runtime wrapping, effective dimensions or runtime overrides.

Consequences: the root width is not proof of usable text width, and the tooltip includes a layout/fitter path beyond the rich-text parser. The prior width-tag experiment's blank oversized tooltip cannot be attributed conclusively to Thai or a particular component. No runtime binding has been established between these prefabs and Settings Resolution.

No speculative prefab patch has been produced. Next evidence request is WO-VISUAL-006: original-only readable English multiline baseline, with source-newline comparison. This must distinguish explicit line breaks from automatic wrapping. A confirmed candidate can then inform targeted prefab/reference tracing and a bounded English control before new Thai A/B.
