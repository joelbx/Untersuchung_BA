# Checkpoint

Issue: QtWebEngine argument construction must support enable and disable feature flags from both command line and configuration, merge enabled features into one flag, and preserve disabled flags separately.

Implementation: `qutebrowser/config/qtargs.py` now exposes enable/disable prefix constants, consolidates enabled feature entries with injected features, and forwards each disable entry unchanged.

Verification: `pytest -q tests/unit/config/test_qtargs.py` passed (82 tests). A direct smoke check covered comma-separated enable/disable values from both `--qt-flag` and `qt.args`, including the merged overlay scrollbar feature. `git diff --check` passed.

Status: Complete.
