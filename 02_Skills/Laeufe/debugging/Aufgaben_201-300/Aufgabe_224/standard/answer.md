Moved `interpolate_color` and `_get_color_percentage` to [qtutils.py](/app/qutebrowser/utils/qtutils.py) and updated the download and tab progress callers to use the new location. Added tests for percentage validation and color spec preservation.

The four relevant test suites passed: **336 tests**. `git diff --check` passed. Lint remains unverified because `flake8` is not installed.