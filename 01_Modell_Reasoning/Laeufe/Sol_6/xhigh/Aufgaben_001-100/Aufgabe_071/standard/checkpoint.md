# CLIXML parser issue

Located `_parse_clixml` in `lib/ansible/plugins/shell/powershell.py` and its unit tests in `test/units/plugins/shell/test_powershell.py`.

Implemented typed parsing of all `<Objs>` blocks, matching stream text concatenation within each block, UTF-16 escape decoding with surrogate pairs and unpaired surrogate preservation, and CRLF separation between nonempty block results. Added tests for controls, Unicode, malformed tokens, underscore handling, empty strings, stream selection, and escapes spanning `<S>` entries.

Verification: `python -m pytest -q test/units/plugins/shell/test_powershell.py` (12 passed); `git diff --check` passed.
