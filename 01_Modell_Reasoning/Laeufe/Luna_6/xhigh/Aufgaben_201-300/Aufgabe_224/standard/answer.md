Moved `interpolate_color` and `_get_color_percentage` to [qtutils.py](/app/qutebrowser/utils/qtutils.py), and updated download and tab progress handlers to use `qtutils.interpolate_color`. The helper validates colors and percentages, supports RGB, HSV, and HSL, and preserves the start color’s spec.

Updated the interpolation tests. **337 tests passed**, and `git diff --check` passed.