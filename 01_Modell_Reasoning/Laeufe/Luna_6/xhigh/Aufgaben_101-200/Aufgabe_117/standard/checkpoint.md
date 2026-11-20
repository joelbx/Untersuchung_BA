# Checkpoint

Task: implement the QtWebEngine 5.15.3 locale fallback workaround in `/app`.

Completed:
- Added `qt.workarounds.locale` as an opt-in, restart-required, QtWebEngine-only setting; updated settings help.
- Added locale pack path, locale normalization, Chromium regional mapping, and fallback selection.
- Added `--lang=<fallback>` to QtWebEngine startup arguments only when enabled on Linux with exactly QtWebEngine 5.15.3 and the full locale pack is missing.

Validation:
- `QT_QPA_PLATFORM=offscreen python -m pytest tests/unit/config/test_qtargs.py tests/unit/config/test_configdata.py -q` — 148 passed.
- `git diff --check` — passed.

The ordinary headless pytest invocation aborted while creating the Qt application; setting Qt to the offscreen platform allowed the focused suites to run successfully.
