# Checkpoint

Task: fix PowerShell CLIXML decoding in the checked-out repository.
Status: complete.
Changes: decode UTF-16 escape tokens (including surrogate pairs), preserve controls and unpaired surrogates, select requested stream, concatenate entries within each block, separate nonempty blocks with CRLF. Added focused unit coverage and updated the previous CRLF expectation.
Verification: `python -m pytest -q test/units/plugins/shell/test_powershell.py` passed (10 tests); `git diff --check` passed.
Constraints followed: local code and tests only; git history, index, and harness configuration unchanged.
