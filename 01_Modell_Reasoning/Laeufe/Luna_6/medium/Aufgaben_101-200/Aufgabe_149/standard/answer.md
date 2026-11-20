Implemented support for `--disable-features=` in [qtargs.py](/app/qutebrowser/config/qtargs.py). Enable flags from command-line and configuration sources continue to merge into one entry; disable flags are preserved as separate arguments. Added prefix constants for both flags.

Verification: `pytest -q tests/unit/config/test_qtargs.py` passed (82 tests), and `git diff --check` passed.