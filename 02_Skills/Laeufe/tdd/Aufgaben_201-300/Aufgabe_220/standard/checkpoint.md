# Checkpoint

Task: add `qcolor_to_qsscolor` with test-first verification and check stylesheet integration.

Status: investigating repository. `rg` is unavailable (`/bin/bash: rg: command not found`); using `grep` and `find`.

TDD: helper test failed with missing attribute, then passed. TabBar stylesheet test failed with empty stylesheet, then passed. WebKit test could not collect initially because `PyQt5.QtWebKitWidgets` is absent; it now skips when that optional Qt module is unavailable.

Blocked check: `QT_QPA_PLATFORM=offscreen python -m pytest -q -o addopts= --override-ini filterwarnings=ignore tests/unit/mainwindow/test_tabwidget.py::TestTabWidget::test_tabbar_background_stylesheet_uses_configured_alpha tests/unit/browser/webkit/test_webview_stylesheet.py` failed during setup/collection. Errors: `ModuleNotFoundError: No module named 'PyQt5.QtWebKitWidgets'`; existing TabWidget constructor raised `TypeError: QSize(...): argument 1 has unexpected type 'float'` from `_set_icon_size`. This limits direct WebView and full TabWidget execution in this environment. A narrower real QTabBar test passes.

Verification:
- `QT_QPA_PLATFORM=offscreen python -m pytest -q -o addopts= tests/unit/mainwindow/test_tabwidget.py::test_tabbar_background_stylesheet_uses_configured_alpha tests/unit/utils/test_qtutils.py::test_qcolor_to_qsscolor_preserves_rgba_components tests/unit/browser/webkit/test_webview_stylesheet.py`: 5 passed, 1 skipped (WebKit module unavailable).
- `QT_QPA_PLATFORM=offscreen python -m pytest -q -o addopts= tests/unit/utils/test_qtutils.py`: 123 passed.
- `python -m compileall -q qutebrowser/utils/qtutils.py qutebrowser/browser/webkit/webview.py qutebrowser/mainwindow/tabwidget.py tests/unit/browser/webkit/test_webview_stylesheet.py`: passed.
- `git diff --check`: passed.
- `QT_QPA_PLATFORM=offscreen python -m pytest`: failed during startup because configured `--strict` triggers `pytest.PytestRemovedIn8Warning: The --strict option is deprecated, use --strict-markers instead.`
- `QT_QPA_PLATFORM=offscreen python -m pytest -o addopts= -q`: started 7866 tests, then end-to-end setup repeatedly failed with `AttributeError: module 'pytestqt.plugin' has no attribute 'SignalBlocker'` (e.g. `tests/end2end/test_dirbrowser.py::test_parent_folder`). Interrupted after 295 errors; full suite status remains uncertain. No dependency downloads or harness changes.
