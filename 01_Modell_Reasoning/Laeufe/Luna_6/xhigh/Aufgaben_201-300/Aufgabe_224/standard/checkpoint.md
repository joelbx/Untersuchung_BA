# Checkpoint

Task: resolve the missing `interpolate_color` helper after its Qt utility refactor.

Completed:
- Moved `_get_color_percentage` and `interpolate_color` from `utils.py` to `qtutils.py`.
- Preserved RGB, HSV, and HSL interpolation; ensured invalid percentages and colorspaces raise `ValueError`, input colors are checked with `ensure_valid`, and output uses the start color's spec.
- Updated download and tab load progress/finished handlers to use `qtutils.interpolate_color`.
- Updated interpolation tests, including invalid percentages when interpolation is disabled and start-spec preservation.

Verification: `python -m pytest tests/unit/utils/test_utils.py tests/unit/utils/test_qtutils.py tests/unit/browser/test_downloads.py tests/unit/mainwindow/test_tabbedbrowser.py` — 337 passed. `git diff --check` passed.
