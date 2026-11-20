Moved `interpolate_color` and its helper to [qtutils.py](/app/qutebrowser/utils/qtutils.py:177) and updated the download and tab progress callers. Interpolation retains RGB, HSV, and HSL support, validates colors and percentages, and preserves the start color’s spec.

Updated the tests; **344 relevant tests passed**. `git diff --check` passed.