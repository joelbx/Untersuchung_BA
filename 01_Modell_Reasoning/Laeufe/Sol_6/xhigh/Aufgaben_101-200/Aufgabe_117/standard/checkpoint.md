# Checkpoint

Task: Fix QtWebEngine 5.15.3 locale crashes on Linux by adding `qt.workarounds.locale` and applying a Chromium-compatible `--lang` fallback when locale resources are missing.

Status: Complete. Implemented the WebEngine-only, default-off setting, locale file lookup, Chromium locale mappings and `--lang` fallback in `qtargs.py`. Added unit tests for locale choices, guards, resource paths, configuration metadata and argument integration. Regenerated the settings reference and reviewed the diff.

Verification: `QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/config/test_qtargs.py tests/unit/config/test_configdata.py` passed (191 tests). `git diff --check` passed. The target QtWebEngine 5.15.3 runtime was simulated in tests; no live browser startup was performed.
