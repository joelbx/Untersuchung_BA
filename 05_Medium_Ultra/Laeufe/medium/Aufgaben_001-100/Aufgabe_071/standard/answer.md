Updated the PowerShell CLIXML parser to decode UTF-16 escape tokens, including surrogate pairs and control characters. It now selects only the requested stream, handles empty `<S>` elements, and joins results from separate `<Objs>` blocks with CRLF. Added unit coverage and updated the existing newline expectation.

Verification: all 10 PowerShell shell tests pass, and `git diff --check` passes.