Implemented the WinRM kinit fix. The plugin now splits command strings into executable and arguments, supports `ansible_winrm_kinit_args`, and gives explicit arguments precedence over automatic delegation `-f`. Subprocess and pexpect use the same argv content.

Added coverage for argument parsing and precedence in both execution paths.

Validation: `python -m pytest -q test/units/plugins/connection/test_winrm.py` passed (32 tests); `git diff --check` passed.

Changed: [winrm.py](/app/lib/ansible/plugins/connection/winrm.py), [test_winrm.py](/app/test/units/plugins/connection/test_winrm.py).