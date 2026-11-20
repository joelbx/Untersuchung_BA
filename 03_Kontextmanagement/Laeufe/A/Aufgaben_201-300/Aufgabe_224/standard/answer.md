Moved `interpolate_color` and `_get_color_percentage` to [qtutils.py](/app/qutebrowser/utils/qtutils.py:177), and updated download and tab progress indicators to use the relocated function. The `colorspace=None` path now validates percentages and preserves the start color’s spec.

The related test suites passed: **335 tests**.