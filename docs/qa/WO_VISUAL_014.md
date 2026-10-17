# WO-VISUAL-014 — remaining actual tooltip coverage, unchanged probe-013

Date: 2026-10-17. Controller: ChatGPT. This is a coverage follow-up, NOT probe-014. Install target remains probe-013. Do not rebuild or alter the staged candidate.

Read WO_VISUAL_013_REPORT.md and PROBE_013_ACCEPTANCE.md (parent docs folder), plus local/prototype/probe-013/manifest.json and tooltip-map.json. Confirm manifest/map/staged hashes before installation. Source reference: local/translations/TOOLTIPS-001.th.r2.json. Exact key prefix throughout: UI/Settings/Tooltips/.

## Required coverage matrix

| Keys | Medium | Small | Large |
|---|---|---|---|
| MSAASamples, AntialiasingQuality, DepthOfField, AmbientOcclusionMode, AmbientOcclusionModeQuality, CharacterDrawDistance | Already accepted; do not repeat | Test | Test |
| AnisoTextures, Bloom, ShadowQuality, TextureQuality, WorldDetail | Test if tooltip naturally exposed | Test if exposed | Test if exposed |
| QualityPresets | One bounded hover attempt on heading and existing selected preset; no click | Only if activation established | Only if activation established |
| AnimationSkinningQuality, CharacterLimits, RenderScale | Reachability observation only if naturally visible | Only if naturally exposed | Only if naturally exposed |
| Resolution, FullScreenMode, MaxFPS, AntialiasingMode, Vsync | Already accepted | Already accepted | Already accepted |

Do not deliberately repeat the five primary keys or their restart matrix. If incidentally exposed, note only new regressions. Do not infer PASS from old results for missing matrix cells. QualityPresets attempts should stop after hover/wait and one fresh capture per available target; no prolonged chase.

## Lifecycle

Use real Windows UI/screenshot access. With Campus closed normally, run separately and inspect each exit code/states:

```
python tools/manage_probe.py check --probe probe-013
python tools/manage_probe.py install --probe probe-013
python tools/manage_probe.py check --probe probe-013
```

Require original for ALL THREE before and probe for all three after. Launch via Steam only after successful installed check in a later call. English, unchanged resolution, main-menu Settings only. Start Medium for newly exposed controls, then Small/Large for missing cells. Change ONLY UI Scale, return Medium afterward. No Apply, graphics option selection, sliders, limit toggles, save/gameplay load, force-close or code edits. If small/large navigation becomes difficult, revert and record coverage gap.

For each tested key/scale capture the actual tooltip and identifying control, complete text accounting against map, visible bounds/line count, source LF vs extra breaks, clipping, readability, edge containment, base/mark/leading-vowel integrity and large empty-space effects. Record exact questionable line boundaries, not guessed text. Capture detail limits native shaping conclusions. Do not use filename alone as proof of content.

If control visible but tooltip absent after bounded attempts, use NOT_OBSERVED and reason; if control absent use NOT_RUN/control not exposed. Never mark N/A solely because not found. CharacterLimits, if naturally exposed, may be inspected without toggling: record actual variable values/colour only when visible, no fake substitution or gameplay expansion. No functional MaxFPS/VSync experiments. No automatic ZWSP/manual newline insertion.

Quit normally, then separately:

```
python tools/manage_probe.py restore --probe probe-013
python tools/manage_probe.py check --probe probe-013
```

Require originals for ALL THREE and retain existing backups. If guard or restore fails, stop/report; no bypass. No new restart test required absent observed failure.

## Delivery

Write docs/qa/WO_VISUAL_014_REPORT.md. Evidence: local/qa/WO-VISUAL-014/. Include per-key/per-scale results, exact image refs, hashes/build/actual scale and resolution, reachability limitations and final Medium/original state. Existing WO-013 evidence stays intact. No branch switches, commit/push, binary/font upload, build/map/source modifications or release approval. No claims of all-20 coverage unless every requested cell actually has evidence.
