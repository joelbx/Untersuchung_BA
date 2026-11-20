# Checkpoint

Completed: moved `_get_color_percentage` and `interpolate_color` from `utils.py` to `qtutils.py`; updated download and tab progress callers; moved interpolation tests to `test_qtutils.py` and added coverage for disabled-gradient percentage bounds and start color spec.

Verification: `DISPLAY=:99 QT_QPA_PLATFORM=offscreen python -m pytest -p no:xvfb -q tests/unit/utils/test_qtutils.py tests/unit/utils/test_utils.py tests/unit/browser/test_downloads.py tests/unit/mainwindow/test_tabbedbrowser.py` — 336 passed. `git diff --check` — clean.
