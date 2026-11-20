# Task checkpoint

Issue: Decode PowerShell CLIXML `_xDDDD_` escapes in the Ansible PowerShell shell plugin.

Implemented: `_parse_clixml` is typed, selects only the requested stream, scans all ordered `<Objs>` blocks, concatenates matching entries inside each block, separates nonempty block results with CRLF, and returns UTF-8 bytes with `surrogatepass`. Escape decoding supports all four-digit hexadecimal UTF-16 units, valid surrogate pairs, lower-case hex, preserved malformed tokens, the specified `_x005F_` behavior, and control characters. Added unit coverage for these cases and updated the legacy trailing-CRLF expectation.

Verification: `python -m pytest -q test/units/plugins/shell/test_powershell.py` passed (10 tests); `git diff --check` passed.
