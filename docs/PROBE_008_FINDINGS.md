# Traced Resolution tooltip width ownership experiment

Date: 2026-10-16. Built/reloaded locally, not installed.

The Resolution localisation component lives on TextOptionName; walking its RectTransform parents reaches the Resolution row. Its hover provider (1244118214773079769) directly references tooltip controller 5202969347434510902, the previously inspected PC arrowLeft prefab. That controller references layout wrapper 1537959580418341430 and content fitter -8613258678337963466. Exact serialized chain is in reports/probe-008-layout-trace.json. This establishes a static reference chain, not a live runtime override trace.

Probe-008 changes only the referenced fitter's horizontal fit from raw 2 to 0 and its content RectTransform sizeDelta.x to 800. It preserves TMP wrapping/size/material settings and the same probe-007-long English stimulus. Reload comparison across the whole UI bundle confirms only those two object payloads change. Fonts/localisation bytes match probe-007-long. Runtime custom layout may still override sizing; the test is diagnostic, not a claimed fix.

The earlier unread component is on a different GameObject and its partial view exposes item sorting/filtering fields. Disabling strict read-size validation is not proof of complete parsing; it was not used for patching. Its unresolved tail does not invalidate the complete, strictly read Resolution provider path.

Guarded manager now handles probe-008's three-file manifest without special bypasses. Preflight independently reports originals for all three. WO-VISUAL-008 requests width/readability/wrapping as separate outcomes and checks shared-prefab regressions. No loader or assembly instrumentation installed.
