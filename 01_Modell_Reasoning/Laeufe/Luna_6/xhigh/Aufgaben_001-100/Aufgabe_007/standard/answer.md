Implemented `ansible_winrm_kinit_args` in [winrm.py](/app/lib/ansible/plugins/connection/winrm.py). Its arguments are split into separate tokens and override automatic `-f`; when unset, delegation still adds `-f`. Both subprocess and pexpect receive the same executable and argument content.

Added tests for argument parsing, precedence, single invocation, and unique `KRB5CCNAME` caches in [test_winrm.py](/app/test/units/plugins/connection/test_winrm.py).

Verification: `pytest -q test/units/plugins/connection/test_winrm.py` — **34 passed**. `git diff --check` passed.