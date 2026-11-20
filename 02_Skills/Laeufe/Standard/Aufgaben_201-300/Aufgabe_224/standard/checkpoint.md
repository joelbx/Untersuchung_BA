# Checkpoint

Issue: relocate Qt color interpolation helpers into `qutebrowser/utils/qtutils.py` and update progress indicator call sites.

Initial repository scan: both helpers remain in `utils.py`; downloads and tabbed browser call `utils.interpolate_color`; existing interpolation tests are in `tests/unit/utils/test_utils.py`. Working tree was clean. `rg` is unavailable, so searches use `grep`.

Completed: moved `_get_color_percentage` and `interpolate_color` to `qtutils.py`, updated download and tab progress callers, and moved interpolation tests to `test_qtutils.py`. The no-gradient path now validates percent and preserves the start color spec.

Verification: `python -m pytest -q tests/unit/utils/test_qtutils.py tests/unit/utils/test_utils.py tests/unit/browser/test_downloads.py tests/unit/mainwindow/test_tabbedbrowser.py` passed (338 tests). The focused interpolation run passed (23 tests). `git diff --check` passed after whitespace cleanup.
