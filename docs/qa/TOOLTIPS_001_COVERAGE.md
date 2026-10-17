# Actual tooltip visual coverage tracker

Updated: 2026-10-17. Baseline probe-013 unchanged. Accepted evidence: WO-VISUAL-013 / docs/PROBE_013_ACCEPTANCE.md. WO-VISUAL-014 is assigned but not executed; do not promote planned coverage.

WO-VISUAL-014 attempt: BLOCKED before installation by wrong-target screenshot and unavailable documented hover/pointer capability in that session. All new cells stay NOT_RUN; no control-absence claims. Resume gate: WO_VISUAL_014_RESUME.md. Prior accepted coverage unchanged.

| Group | Count | Medium | Small/Large | Follow-up |
|---|---:|---|---|---|
| Resolution, FullScreenMode, MaxFPS, AntialiasingMode, Vsync | 5 | scoped PASS | scoped PASS | No repeat |
| MSAASamples, AntialiasingQuality, DepthOfField, AmbientOcclusionMode, AmbientOcclusionModeQuality, CharacterDrawDistance | 6 | scoped PASS | NOT_RUN | WO-014 |
| AnisoTextures, Bloom, ShadowQuality, TextureQuality, WorldDetail | 5 | NOT_RUN | NOT_RUN | WO-014, bounded activation attempts |
| QualityPresets | 1 | NOT_RUN | NOT_RUN | WO-014, activation uncertain |
| AnimationSkinningQuality, CharacterLimits, RenderScale | 3 | NOT_RUN | NOT_RUN | Main-menu reachability uncertain; no gameplay expansion |

All counts sum to 20 records. PASS means only inspected text/readability/layout within capture limits, not full native-resolution shaping or functional option semantics. CharacterLimits variable/colour coverage unresolved; graphics-option lists and MaxFPS/VSync behavior remain outside current visual assignment. Global fixed-width suitability and release remain unapproved.
