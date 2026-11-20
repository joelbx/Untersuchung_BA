# Checkpoint

Task: decode embedded Windows stderr CLIXML while preserving surrounding and invalid data.

Root cause: SSH only called `_parse_clixml` when stderr began with `#< CLIXML`, and the parser consumes XML without preserving surrounding bytes. The UTF-16-BE escape regex allowed arbitrary arrangements of zero bytes and hex characters, so Unicode lookalikes could be treated as escapes and raise `ValueError`.

Reproduction: New focused tests failed before the patch: eight helper cases raised `AttributeError` because the helper was absent; the Unicode lookalike case raised `ValueError` in `base64.b16decode`. Existing SSH condition also showed why prefixed CLIXML was skipped.

Fix: Added `_replace_stderr_clixml` to locate complete headers and XML blocks, decode UTF-8 with cp437 fallback, call `_parse_clixml`, and retain surrounding bytes. Invalid or incomplete blocks remain unchanged. SSH invokes it for Windows stderr. Tightened UTF-16-BE escape matching.

Verification: `python -m pytest -q --override-ini reruns=0 test/units/plugins/connection/test_ssh.py test/units/plugins/shell/test_powershell.py` passed (48 tests). `git diff --check` passed. Initial `rg` search was unavailable (`/bin/bash: rg: command not found`); local grep/find supplied the same repository evidence.
