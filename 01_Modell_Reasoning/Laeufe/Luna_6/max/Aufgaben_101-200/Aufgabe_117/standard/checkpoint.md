# Checkpoint

Task: implement the opt-in QtWebEngine 5.15.3 locale workaround in `/app`.

Implementation:
- Added `qt.workarounds.locale` (default `false`, QtWebEngine backend only, restart required).
- Added locale normalization, `.pak` path construction, Chromium-compatible fallback candidates, and `_get_lang_override` gates for enabled config, Linux, QtWebEngine backend, and exact 5.15.3.
- Added `--lang=<locale>` to QtWebEngine startup arguments when a fallback is needed. Locale resources are searched under Qt's `TranslationsPath/qtwebengine_locales`.

Verification:
- `QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/config/test_qtargs.py tests/unit/config/test_configdata.py` — 148 passed.
- `git diff --check` — clean.
- A test run without `QT_QPA_PLATFORM=offscreen` aborted while Qt attempted to initialize a display; rerunning offscreen passed.
