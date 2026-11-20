Moved `interpolate_color` and `_get_color_percentage` to `qtutils`, and updated download and tab progress indicators to call the relocated function. The `None` color space path now validates percentages and preserves the start color’s spec.

All 20 interpolation tests pass. The combined utility test run reported 304 passed, though the process exited with an X server shutdown error afterward.