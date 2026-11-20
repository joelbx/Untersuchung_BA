Task: Fix GUI process error messages.
Status: Implemented per-error wording, command inclusion, and Unix startup hint. Added unit coverage for all requested codes and both hint details.
Verification: 28 tests in tests/unit/misc/test_guiprocess.py passed; pytest process exited 1 afterward due Xvfb XIO shutdown error. git diff --check passed.
