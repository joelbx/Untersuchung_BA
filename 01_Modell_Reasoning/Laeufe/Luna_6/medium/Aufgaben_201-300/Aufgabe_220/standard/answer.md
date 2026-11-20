Implemented `qcolor_to_qsscolor` in [qtutils.py](/app/qutebrowser/utils/qtutils.py:79). It formats QColor’s resolved RGBA components, including alpha, as `rgba(r, g, b, a)`.

Validation passed: all 119 tests in `tests/unit/utils/test_qtutils.py`. The checked-out WebView and TabBar files do not contain the described `STYLESHEET` templates.