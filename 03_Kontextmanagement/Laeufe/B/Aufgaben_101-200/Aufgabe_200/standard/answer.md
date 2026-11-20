Added unit based durations to `:later`. It now accepts values such as `5s`, `2m30s`, and `1.5h`; bare integers still mean milliseconds. Invalid durations raise an error. I also updated the command help and added tests.

Verification: **186 relevant tests passed**, and `git diff --check` passed.