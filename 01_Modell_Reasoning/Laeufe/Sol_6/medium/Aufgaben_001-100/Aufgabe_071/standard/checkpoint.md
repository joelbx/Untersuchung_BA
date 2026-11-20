# Checkpoint

Task: Fix PowerShell CLIXML decoding in the checked-out repository.

Status: complete. `_parse_clixml` now selects the requested stream, decodes UTF-16 escape tokens including surrogate pairs, preserves decoded control characters and unpaired surrogates, and joins nonempty `<Objs>` results with CRLF. Focused unit tests cover escapes, empty elements, streams, and block boundaries.

Verification: `python -m pytest -q test/units/plugins/shell/test_powershell.py` (8 passed); `git diff --check` passed.
