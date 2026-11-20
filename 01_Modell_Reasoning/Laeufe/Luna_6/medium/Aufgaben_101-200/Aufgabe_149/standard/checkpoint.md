# Checkpoint

Implemented QtWebEngine feature flag handling in `qutebrowser/config/qtargs.py`:
- Added module prefix constants for enable and disable feature flags.
- Collected enable flags from the combined argv sources and retained existing merging with injected features.
- Collected and propagated disable flags unchanged as separate arguments.

Verification: `pytest -q tests/unit/config/test_qtargs.py` passed (82 tests); `git diff --check` passed.
