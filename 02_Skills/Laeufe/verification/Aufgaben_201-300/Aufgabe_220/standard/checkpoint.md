# Checkpoint

Task: add QColor to QSS RGBA conversion utility and integrate relevant stylesheet use.
Status: implemented `qcolor_to_qsscolor`, applied it to WebView and TabBar stylesheet backgrounds, and added named/RGB/RGBA cases.

Verification:
- `QT_QPA_PLATFORM=offscreen python -m pytest -o addopts='' tests/unit/utils/test_qtutils.py -q`: 123 passed.
- `python -m compileall -q qutebrowser/utils/qtutils.py qutebrowser/browser/webkit/webview.py qutebrowser/mainwindow/tabwidget.py tests/unit/utils/test_qtutils.py`: exit 0.
- `git diff --check`: exit 0.

Environment limits and failed checks:
- `python -m pytest tests/unit/utils/test_qtutils.py -q`: exit 1 during pytest configuration with `pytest.PytestRemovedIn8Warning: The --strict option is deprecated, use --strict-markers instead.` No tests ran; rerun with `-o addopts=''` passed.
- `python -m pytest -o addopts='' tests/unit/utils/test_qtutils.py -q`: exit 134 when pytest-qt created a GUI fixture without a display (`Fatal Python error: Aborted`); offscreen rerun passed.
- `QT_QPA_PLATFORM=offscreen python -m pytest -o addopts='' tests/unit/mainwindow/test_tabwidget.py -q`: exit 1, 27 setup/teardown errors before the changed color path. `TabBar._set_icon_size` passes a float to `QSize`, which rejects it (`argument 1 has unexpected type 'float'`). The TabWidget stylesheet behavior remains unverified by this suite.
- A direct import/format check of `TabBar.STYLESHEET` produced `QTabBar { background-color: rgba(255, 0, 0, 255); }`. Importing `WebView` failed with `No module named 'PyQt5.QtWebKit'`, so the WebView stylesheet path cannot be exercised locally.
