# Checkpoint

Implemented `ansible_winrm_kinit_args` in the WinRM connection plugin. The arguments are shell-tokenized and appended after the configured executable, followed by the principal. Explicit arguments suppress the automatic `-f`; delegation still adds `-f` when no explicit arguments are configured. Both subprocess and pexpect receive the same argv content, and the existing per-attempt unique `FILE:` credential cache environment handling remains in place.

Validation: `python -m pytest -q test/units/plugins/connection/test_winrm.py` passed (26 tests); `git diff --check` passed.
