# WinRM Kerberos kinit fix

Status: complete.

The plugin now accepts `ansible_winrm_kinit_args`, tokenizes it, and builds one command line for subprocess and pexpect. The existing unique credential cache is covered by a new test for both paths. Documentation and changelog were updated.

Verification: `python -m pytest -q test/units/plugins/connection/test_winrm.py` (37 passed); `git diff --check` passed.
