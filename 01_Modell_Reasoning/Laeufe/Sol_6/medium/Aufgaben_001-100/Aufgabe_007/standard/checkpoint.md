# Checkpoint

Task: fix WinRM Kerberos kinit command arguments and execution consistency.
Status: complete.
Changes: added ansible_winrm_kinit_args option; parsed command and argument strings; explicit arguments override the default delegation flag; kept one command line for subprocess and pexpect. Added unit coverage for both paths and unique caches.
Verification: python -m pytest -q test/units/plugins/connection/test_winrm.py (38 passed); git diff --check passed.
