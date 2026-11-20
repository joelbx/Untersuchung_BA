Added `parse_duration` and updated `:later` to accept durations such as `5s`, `2m30s`, and `1.5h`. Bare numbers still mean milliseconds. Invalid durations raise `ValueError`, and the command help and regression tests are updated.

Verification: 188 relevant tests passed; `git diff --check` passed.