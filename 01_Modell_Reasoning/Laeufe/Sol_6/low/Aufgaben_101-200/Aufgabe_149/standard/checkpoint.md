Issue: QtWebEngine feature flags.
Completed: Exposed enable/disable prefix constants; enable flags are merged with injected features, while disable flags are retained verbatim. Added command-line/configuration regression coverage.
Verification: pytest -q tests/unit/config/test_qtargs.py (84 passed).
