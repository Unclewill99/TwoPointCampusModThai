# WO-VISUAL-009 REPORT

2026-10-16 (Asia/Bangkok). **COMPLETED — POSITIVE MARKER**. Resolution displayed bright magenta throughout its three readable lines. Original restored and SHA-256 verified for all three bundles.

Read WO_VISUAL_009.md, reports/probe-009-build.json and local/prototype/probe-009/manifest.json. Marker: TMP path 2671690608638065206; m_fontColor and m_fontColor32, RGB 1,0,1 alpha 1. Manifest/build preparation-time NOT_RUN metadata was not edited; this report records runtime results. Both JSON files remain SHA-256 6ba4257e5805060a15e88a074c7e4449d9b3e1a355837002151f7ba71d6bf594.

## Environment and procedure

Steam launch; build 10.3.169253+2024-12-06.1241; English, UI scale Medium; Full Screen Window, 3840 × 2160 at 60 Hz. Full-screen captures are 1920 × 1080. No settings changed or Apply used; no gameplay/save loaded.

Initial attempt was blocked by the running-game guard without installation. Logs 01–05 preserve that attempt. After the user closed Campus, 06-resume-original.txt confirmed all three originals. An escalation retry was automatically rejected over the earlier running-state concern; fresh read-only process/window evidence confirmed closure, then guarded installation succeeded. 07-install.txt and 08-installed.txt confirm all three probe bundles. Every manager command used --probe probe-009. No other variant installed.

## Visual results

| Target | Observation and evidence |
|---|---|
| Resolution | **POSITIVE**: all three lines bright magenta, fully readable; no visible mixed/dark portions. White body approximately x939–1426, y342–425 in capture coordinates. [Image](../../local/qa/WO-VISUAL-009/12-resolution-magenta.jpg). Prior [short English tooltip](../../local/qa/WO-VISUAL-007/08-short-tooltip.jpg) had dark text. |
| Antialiasing | All four lines magenta and readable. Separate [image](../../local/qa/WO-VISUAL-009/13-antialiasing-magenta.jpg). |
| Quality Presets | **NOT_OBSERVED**: no tooltip after hovering heading or Very High control and allowing capture to settle. Separate [heading](../../local/qa/WO-VISUAL-009/14-quality-heading-no-tooltip.jpg) and [control](../../local/qa/WO-VISUAL-009/15-quality-control-no-tooltip.jpg) images. Identifying visible labels: Quality Presets; Very Low, Low, Medium, High, Very High. No runtime tooltip available to transcribe. |

Resolution transcription (visual lines):

```text
Sets window resolution.
Higher resolution makes the whole game appear sharper.
Reduce resolution to increase CPU and graphics performance.
```

Antialiasing transcription, preserving source wording “that”:

```text
Enables anti-aliasing, which reduces jagged edges.
SMAA is higher quality that FXAA.
SMAA is also slower to run than FXAA.
Disable to increase graphics performance.
```

Environment evidence: [build](../../local/qa/WO-VISUAL-009/09-build.jpg), [English/Medium](../../local/qa/WO-VISUAL-009/10-english-medium.jpg), [Video](../../local/qa/WO-VISUAL-009/11-video.jpg). Antialiasing evidence is not cited as Quality Presets evidence.

The positive marker supports consumption of the patched serialized TMP path. It does not establish a particular runtime object instance or layout-controller override. No width, automatic-wrapping, Thai or ZWSP conclusions.

## Restoration

Quit normally through main-menu Quit. 16-restore.txt records restoration; 17-final-original.txt reports original for ALL THREE. 18-final-hashes.json independently verifies all manifest original hashes. Backups retained.

| Bundle | Final original SHA-256 |
|---|---|
| fonts_assets_all.bundle | 33aa34892719fbc7caaabd0a292c32bb135bc61978a4cd3ce73c6c40da8f4e6e |
| localisation_assets_localisationenglish.bundle | c1e7ca97f260813ccc9a1cf463f20d066631f8e5616bf797fe8d5ae93227878f |
| ui-prefabs-general_assets_all.bundle | 2152e5ba289ccb0414c462371cfdfe05cc7ac589a10a75b8b46d359afd99786d |

Evidence and exact outputs: local/qa/WO-VISUAL-009/. Apart from authorized probe installation/restoration, no code/assets/translations edited during testing. Only evidence/report written. No loader installation, branch change, commit/push or uploads.
