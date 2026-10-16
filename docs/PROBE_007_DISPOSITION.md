# Controller disposition — tag-free English length control

Date: 2026-10-16. Read WO_VISUAL_007_REPORT.md; inspected 17-long-tooltip.jpg; independently checked installed hashes via manage_probe.py check --probe probe-007-long: both original. Other session observations are attributed to the desktop tester.

Accepted: short baseline PASS for the original explicit three-line English tooltip under probe-003 fonts. Long variant shows viewport-spanning horizontal expansion/clipping, readable fragments of the repeated middle line, and no established extra break within that segment. First/last source lines cannot be evaluated from the long capture. Automatic wrapping remains NOT_ESTABLISHED.

This result shows the unsuitable long-text outcome is reproducible without width markup; the prior width tag is therefore not a necessary condition for horizontal growth. It does not prove both failures share one cause or identify a particular runtime setting. No Thai, dictionary, ZWSP, font-shaping or universal-wrapping conclusion follows.

Stop further content-only wrapping trials on this unchanged Resolution path. Retain probe-003 as the translation baseline. Next engineering must resolve effective layout/constraint ownership: trace the Resolution GameObject and tooltip-provider references (including the unread component), locate preferred/max-width logic or validate an actually bounded component before patching. If runtime inspection tooling is required, prepare a separate concrete instrumentation plan; do not silently install a loader or modify assemblies.

Any future test must establish bounded readable spaced English before Thai A/B. A prefab with a wrapping-related name or root size alone is insufficient. Explicit-newline layout remains a demonstrated capability but is not yet approved as a global Thai segmentation workaround.

Originals independently verified restored; both variant backups retained per report. No new visual work order or new build in this review. VOWEL-02 evidence quality, atlas stress, gameplay and token/plural semantics remain pending.
