# Checkpoint

Implemented `qcolor_to_qsscolor(c: QColor) -> str` using `QColor.getRgb()`, preserving all four 8-bit channels. Added WebView and TabBar multi-line QSS background templates and wired them to the conversion function while preserving existing palette updates. Added utility tests for named colors, RGB, RGBA, and zero alpha.

Verification: all 124 tests in `tests/unit/utils/test_qtutils.py` pass with `-o addopts=''`. Qt accepted the generated RGBA string and exposed the same RGBA values in a QWidget palette. Python compilation and `git diff --check` pass. Existing TabWidget tests cannot reach the modified code because setup fails on a pre-existing float passed to `QSize` in `_set_icon_size`; QtWebKit is unavailable locally, so WebView runtime tests cannot run.
