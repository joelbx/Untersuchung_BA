Moved `interpolate_color` and `_get_color_percentage` to [qtutils.py](/app/qutebrowser/utils/qtutils.py), updated download and tab progress indicators to use the new location, and redirected the existing interpolation tests.

Verification: all 332 focused tests passed, and `git diff --check` reported no issues.