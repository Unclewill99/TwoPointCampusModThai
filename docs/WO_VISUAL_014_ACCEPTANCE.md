# Controller acceptance — WO-VISUAL-014

Date: 2026-10-18 (Asia/Bangkok). Completed desktop report supersedes earlier capability blockers. Controller read the report and WO/resume requirements; independently inspected S-MSAASamples, L-WorldDetail and L-CharacterLimits images. Remaining observations are attributed to the desktop tester, not a repeated Controller session.

Accept 27 new Video cells: six prior Medium-only keys at Small/Large, plus AnisoTextures, Bloom, ShadowQuality, TextureQuality and WorldDetail at all three scales. Accept CharacterLimits text/substitution/colour at all three scales per report and sampled Large evidence. Counts displayed are 150/300 and 300/600; warning is red and no raw variables/tags remain. Limit functionality was not exercised.

Together with WO-013 this establishes scoped visual coverage for 17/20 records at all three scales. QualityPresets is NOT_OBSERVED at Medium after heading/selected-value attempts; Small/Large were conditional and remain NOT_RUN. AnimationSkinningQuality and RenderScale remain NOT_RUN/control not exposed. WO-014 execution is complete within its bounded instructions, with these explicit coverage gaps; no all-20 acceptance.

Source LF versus extra wrapping is distinguished in the report. Short continuation rows/unused width remain quality tradeoffs; no content loss is established in sampled images. Capture detail does not establish native shaping fidelity or dictionary-quality segmentation. No translation/layout/build change, production ZWSP, permanent installation or release follows from this result.

Controller ran manage_probe check --probe probe-013: all THREE installed originals and staged/retained-backup hashes pass. Report supplies normal exit, final Medium and independent final hash evidence. Medium is tester evidence; Controller did not launch the game. Original manifest/map remain unchanged.

Next engineering step performed: recursive read-only search of original UI prefab serialized strings. References exist for all three remaining keys (six matching objects); one object cannot be decoded and is explicitly retained as a limitation. See reports/remaining-tooltip-context.json and tools/inspect_remaining_tooltips.py. Presence is not activation evidence. Continue visibility/provider tracing under WO_TOOLTIP_CONTEXT_001.md before another runtime assignment.
