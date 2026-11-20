# Checkpoint

Implemented version-aware `disable_accelerated_2d_canvas` modes.

- Config schema now accepts `always`, `auto`, and `never`, with `auto` as the default.
- WebEngine settings receive versions, parsed CLI namespace, and special flags; callable setting values resolve to a mapped enum value.
- Automatic mode enables the flag only on Qt 6 with a known, non-zero Chromium major below 111.

Verification: `QT_QPA_PLATFORM=offscreen QTWEBENGINE_DISABLE_SANDBOX=1 pytest -q tests/unit/config/test_qtargs.py` passed (102 tests). `python -m py_compile qutebrowser/config/qtargs.py` and `git diff --check` passed. Running pytest without the offscreen environment aborted while initializing Qt's application fixture.
