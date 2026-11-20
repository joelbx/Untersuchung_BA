# Checkpoint

Task: support both QtWebEngine feature flags, merge enabled features, preserve disabled flags.

Implemented in `qutebrowser/config/qtargs.py`: added `ENABLE_FEATURES_PREFIX` and `DISABLE_FEATURES_PREFIX`, collected both feature flag kinds from command line and config, merged enabled values into one flag, and emitted disabled flags unchanged and separately. Added coverage for mixed sources, comma-separated values, multiple flags, overlay injection, and disabled-only input in `tests/unit/config/test_qtargs.py`.

Verification: `python -m pytest tests/unit/config/test_qtargs.py -q` passed (92 tests). `git diff --check` passed.
