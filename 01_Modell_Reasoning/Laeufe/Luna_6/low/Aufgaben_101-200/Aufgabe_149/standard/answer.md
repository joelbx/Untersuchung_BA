Added exported prefix constants and tests confirming that comma-separated `--disable-features` values pass through from both command-line and configuration inputs. Existing enable-feature merging remains in place, producing one combined enable flag.

All 85 tests in `tests/unit/config/test_qtargs.py` pass.