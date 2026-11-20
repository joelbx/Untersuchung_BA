Moved `interpolate_color` and `_get_color_percentage` to `qtutils`, updated the download and tab progress callers, and moved the color tests to `test_qtutils.py`. The helper now validates percentages even when the gradient is disabled and preserves the start color’s spec.

Verification: 336 relevant tests passed; `git diff --check` is clean.