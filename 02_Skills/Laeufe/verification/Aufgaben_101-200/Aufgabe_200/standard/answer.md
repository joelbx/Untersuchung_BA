Added unit-aware durations to `:later`. It now accepts values such as `5s`, `2m30s`, and `1.5h`; bare digits such as `5000` still mean milliseconds. Invalid durations raise a command error. Updated the command help and tests.

Verification: 188 unit tests passed, and the focused end to end run had 4 passes and 1 expected failure.