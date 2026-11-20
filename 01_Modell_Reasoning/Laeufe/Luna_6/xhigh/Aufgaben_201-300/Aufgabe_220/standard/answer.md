Added `qcolor_to_qsscolor` in [qtutils.py](/app/qutebrowser/utils/qtutils.py:115). It formats QColor’s red, green, blue, and alpha components as `rgba(r, g, b, a)`.

Validation passed: the focused Qt utility suite (119 tests) and a smoke check covering named colors, RGB, and RGBA inputs.