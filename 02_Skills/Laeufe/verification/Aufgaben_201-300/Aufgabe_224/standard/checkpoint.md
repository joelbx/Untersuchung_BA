# Checkpoint

Task: relocate Qt color interpolation helpers into `qutebrowser.utils.qtutils` and update download/tab progress call sites.

Changes:
- Moved `_get_color_percentage` and `interpolate_color` from `utils.py` to `qtutils.py`.
- Updated download and tab progress/finished indicators to call `qtutils.interpolate_color`.
- Moved interpolation tests to `test_qtutils.py`; added boundary/spec and progress call-site tests.

Verification:
- `DISPLAY=:99 QT_QPA_PLATFORM=offscreen python -m pytest -q -p no:xvfb tests/unit/browser/test_downloads.py tests/unit/mainwindow/test_tabbedbrowser.py tests/unit/utils/test_qtutils.py tests/unit/utils/test_utils.py` — exit 0, 345 passed.
- `git diff --check` — exit 0.

Tooling notes:
- Initial inspection command using `rg` failed with `/bin/bash: rg: command not found`; used `grep`/`find` instead.
- With the Xvfb plugin enabled, `QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/utils/test_qtutils.py tests/unit/utils/test_utils.py tests/unit/browser/test_downloads.py tests/unit/mainwindow/test_tabbedbrowser.py` reported 338 passed but exited 1 after `XIO: fatal IO error 0 (Success) on X server ":0"` during teardown. The offscreen run above with the Xvfb plugin disabled exited 0.
- Without Xvfb, the repository's `check_display` fixture requires a nonempty `DISPLAY`. The successful command sets `DISPLAY=:99` while `QT_QPA_PLATFORM=offscreen` keeps Qt offscreen.
