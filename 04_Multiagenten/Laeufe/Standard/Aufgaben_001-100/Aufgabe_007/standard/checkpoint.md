# Checkpoint

Task: Fix WinRM Kerberos kinit command construction and add kinit_args support.
Status: Complete.
Changes: Added ansible_winrm_kinit_args option, parsed executable and argument strings with shlex, preserved delegation defaults only when kinit_args is unset, and kept the same command line for subprocess and pexpect. Added tests for command parsing, precedence, single invocation, and distinct credential caches.
Verification: `python -m pytest -q test/units/plugins/connection/test_winrm.py` (36 passed); `git diff --check` passed.
