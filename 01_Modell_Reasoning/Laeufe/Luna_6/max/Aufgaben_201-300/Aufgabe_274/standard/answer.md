Implemented `always`, `auto`, and `never` for the canvas workaround, with `auto` as the default. The resolver enables the flag only for Qt 6 with a known, nonzero Chromium major below 111. Added regression coverage for the requested versions and forced modes.

Verification: **142 tests passed** with `QT_QPA_PLATFORM=offscreen`; `git diff --check` passed.

Updated [configdata.yml](/app/qutebrowser/config/configdata.yml:388), [qtargs.py](/app/qutebrowser/config/qtargs.py:280), and [test_qtargs.py](/app/tests/unit/config/test_qtargs.py:223).