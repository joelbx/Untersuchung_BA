# Checkpoint

Task: Fix WinRM custom kinit command handling and add ansible_winrm_kinit_args.

Completed: Added the option, tokenized command and argument strings, preserved delegation defaults only when no explicit arguments are supplied, and shared one command line across subprocess and pexpect. Added unit cases for the reported command, argument precedence, one invocation, and unique cache files. Updated documentation and changelog.

Verification: `python -m pytest -q test/units/plugins/connection/test_winrm.py` passed (36 tests); `git diff --check` passed.
