Moved `_get_color_percentage` and `interpolate_color` to `qtutils`, and updated download and tab progress indicators to use the relocated helper. The existing interpolation tests now target `qtutils`.

Verification passed: 178 utility tests, 28 download and tabbed browser tests, and `git diff --check`.