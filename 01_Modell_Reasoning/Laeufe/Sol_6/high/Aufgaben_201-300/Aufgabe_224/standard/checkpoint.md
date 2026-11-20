# Color interpolation relocation

Status: complete.

Found `interpolate_color` and `_get_color_percentage` in `qutebrowser/utils/utils.py`. Runtime callers in downloads and tabbedbrowser still use `utils.interpolate_color`; existing unit tests are in `tests/unit/utils/test_utils.py`.

Moved both helpers to `qtutils.py`, updated the download and tab progress callers, and moved interpolation tests to `test_qtutils.py`. Added coverage for invalid percentages with no gradient and for preserving the start color spec.

Verification: `xvfb-run -a python -m pytest -q -p no:xvfb tests/unit/utils/test_qtutils.py tests/unit/utils/test_utils.py tests/unit/browser/test_downloads.py tests/unit/mainwindow/test_tabbedbrowser.py` passed (338 tests). `git diff --check` passed.
