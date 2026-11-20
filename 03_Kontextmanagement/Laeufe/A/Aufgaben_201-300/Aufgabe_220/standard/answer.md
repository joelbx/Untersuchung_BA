Added `qcolor_to_qsscolor(c: QColor) -> str` in [qtutils.py](/app/qutebrowser/utils/qtutils.py). It formats the color’s red, green, blue, and alpha values as `rgba(r, g, b, a)`. Added tests for named colors, RGB colors, and explicit alpha.

The existing qtutils test file passed with Qt’s offscreen platform: **123 passed**.