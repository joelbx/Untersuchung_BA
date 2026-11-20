Updated `_parse_clixml` to decode CLIXML escape sequences, combine valid surrogate pairs, preserve unpaired surrogates, filter by stream, and separate multiple `<Objs>` blocks with CRLF. Added focused coverage for these cases and updated the newline expectation.

Validation: `python -m pytest -q test/units/plugins/shell/test_powershell.py` — **9 passed**. `git diff --check` passed.