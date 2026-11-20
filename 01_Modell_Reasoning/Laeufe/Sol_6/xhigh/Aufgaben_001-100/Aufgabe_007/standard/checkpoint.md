# WinRM Kerberos kinit fix

Status: complete. Added the `ansible_winrm_kinit_args` option, parsed its arguments with `shlex.split`, and shared the same command tokens between subprocess and pexpect. Explicit arguments override the default delegation flag; absent arguments retain it. Documented the option and added tests for both execution paths, precedence, argument parsing, and distinct credential caches per attempt.

Verification: `python -m pytest test/units/plugins/connection/test_winrm.py -q` (35 passed); `git diff --check` passed.
