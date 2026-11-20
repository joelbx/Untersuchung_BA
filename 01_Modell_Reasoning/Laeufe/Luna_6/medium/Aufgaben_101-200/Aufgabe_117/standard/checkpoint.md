# Checkpoint

Implemented `qt.workarounds.locale` (QtWebEngine only, false by default), locale `.pak` path lookup, Chromium locale fallback selection, and `--lang` startup argument injection gated to Linux with QtWebEngine 5.15.3.

Verification: `QT_QPA_PLATFORM=offscreen python -m pytest tests/unit/config/test_qtargs.py -q` passed (117 tests); `git diff --check` passed. A regular pytest invocation and an `xvfb-run` invocation aborted while creating Qt's application in this environment; offscreen mode runs the suite successfully.
