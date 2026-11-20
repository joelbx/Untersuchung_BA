# Checkpoint

Task: add `qcolor_to_qsscolor` to `qutebrowser/utils/qtutils.py` and use it where the WebView and TabBar build QSS background colors.

Initial state: working tree clean. `rg` is unavailable, so repository inspection used `grep` and `find`.

Implemented: `qcolor_to_qsscolor` formats `QColor.getRgb()` as `rgba(r, g, b, a)`. WebView and TabBar now apply QSS background colors through class `STYLESHEET` templates while retaining their palette updates. Added utility cases for named, RGB, and RGBA colors, plus a TabBar config update test with alpha.

Verification: the final targeted run passed all 124 tests. `py_compile` and `git diff --check` passed. The existing TabWidget tests fail during setup at an unchanged `_set_icon_size` call, where installed PyQt rejects a float passed to `QSize`. PyQt5.QtWebKitWidgets is absent, so WebView cannot be imported for a runtime test in this environment.
