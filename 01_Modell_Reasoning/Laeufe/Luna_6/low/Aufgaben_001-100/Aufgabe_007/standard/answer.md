Implemented `ansible_winrm_kinit_args` in the WinRM plugin. Its arguments are split into separate tokens and take precedence over the default delegation flag; the principal is appended last. Each authentication attempt continues to use its own `KRB5CCNAME` cache, and both process paths use the same command arguments.

Added coverage for argument parsing, delegation precedence, and distinct cache files.

Verification: `python -m pytest -q test/units/plugins/connection/test_winrm.py` passed (28 tests); `git diff --check` passed.