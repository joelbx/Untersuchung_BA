Updated the setting schema to a string enum with default `auto`. The resolver enables the flag only for Qt 6 with a known, nonzero Chromium major below 111; `_qtwebengine_args` now passes version and CLI context through the settings helper.

Verification: **133 tests passed** with `QT_QPA_PLATFORM=offscreen`; five direct resolver cases and `git diff --check` also passed.

Changed [qtargs.py](/app/qutebrowser/config/qtargs.py:276) and [configdata.yml](/app/qutebrowser/config/configdata.yml:388).