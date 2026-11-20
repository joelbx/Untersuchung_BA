Task: support --disable-features in QtWebEngine argument building while preserving enable merging.
Done: defined ENABLE_FEATURES_PREFIX and DISABLE_FEATURES_PREFIX; collected both feature flag types from command line and configuration; merged enable values into one flag; passed each disable flag through unchanged. Added tests for command-line, config, mixed inputs, comma-separated values, overlay merge, and disable-only case.
Verification: pytest -q tests/unit/config/test_qtargs.py -> 86 passed. git diff --check -> clean.
Delegation: none.
