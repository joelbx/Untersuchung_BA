Implemented QtWebEngine feature consolidation in [qtargs.py](/app/qutebrowser/config/qtargs.py). CLI and configured feature flags are extracted, comma-separated values are combined with configuration-required features, and the result contains at most one `--enable-features=` argument. Other backends retain their existing argument behavior.

Added focused coverage in [test_qtargs.py](/app/tests/unit/config/test_qtargs.py).

Validation: `TestQtArgs` passed (58 tests), and `git diff --check` passed. The full test file exited during `TestDarkMode` without a pytest failure summary; the relevant `TestQtArgs` subset passed.