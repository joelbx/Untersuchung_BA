# Checkpoint

Task: Add support for merging QtWebEngine `--enable-features` and `--disable-features` arguments from command line and configuration.

Implemented in `qutebrowser/config/qtargs.py`: exported exact prefix constants, consolidated enabled feature values with injected features, and preserved disable flags as separate arguments. Added coverage for comma-separated enable/disable lists supplied via either command line or `qt.args` configuration.

Verification: `pytest -q tests/unit/config/test_qtargs.py` passed (84 tests).
