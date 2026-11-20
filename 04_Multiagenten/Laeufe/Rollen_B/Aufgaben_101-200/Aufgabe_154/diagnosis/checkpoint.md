Role: fault localization; source and tests untouched.
Findings:
- lib/ansible/plugins/connection/ssh.py:1332-1333 only parses when stderr starts with b'#< CLIXML'; mixed stderr bypasses parsing, and whole-stream parsing would discard surrounding bytes.
- lib/ansible/plugins/shell/powershell.py:59-91 searches for <Objs ...></Objs>, returns only Error stream text; incomplete blocks return b'', malformed XML raises ParseError.
- powershell.py:31 regex uses an 8-byte character class rather than four explicit UTF-16-BE zero/hex pairs. Reproduced ValueError for literal `_x\u6100\u6200\u6300\u6400_`.
- Existing parser tests cover complete CLIXML and escapes, but no mixed stderr, malformed/incomplete blocks, or cp437 fallback. Existing SSH exec test does not cover Windows bytes.
Likely fix locations: add byte-preserving block replacement helper near _parse_clixml in powershell.py; use from Windows branch of ssh.Connection.exec_command; tighten regex to four zero/hex pairs. Preserve surrounding bytes and failed blocks, parse complete blocks, decode UTF-8 with cp437 fallback only for CLIXML content.
Uncertainty: issue names b'\r\nCLIXML\r\n' as header, while parser docstring/tests use b'#< CLIXML\r\n'; implementation should reconcile against actual emitted format.
