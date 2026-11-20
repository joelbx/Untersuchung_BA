# Checkpoint

Task: implement `qcolor_to_qsscolor` in `qutebrowser/utils/qtutils.py` so QColor values serialize as QSS-compatible `rgba(r, g, b, a)` strings.

Completed: added a typed helper that reads QColor's red, green, blue, and alpha components. Named colors, RGB colors with default alpha, and explicit RGBA colors were checked.

Validation: `QT_QPA_PLATFORM=offscreen pytest -o addopts='' -q tests/unit/utils/test_qtutils.py` passed (119 tests). A direct smoke check of four QColor inputs passed. `git diff --check` passed.
