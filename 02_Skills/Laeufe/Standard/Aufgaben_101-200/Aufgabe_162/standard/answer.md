Added optional encoding validation to `FormatString` during `to_py` and set the user-agent header format to require ASCII. Format strings without an encoding constraint still accept Unicode.

The relevant config tests passed: **1,139 passed, 10 expected failures**. `git diff --check` passed.