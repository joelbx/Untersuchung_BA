Task: Consolidate QtWebEngine --enable-features arguments from CLI, qt.args, and qutebrowser-required features.
Status: Implemented in qutebrowser/config/qtargs.py with regression coverage in tests/unit/config/test_qtargs.py.
Behavior: QtWebEngine extracts existing equals-form feature flags, combines comma-separated user features with the configured OverlayScrollbar feature, and emits one flag when features exist. QtWebKit argument behavior is unchanged.
Verification: 79 tests passed in tests/unit/config/test_qtargs.py with test_new_chromium deselected; that existing test terminates under root because Chromium refuses to run without --no-sandbox. git diff --check passed.
