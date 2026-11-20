Updated [_parse_clixml](/app/lib/ansible/plugins/shell/powershell.py:32) to decode CLIXML escapes, preserve control characters and unpaired surrogates, filter by stream, and separate nonempty `<Objs>` results with CRLF.

Added regression coverage in [test_powershell.py](/app/test/units/plugins/shell/test_powershell.py:77).

Verification: focused tests passed (9 tests); `git diff --check` passed.