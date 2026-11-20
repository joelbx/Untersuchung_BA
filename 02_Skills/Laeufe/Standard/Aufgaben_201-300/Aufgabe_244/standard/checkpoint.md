# Checkpoint

Task: Fix the dark mode foreground threshold option and QtWebEngine 6.4 key selection.

Completed:
- Added `colors.webpage.darkmode.threshold.foreground` as an Int option with default 256 and mapped the old `threshold.text` name through config migrations.
- Mapped the new option to Chromium `TextBrightnessThreshold` before QtWebEngine 6.4 and `ForegroundBrightnessThreshold` from 6.4 onward.
- Updated settings documentation and added version and migration tests.

Checks:
- `QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/browser/webengine/test_darkmode.py tests/unit/config/test_configdata.py tests/unit/config/test_configfiles.py`: 304 passed, 1 skipped.
- `git diff --check`: passed.
- Initial `python -m pytest -q tests/unit/browser/webengine/test_darkmode.py tests/unit/config/test_configdata.py` aborted (exit 134) during `pytestqt/plugin.py` qapp fixture creation with `Fatal Python error: Aborted`, before assertions. Retried successfully with `QT_QPA_PLATFORM=offscreen`.

Limit: local QtWebEngine runtime is 5.15.2; the 6.4 behavior is verified with simulated version values in unit tests, not a 6.4 runtime.
