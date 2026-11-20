# Checkpoint

Implemented `qt.workarounds.locale` as a QtWebEngine-only boolean that defaults to false. Added locale `.pak` path lookup and a QtWebEngine 5.15.3 Linux override that checks the active locale before applying Chromium language fallbacks, and adds `--lang=<locale>` to QtWebEngine startup arguments when needed.

Validation: `QT_QPA_PLATFORM=offscreen python -m pytest tests/unit/config/test_qtargs.py tests/unit/config/test_configdata.py -q` passed (148 tests). `git diff --check` passed. The initial run without the offscreen platform aborted during Qt application setup due to the headless environment.
