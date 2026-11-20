# Checkpoint

Task: fix QtWebEngine 5.15.3 locale resource fallback in qutebrowser.

Status: investigating repository code and tests. `rg` is unavailable (`/bin/bash: rg: command not found`); using local `find` and `grep`.

Root cause evidence: `qutebrowser/config/qtargs.py` builds WebEngine flags without checking the system locale or locale resource files. Qt's locale resources are in `QLibraryInfo.TranslationsPath/qtwebengine_locales`; the installed files include `es.pak`, `es-419.pak`, `pt-BR.pak`, `pt-PT.pak`, `zh-CN.pak`, `zh-TW.pak`, `en-US.pak`, but no `es-MX.pak`, `zh-HK.pak`, or `en-AU.pak`. Qt locale names need underscore-to-hyphen normalization. Hypothesis: on QtWebEngine 5.15.3/Linux, selecting an existing fallback pak with `--lang` when the locale's pak is missing avoids the broken internal fallback.

Implementation: added `qt.workarounds.locale` (default false, QtWebEngine only), locale pak path and override helpers, and conditional `--lang` emission. The helper checks the actual locale pak first, then Chromium-compatible mapped alternatives, then base language, then en-US.

Checks:
- `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/config/test_qtargs.py tests/unit/config/test_configdata.py -o reruns=0`: 180 passed.
- `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/config -o reruns=0`: exit 1; existing `tests/unit/config/test_configfiles.py::TestConfigPy::test_nul_bytes` expects ValueError, but Python 3.11 `compile()` raises SyntaxError for null bytes. All other shown tests passed; final output was truncated, so no claim for entire suite.
- `git diff --check`: passed.

Remaining uncertainty: runtime startup with QtWebEngine 5.15.3 could not be exercised in this environment (installed Qt runtime is 5.15.2). The regression tests simulate 5.15.3 and assert the generated flag.
