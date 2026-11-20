Added `parse_duration` and updated `:later` to accept durations such as `5s`, `2m30s`, and `1.5h`. Bare integers still mean milliseconds; invalid durations raise an error.

The focused parser and command tests pass (26 tests total), and `git diff --check` passes. A broader run reported 189 passing tests, then exited with an X server shutdown error.