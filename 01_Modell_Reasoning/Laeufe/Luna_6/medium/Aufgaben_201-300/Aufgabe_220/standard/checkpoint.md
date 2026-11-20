# Checkpoint

Implemented `qcolor_to_qsscolor(c: QColor) -> str` in `qutebrowser/utils/qtutils.py`. It formats QColor's resolved red, green, blue, and alpha components as `rgba(r, g, b, a)`.

Validation: `QT_QPA_PLATFORM=offscreen python -m pytest -o addopts='' tests/unit/utils/test_qtutils.py -q` passed (119 tests). Without the offscreen setting Qt aborted during display initialization; the successful offscreen run covers the full focused test module.

Repository note: this checked-out version has no `STYLESHEET` templates in the named WebView/TabBar files.
