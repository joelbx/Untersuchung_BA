Task: Resolve the missing `interpolate_color` helper after its Qt utility refactor.

Initial inspection: The repository is present at `/app`; `rg` is unavailable in the shell, so inspection used `find` and standard text-search tools.

Changes made: Moved `_get_color_percentage` and `interpolate_color` from `utils.py` into `qtutils.py`; kept RGB, HSV, HSL, and `None` behavior, added explicit 0–100 validation, and preserved the start QColor spec. Updated download and tab progress call sites and redirected the existing interpolation tests to `qtutils`.

Verification: `pytest -q tests/unit/utils/test_utils.py tests/unit/browser/test_downloads.py tests/unit/mainwindow/test_tabbedbrowser.py` passed (206 tests); `pytest -q tests/unit/utils/test_qtutils.py` passed (126 tests). `git diff --check` passed, and no production call sites use `utils.interpolate_color`.
