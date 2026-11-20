# Checkpoint

Issue: QtWebEngine 5.15.3 locale workaround.

Plan: inspect startup arguments and config declarations; implement the gated locale override and focused tests; run relevant existing tests. `rg` is unavailable (`/bin/bash: rg: command not found`), so use `grep`/`find` locally.

Initial test command: `python -m pytest -q tests/unit/config/test_qtargs.py tests/unit/config/test_configdata.py` aborted (exit 134) while pytest-qt created QApplication; Qt platform setup appears unavailable. Retrying with `QT_QPA_PLATFORM=offscreen`.

Implemented `qt.workarounds.locale` (QtWebEngine only, default false), locale pak lookup, Chromium locale mappings/fallbacks, and conditional `--lang` generation. Added focused tests for configuration, locale mappings, gates, and Qt arguments.

Verification: `QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/config/test_qtargs.py tests/unit/config/test_configdata.py` passed: 184 tests. `git diff --check` passed. Runtime behavior on QtWebEngine 5.15.3 was not directly exercised because installed Qt runtime is 5.15.2; tests patch the detected version.
