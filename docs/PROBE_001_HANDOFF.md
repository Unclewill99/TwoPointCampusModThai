# Rendering probe 001 — staged, not installed

Created 2026-10-15. The probe is local/prototype/probe-001. It contains two rebuilt Campus bundles and a hash manifest. Original installed files are unchanged; the read-only installer check verifies this state. No runtime test has run.

## Evidence and strategy

Museum Thai font bundles exist under logical filenames alongside hashed bundles. The initial claim that physical mapping necessarily required hash decoding was too broad. tools/build_rendering_probe.py reads those named bundles directly.

Museum's Thai font-localisation mapping directs the inspected terms to NotoSans_Thai. Its serialized TMP assets expose static and dynamic variants, fallback references and font-feature records. Detailed counts appear in reports/museum-thai-font-research.json. This is stronger asset evidence, still not runtime proof.

The probe reuses Campus's existing NotoSans_Arabic_Dynamic slot and replaces the embedded NotoSansArabic-Regular font bytes with Museum's Thai TTF while retaining asset identities. It maps English font terms to that existing dynamic name and substitutes the 50-record r3 pilot. This intentionally affects the experimental English language slot; it is not a shipped Thai language selector. It does not transplant a Unity 6 TMP asset into Unity 2020.

Both rebuilt bundles reload in UnityPy. All 50 substitutions and the embedded TTF bytes compare exactly. Source TTF cmap covers the pilot characters; this does not prove dynamic glyph generation, fallback behavior, mark positioning or line breaking. Hash/CRC checks or source-font resolution may prevent runtime loading.

## Reversible execution

Close Campus first. From the project directory:

```
python tools/manage_probe.py check
python tools/manage_probe.py install
```

The installer rejects unknown installed hashes and mismatched stage/backup hashes, backs up both originals before any replacement, and rolls back on a copy/verification error. No catalog CRC/hash bypass is included. A successful copy is not successful game loading. Use the normal Steam launch, choose English and inspect settings first; the general font mapping may affect text outside the translated pilot. Do not save over an important save as part of the rendering experiment; main-menu settings are the first target.

If loading fails, record the error and restore; do not repeatedly patch unrelated bundles. Restore with Campus closed:

```
python tools/manage_probe.py restore
python tools/manage_probe.py check
```

## QA first pass

Record prototype manifest hashes, game build, resolution, actual UI scale and screenshots. Inspect Thai settings labels, Latin/numeric symbols, missing glyphs and top/bottom clipping. Then inspect available pilot notifications/classes. Synthetic corpus injection is not part of this build; tests requiring those strings remain BLOCKED/NOT_RUN. Dynamic-cache cold restart and multi-screen testing follow only after basic loading succeeds. Do not mark substitution/parser semantics or all QA cases PASS from menu text alone.

The current delivery is staged and checked only. Installation, game launch and visual results require a separate recorded execution. Bundles and the Museum font remain local and must not be uploaded to GitHub.
