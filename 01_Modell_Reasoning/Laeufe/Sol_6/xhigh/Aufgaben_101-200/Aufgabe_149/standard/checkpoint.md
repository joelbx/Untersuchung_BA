# Checkpoint

- Task: support `--disable-features=` in QtWebEngine argument building while merging enabled features with configuration additions.
- Starting state: working tree clean; relevant implementation appears in `qutebrowser/config/qtargs.py` and tests in `tests/unit/config/test_qtargs.py`.
- Implemented: added `ENABLE_FEATURES_PREFIX` and `DISABLE_FEATURES_PREFIX`; collect both flag types, merge enabled values with injected features, and pass disabled flags through unchanged.
- Verification: `python -m pytest -q tests/unit/config/test_qtargs.py` passed (93 tests).
