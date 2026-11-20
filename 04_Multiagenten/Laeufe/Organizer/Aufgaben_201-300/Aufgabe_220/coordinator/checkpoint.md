Task: QColor to QSS rgba conversion.
Implemented: qtutils.qcolor_to_qsscolor using QColor.getRgb(); WebView and TabBar background QSS templates and call sites; parameterized utility tests for named, RGB, and RGBA colors.
Verification: tests/unit/utils/test_qtutils.py passed (123); TabBar QSS formatting smoke check passed; compileall and git diff --check passed. TabWidget suite blocked during existing _set_icon_size: QSize receives float. WebKit widget import unavailable because PyQt5.QtWebKit is not installed.
Delegation: none.
