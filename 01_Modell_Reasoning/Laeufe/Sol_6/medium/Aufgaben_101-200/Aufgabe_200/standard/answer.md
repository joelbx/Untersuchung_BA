Added unit-based durations to `:later`: values such as `5s`, `2m30s`, and `1.5h` now work, while bare integers remain milliseconds. Invalid durations raise an error. I also updated the command help and added tests.

Verification: **188 relevant tests passed**; `git diff --check` passed.