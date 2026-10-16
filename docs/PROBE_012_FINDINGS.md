# Bounded Thai/ZWSP comparison build

Date: 2026-10-16. Both variants staged/reloaded; not installed. Three originals independently checked.

probe-012a/b derive from the English-control layout of probe-011. Font and UI bundles are byte-identical across both and to that baseline. Only one localisation segment changes: Resolution tooltip. A repeats the original synthetic Thai paragraph three times. B repeats its ZWSP variant with an extra boundary opportunity between repetitions. Removing U+200B from B exactly reproduces A; neither has LF, tags or source delimiter. Code points and insertion offsets are in each local diagnostic map, hash-bound by manifest.

Reload comparisons verify only the intended Settings segment changes, with all other TextAssets intact. Translation pilot r3 remains untouched. These synthetic bodies are not gameplay translations and not release assets.

WO-VISUAL-012 requests exact line-boundary/readability comparison under the same recorded environment, actual bounds verification and three-file restoration between variants. English control already demonstrated bounded automatic wrapping; Thai word-boundary quality, glyph grouping and ZWSP effects remain NOT_RUN. No dictionary-breaking or production insertion policy is assumed.
