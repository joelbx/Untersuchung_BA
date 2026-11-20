Updated `_parse_clixml` to decode CLIXML escapes, including surrogate pairs and control characters, filter by stream, handle empty elements, and join results with separators only between blocks. Updated the [PowerShell parser tests](/app/test/units/plugins/shell/test_powershell.py).

Verification: **8 focused tests passed**; `git diff --check` passed.