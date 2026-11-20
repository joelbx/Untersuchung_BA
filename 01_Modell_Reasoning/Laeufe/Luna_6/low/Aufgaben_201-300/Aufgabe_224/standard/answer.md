Moved `_get_color_percentage` and `interpolate_color` into [qtutils.py](/app/qutebrowser/utils/qtutils.py), and updated the download and tab progress callers to use `qtutils.interpolate_color`. Updated the existing interpolation tests to exercise the new module.

Verification: **332 relevant tests passed** across the utility, download, and tabbed browser test files; `git diff --check` passed.