# Checkpoint

Task: Move Qt color interpolation helpers to `qutebrowser.utils.qtutils`, update progress indicator call sites, and run relevant existing tests.

Status: Complete. Moved both color helpers to `qtutils`, updated download and tab progress call sites, and moved interpolation tests alongside the helper. Added progress and edge case regression coverage.

Verification: `DISPLAY=:99 QT_QPA_PLATFORM=offscreen pytest -p no:xvfb -q tests/unit/utils/test_qtutils.py tests/unit/utils/test_utils.py tests/unit/browser/test_downloads.py tests/unit/mainwindow/test_tabbedbrowser.py` passed (344 tests). `git diff --check` passed.
