Updated `_parse_clixml` to decode UTF-16 escape sequences, combine valid surrogate pairs, preserve control characters and unpaired surrogates, and return only the requested stream. It now handles empty `<S>` elements and joins results from separate `<Objs>` blocks with `\r\n`.

Updated the existing tests. All 17 PowerShell shell tests pass, and `git diff --check` is clean.