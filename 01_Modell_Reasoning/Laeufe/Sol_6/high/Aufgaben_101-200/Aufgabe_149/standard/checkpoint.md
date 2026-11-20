# Checkpoint

Issue: propagate `--disable-features` through QtWebEngine argument building while merging enabled features into one flag.

Status: implemented module prefix constants and explicit handling for enable and disable feature flags. Enabled values are merged with internally injected features; disable flags are preserved as separate, unchanged arguments. Added tests for both command-line and configuration sources, comma-separated lists, and disable-only flags.

Verification: `python -m pytest tests/unit/config/test_qtargs.py -q` passed (88 tests); `git diff --check` passed.
