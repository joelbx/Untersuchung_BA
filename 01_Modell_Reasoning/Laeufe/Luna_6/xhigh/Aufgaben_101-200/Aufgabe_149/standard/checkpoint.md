# Checkpoint

Task: resolve missing `--disable-features` support in QtWebEngine argument building.

Implemented:
- Exposed `ENABLE_FEATURES_PREFIX` and `DISABLE_FEATURES_PREFIX` constants.
- Collected and removed both feature switches from the shared Qt argv, merged enable values with generated features, and re-added each disable switch unchanged.
- Added tests for multiple comma-separated enable and disable values through both `--qt-flag` and `qt.args` configuration, including the injected `OverlayScrollbar` feature.

Verification: `python -m pytest tests/unit/config/test_qtargs.py` passed (84 tests); `git diff --check` passed.

Constraints followed: local repository code and tests only; no downloads or delegation; no credentials/private process files/evaluator artifacts read; no git history, index baseline, or harness configuration changes.
