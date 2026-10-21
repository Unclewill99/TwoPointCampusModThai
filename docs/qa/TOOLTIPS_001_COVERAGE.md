# Actual tooltip visual coverage tracker

Updated: 2026-10-18. Baseline probe-013 unchanged. Accepted evidence: WO-VISUAL-013, completed WO-VISUAL-014 and WO-VISUAL-015 runs. Earlier capability blockers are historical.

| Group | Count | Medium | Small/Large | Follow-up |
|---|---:|---|---|---|
| Resolution, FullScreenMode, MaxFPS, AntialiasingMode, Vsync | 5 | scoped PASS (WO-013) | scoped PASS (WO-013) | No repeat |
| MSAASamples, AntialiasingQuality, DepthOfField, AmbientOcclusionMode, AmbientOcclusionModeQuality, CharacterDrawDistance | 6 | scoped PASS (WO-013) | scoped PASS (WO-014) | No repeat |
| AnisoTextures, Bloom, ShadowQuality, TextureQuality, WorldDetail | 5 | scoped PASS (WO-014) | scoped PASS (WO-014) | No repeat |
| CharacterLimits | 1 | scoped PASS (WO-014) | scoped PASS (WO-014) | Visible substitution/colour accepted; functional limits untested |
| QualityPresets | 1 | scoped PASS (WO-015) | scoped PASS (WO-015) | Parent-gap activation established; no repeat |
| AnimationSkinningQuality, RenderScale | 2 | NOT_RUN/control not exposed | NOT_RUN/control not exposed | Static visibility/context investigation |

18/20 records have scoped Small/Medium/Large visual evidence (54 cells total across WO-013/014/015). WO-015 adds QualityPresets at all three scales via one visible parent-gap hover per scale. WO-014 adds 27 Video cells and three CharacterLimits cells. CharacterLimits displays 150/300 closed and 300/600 open-description counts and a red warning without toggling the control. These are displayed substitutions, not functional option tests.

PASS covers inspected content/readability/containment at returned capture detail, not full native-resolution shaping or all Thai word boundaries. Shared-width short rows/unused space remain layout-quality observations. No all-20, global fixed-width rollout, glossary, ZWSP or release approval. Graphics-option lists and MaxFPS/VSync behavior remain outside this assignment.

Current disposition: reachable actual-tooltip scale milestone complete. No new desktop WO is needed for these 18 keys. AnimationSkinningQuality and RenderScale stay NOT_RUN/control not exposed, not N/A or PASS; initial inactive state and no supported activation route in reviewed lifecycle code are documented in ../TOOLTIP_NATIVE_FINDINGS.md. Do not force-enable controls just to fill the matrix.

WO-015 parent-gap success establishes an activation route, consistent with the static child-Image explanation; runtime hit order remains unmeasured. Earlier WO-014 negative heading/button results remain historical evidence for those different targets. Final Medium is tester evidence; Controller inspected all three QualityPresets captures and independently verified the three originals. See ../WO_VISUAL_015_ACCEPTANCE.md.

Next Controller work: consolidate the probe-013 milestone and known layout/coverage limits before choosing the next rendering or translation batch. No all-20 or release acceptance; no speculative hidden-control repeat, rebuild or text edit follows from this result.
