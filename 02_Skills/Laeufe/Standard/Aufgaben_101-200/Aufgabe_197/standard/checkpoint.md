# Checkpoint

Resolved the Qt 6.4 dark mode text threshold mapping in `qutebrowser/browser/webengine/darkmode.py`. QtWebEngine 6.4 and later select a dedicated variant that emits `ForegroundBrightnessThreshold`; earlier versions keep `TextBrightnessThreshold`. Added version-specific regression coverage in `tests/unit/browser/webengine/test_darkmode.py`.

Checks:
- `QT_QPA_PLATFORM=offscreen python -m pytest tests/unit/browser/webengine/test_darkmode.py -q` — 43 passed.
- `git diff --check` — passed.

Initial `rg` search was unavailable (`/bin/bash: rg: command not found`); local `grep` and `find` were used instead.
