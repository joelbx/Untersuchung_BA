# Process outcome message fix

Implemented signal aware process outcomes: SIGTERM gets a terminated state and silent finish unless verbose; crashes with a known signal include its name, while crashes with an unknown code retain the generic wording. Finished messages include the process instance PID. Updated unit tests and the spawn and hint feature expectations.

Validation: `xvfb-run -a env QUTE_QT_WRAPPER=PyQt6 QT_QPA_PLATFORM=offscreen pytest -p no:xvfb -q tests/unit/misc/test_guiprocess.py tests/unit/browser/test_qutescheme.py` passed (72 tests). The focused spawn end to end scenario matched the new message, but its teardown reported an offscreen Qt warning (`This plugin does not support raise()`). The full spawn end to end run could not start Chromium as root without disabling its sandbox; a subsequent focused run with `QTWEBENGINE_DISABLE_SANDBOX=1` reached and passed the scenario before that Qt warning. `git diff --check` passed.
