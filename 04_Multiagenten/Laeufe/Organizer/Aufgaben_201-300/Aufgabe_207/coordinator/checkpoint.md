Issue: consolidate QtWebEngine --enable-features arguments across CLI, qt.args, and configuration.
Status: implementation and regression tests complete.
Tests: 79 passed in tests/unit/config/test_qtargs.py with test_new_chromium excluded; that existing Chromium version probe segfaults in Qt native code (exit 139).
Delegation: none.
