# Initial local evidence — 2026-10-15

Campus build: 10.3.169253+2024-12-06.1241; Unity 2020.3.47f1.
Museum build: 12.0.244617+2026-10-08.0811; Unity 6000.0.63f1.
Both have GameAssembly.dll, IL2CPP metadata and Addressables bundle catalogs.

The catalogs were decoded locally with UnityPy. Campus has 158 base Addressables bundles; Museum has 9169. These counts exclude DLC folders.

Museum catalog explicitly names NotoSans_Thai, NotoSans_Thai_Dynamic, NotoSans_Thai_LanguageNames and NotoSansThai-Medium.ttf, plus Thai I2LS text files including I2LS_Fonts.txt. This establishes Thai font/localisation asset references, not proof of their runtime configuration or shaping behavior.

Campus contains a fonts bundle and language-specific localisation bundles. Its engine version differs substantially from Museum's; direct bundle transplantation has not been validated.

Several Campus bundles omit a usable Unity version. The inspection tool uses the version read from that game's globalgamemanagers as an explicit fallback. Object read errors remain visible in the JSON report.

Open questions: Museum physical bundle mapping, TMP font fallback and glyph coverage, Thai mark positioning and wrapping, Campus text serialization and safe loading hook. No runtime rendering tests or binary patches have been performed.
