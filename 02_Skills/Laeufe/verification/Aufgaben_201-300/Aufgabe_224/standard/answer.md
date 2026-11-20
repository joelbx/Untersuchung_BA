Moved `interpolate_color` and `_get_color_percentage` to `qtutils`, and updated download and tab progress indicators to use the new location. The relocated helper retains RGB, HSV, and HSL interpolation, validates colors and percentages, and preserves the start color’s spec.

Verification: **345 relevant tests passed** with Qt offscreen; `git diff --check` passed.