# Checkpoint

Task: add support for `--disable-features=` alongside merged `--enable-features=` QtWebEngine arguments.

Status: implemented both public feature prefix constants, unified detection for QtWebEngine feature flags, merging of enable flags, and unchanged propagation of disable flags. Added tests for command line, config, mixed, and disable only cases.

Verification: `pytest -q tests/unit/config/test_qtargs.py` passed (86 tests); `git diff --check` passed.
