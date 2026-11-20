Task: Fix WinRM Kerberos kinit argument handling.
Completed: Added kinit_args option mapped to ansible_winrm_kinit_args; parse arguments with shlex, override default delegation flag when supplied, and keep command construction shared between subprocess and pexpect. Added coverage for multiple arguments, delegation precedence, command invocation, and unique credential cache names.
Verification: python -m pytest test/units/plugins/connection/test_winrm.py -q (30 passed); git diff --check passed.
