# Checkpoint

Implemented WinRM kinit command parsing and the `ansible_winrm_kinit_args` option. Explicit arguments override automatic `-f`; subprocess and pexpect receive the same argv content, with one principal appended. Existing per-attempt temporary credential caches remain exposed via `KRB5CCNAME`.

Validation: `python -m pytest -q test/units/plugins/connection/test_winrm.py` passed (32 tests); `git diff --check` passed.
