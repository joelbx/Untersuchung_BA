# Checkpoint

Completed: moved `_get_color_percentage` and `interpolate_color` into `qutebrowser.utils.qtutils`, preserving their signatures and RGB/HSV/HSL behavior. The relocated function validates colors and rejects percentages outside 0–100 and unsupported color spaces. Updated download and tab progress call sites and migrated the existing interpolation unit tests to `qtutils`.

Verification: `tests/unit/utils/test_utils.py` passed (178 tests); `tests/unit/browser/test_downloads.py` and `tests/unit/mainwindow/test_tabbedbrowser.py` passed (28 tests); `git diff --check` passed.
