# Checkpoint

Implemented the documented `kinit_args` option in the WinRM connection plugin. Explicit arguments are split into argv tokens and override automatic delegation `-f`; the default delegation behavior remains when the option is unset. Both subprocess and pexpect use the same executable and argv content, and each authentication attempt retains its own temporary credential cache via `KRB5CCNAME`.

Added unit coverage for custom executable and arguments, delegation precedence, empty explicit arguments, invocation counts, and cache uniqueness. Verification passed: `pytest -q test/units/plugins/connection/test_winrm.py` (34 passed), and `git diff --check`.
