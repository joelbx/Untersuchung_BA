Added `qcolor_to_qsscolor` in [qtutils.py](/app/qutebrowser/utils/qtutils.py). It returns `rgba(r, g, b, a)` for named colors, RGB colors, and colors with an explicit alpha value.

Added four cases in [test_qtutils.py](/app/tests/unit/utils/test_qtutils.py); all four pass.