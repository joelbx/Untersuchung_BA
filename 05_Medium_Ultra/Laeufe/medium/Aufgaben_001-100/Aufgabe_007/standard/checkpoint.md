Task: Fix WinRM Kerberos kinit argument handling.
Status: Complete.
Changes: Added ansible_winrm_kinit_args option; tokenizes arguments, gives them precedence over the default delegation flag, and uses one command line for subprocess and pexpect. Added tests for custom flags, delegation precedence, empty arguments, single invocation, and unique credential caches in both execution paths.
Verification: python -m pytest test/units/plugins/connection/test_winrm.py -q (34 passed); git diff --check.
