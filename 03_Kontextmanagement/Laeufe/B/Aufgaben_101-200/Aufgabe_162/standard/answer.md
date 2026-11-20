Implemented optional encoding validation in `FormatString` during `to_py` and set `content.headers.user_agent` to require ASCII. Configurations without an encoding constraint retain their existing behavior.

Validation passed: 1,136 tests passed, 10 were expected failures, and `git diff --check` found no issues.