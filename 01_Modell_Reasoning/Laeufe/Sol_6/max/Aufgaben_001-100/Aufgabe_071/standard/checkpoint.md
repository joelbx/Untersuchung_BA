# Checkpoint

Task: Fix PowerShell CLIXML escape decoding in the checked-out repository.

Status: Complete. Updated the parser to decode CLIXML UTF-16 escape tokens, preserve surrogate code units, select the requested stream, and join text by object block. Added focused unit coverage for escapes, stream selection, empty elements, and block boundaries.

Verification: `python -m pytest test/units/plugins/shell/test_powershell.py -q` (11 passed); `git diff --check` (passed).
