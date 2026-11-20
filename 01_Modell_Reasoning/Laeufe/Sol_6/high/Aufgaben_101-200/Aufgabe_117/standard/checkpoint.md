# Checkpoint

Task: Resolve QtWebEngine 5.15.3 locale pack crashes with an opt-in Linux workaround.

Implemented:
- Added `qt.workarounds.locale` as a QtWebEngine-only, restart-required boolean setting defaulting to false.
- Added locale pack path lookup, Chromium-style fallback mappings, version/platform/config gates, and `--lang` argument injection.
- Added tests for locale mappings, missing packs, gates, configuration scope, and QtWebEngine/QtWebKit argument behavior.

Verification:
- `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/config/test_qtargs.py tests/unit/config/test_configdata.py`: 192 passed.
- `git diff --check`: passed.
- `python -m py_compile` on changed Python files: passed.
- `python -m flake8` unavailable locally (module not installed); no downloads requested.
