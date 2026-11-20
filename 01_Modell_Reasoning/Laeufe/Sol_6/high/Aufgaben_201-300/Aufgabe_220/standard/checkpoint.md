# Checkpoint

Implemented `qcolor_to_qsscolor(c: QColor) -> str` using the integer channels from `QColor.getRgb()`.

Added WebView and TabBar stylesheet templates and applied converted configured background colors when those widgets update their palettes. Added cases for named colors, RGB, and explicit alpha in `tests/unit/utils/test_qtutils.py`.

Verification: `tests/unit/utils/test_qtutils.py` passes (123 tests) using `-o addopts=''` because the repository's `--strict` pytest flag is deprecated under the installed pytest. Edited modules compile and `git diff --check` passes. `tests/unit/mainwindow/test_tabwidget.py` cannot reach the color code: setup fails in unchanged `_set_icon_size` because it passes a float to `QSize` with this PyQt build.
