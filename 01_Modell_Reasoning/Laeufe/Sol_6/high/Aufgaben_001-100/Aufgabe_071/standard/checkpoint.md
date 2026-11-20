# Checkpoint

- Issue: decode PowerShell CLIXML `_xDDDD_` escapes, preserve stream filtering and block boundaries.
- Located implementation in `lib/ansible/plugins/shell/powershell.py` and existing unit tests in `test/units/plugins/shell/test_powershell.py`.
- Updated the parser to decode UTF-16 escape units, combine surrogate pairs, preserve lone surrogates in UTF-8 bytes, and join matching stream text at block boundaries.
- Extended the existing unit tests for escapes, empty entries, stream filtering, and multiple blocks.
- Verification: `python -m pytest test/units/plugins/shell -q` passed (21 tests); `git diff --check` passed.
