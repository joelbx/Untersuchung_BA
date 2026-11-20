# Checkpoint

Task: support simultaneous QtWebEngine enable and disable feature flags.

Changes:
- Added `ENABLE_FEATURES_PREFIX` and `DISABLE_FEATURES_PREFIX` constants in `qutebrowser/config/qtargs.py`.
- Collect both feature flag types from command-line and config arguments. Merge enabled features with injected features into one flag; pass each disabled feature flag through unchanged.
- Added tests for all source combinations, comma-separated values, multiple flags, and disable-only input.

Verification:
- `python -m pytest -q tests/unit/config/test_qtargs.py`: 89 passed (exit 0).
- `git diff --check`: exit 0.
- `python -m flake8 qutebrowser/config/qtargs.py tests/unit/config/test_qtargs.py`: unavailable (exit 1, `/usr/local/bin/python: No module named flake8`). Style-lint status is unverified because flake8 is not installed. No downloads attempted.
