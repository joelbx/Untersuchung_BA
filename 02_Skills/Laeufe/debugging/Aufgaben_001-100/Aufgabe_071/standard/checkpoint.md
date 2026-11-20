# CLIXML parser checkpoint

Task: decode PowerShell CLIXML stream text, including UTF-16 escapes and multiple Objs blocks.

Status: investigating parser and existing tests. `rg` is unavailable (`/bin/bash: rg: command not found`); using local grep/find fallback.

Investigation: `_parse_clixml` in `lib/ansible/plugins/shell/powershell.py` currently removes only `_x000D__x000A_`, joins every matching S element with CRLF, and dereferences `e.text` without handling None. It already loops over Objs blocks. Existing tests assert the old removal and per-S separators. Call sites consume bytes. Root cause is decoding/assembly in this parser, not the connection layers. Hypothesis: decoding each S as UTF-16 escape tokens and joining only completed blocks fixes all reported output corruption. Preserve unmatched escape text and encode unpaired surrogates with surrogatepass.

Verification: baseline `python -m pytest -q test/units/plugins/shell/test_powershell.py` passed 6/6. New reproduction tests then failed on escaped Unicode, CR/LF, literal underscore handling, unpaired surrogate, empty S text, and per-S separators. A follow-up regression test failed when two blocks had no output (`b'\r\n'` instead of `b''`); fixed by skipping blocks without matching S and returning empty bytes when all matching text is empty.

Final checks: `python -m pytest -q test/units/plugins/shell -o reruns=0` passed 20/20. `git diff --check` passed. No external tooling used.
