# Checkpoint

- Task: support `--disable-features=` in QtWebEngine arguments while preserving enable-feature merging.
- Repository status at start: clean.
- Located implementation in `qutebrowser/config/qtargs.py` and existing tests in `tests/unit/config/test_qtargs.py`.
- Updated `qutebrowser/config/qtargs.py` with exposed enable/disable prefix constants, one merged enable flag, and unchanged forwarding of each disable flag.
- Added tests for command line and config sources, comma-separated disabled values, overlay injection, and mixed-source flags.
- Verification: `pytest -q tests/unit/config/test_qtargs.py` passed (88 tests); `git diff --check` passed.
