# Checkpoint

Implemented `qutebrowser.utils.qtutils.qcolor_to_qsscolor(c: QColor) -> str` using `QColor.getRgb()` to preserve RGB and alpha integer values in `rgba(r, g, b, a)` format.

Validation: the existing `tests/unit/utils/test_qtutils.py` suite passed (119 tests) with `QT_QPA_PLATFORM=offscreen` and `-o addopts=''`. A direct smoke check also passed for named red and blue, and explicit RGBA values. `git diff --check` passed.

The WebView and TabBar stylesheet templates mentioned in the issue description are not present in this checkout; these classes currently use palette APIs.
