# Checkpoint

Issue: relocate Qt color interpolation helpers to `qutebrowser.utils.qtutils` and update download and tab progress call sites and tests.

Completed: moved both helpers into `qtutils.py`, updated the three production calls, and moved interpolation tests into `test_qtutils.py`. The helper now rejects percentages outside 0–100 even when the color system is `None`, and preserves the start color spec in that mode.

Verification: 338 relevant tests passed with exit code 0 using `DISPLAY=:99 QT_QPA_PLATFORM=offscreen python -m pytest -q -p no:xvfb -o addopts='' tests/unit/utils/test_qtutils.py tests/unit/utils/test_utils.py tests/unit/browser/test_downloads.py tests/unit/mainwindow/test_tabbedbrowser.py`. `git diff --check` passed.
