Implemented optional encoding validation for `FormatString` and configured `content.headers.user_agent` to require ASCII. Unconstrained `FormatString` behavior remains unchanged.

The existing config type and config data tests passed: **1134 passed, 10 xfailed**. `git diff --check` was clean.