# Checkpoint

Task: Consolidate QtWebEngine `--enable-features=` arguments from CLI, `qt.args`, and configuration without changing non-QtWebEngine arguments.

Implementation: `qt_args` extracts existing feature flags only for QtWebEngine, and passes them to `_qtwebengine_args`. `_qtwebengine_enabled_features` strips each prefix, splits comma-separated values, then adds OverlayScrollbar when configured and supported. Added tests for merging, QtWebKit unchanged behavior, empty flags, and both helpers.

Verification:
- `pytest -q tests/unit/config/test_qtargs.py -k 'not test_new_chromium'`: 81 passed, 1 deselected.
- Regression tests against original `HEAD:qutebrowser/config/qtargs.py`: 4 failed, 1 passed, as expected. Restored edited implementation and reran the suite above successfully.
- `git diff --check`: exit 0.
- `pytest -q tests/unit/config/test_qtargs.py`: exit 1, stopped without summary at `TestDarkMode::test_new_chromium`.
- `pytest -vv tests/unit/config/test_qtargs.py::TestDarkMode::test_new_chromium`: exit 139, Fatal Python error: Segmentation fault in `qutebrowser/browser/webengine/webenginesettings.py:360` (`init_user_agent`), called from `version._chromium_version`. This environment prevents verifying the full file including that preexisting QtWebEngine version test.

Tooling: `rg` unavailable (`/bin/bash: rg: command not found`), used local grep/find. A temporary red-green command containing `rm -f` was rejected by automatic approval review as unsafe; reran safely without deletion.
- `flake8 qutebrowser/config/qtargs.py tests/unit/config/test_qtargs.py`: exit 127, `/bin/bash: flake8: command not found`. Lint status remains unverified; no downloads were attempted.
- `python -m compileall -q qutebrowser/config/qtargs.py tests/unit/config/test_qtargs.py`: exit 0.
- Final `git diff --check`: exit 0.
