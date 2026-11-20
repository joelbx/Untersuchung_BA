Added `parse_duration` and updated `:later` to accept values such as `5s`, `2m30s`, and `1.5h`. Bare numbers still mean milliseconds. Invalid durations raise an error, and the command help and unit tests are updated.

The focused tests passed (26). All 190 tests in the two relevant unit files reported passing, though that test process exited with an X11 connection error during shutdown.