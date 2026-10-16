# Text-child layout constraint investigation

Date: 2026-10-16. Staged/reloaded only; original three files verified.

The traced TMP text GameObject has a RectTransform (3218277146759428662), CanvasRenderer and localisation component, but no separate serialized LayoutElement. Text rect width starts at zero. Its parent's referenced standard layout group (2617668728378194486) stores m_ChildControlWidth=1 and m_ChildControlHeight=1, while a custom wrapper and content fitter coexist. These serialized references identify a plausible text-child width owner, not proof of runtime assignments.

Probe-008 altered the content rect/fitter, not this text rect or parent's child-width control. Probe-011 therefore tests a distinct paired hypothesis: set text rect width to 800 and parent m_ChildControlWidth=0, allowing the existing child width to serve as the requested constraint. Keep original m_TextWrappingMode=1 (Normal decoded from actual metadata), original content fitter/custom wrapper, font, material and long English stimulus. No width tags, source newlines or colour markers added.

Raw-payload/reload comparison across the UI bundle verifies exactly two objects changed and complete expected trees match. Font/localisation bytes equal probe-007-long. Runtime custom behavior could still override either edit; no width or wrapping success claimed. Report must distinguish boundedness, automatic breaks, completeness and shared-tooltip effects. No need to infer specific C# causes from a negative result.

WO-VISUAL-011 is ready. No new assemblies, loader or live instrumentation. Probe-003 remains translation baseline; this experiment contains synthetic long English, not a release candidate.
