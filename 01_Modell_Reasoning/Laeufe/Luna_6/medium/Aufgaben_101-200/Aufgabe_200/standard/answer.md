Implemented `parse_duration` in [utils.py](/app/qutebrowser/utils/utils.py) and updated `:later` in [utilcmds.py](/app/qutebrowser/misc/utilcmds.py) to accept unit-based durations while preserving digit-only millisecond inputs.

Verification: 224 existing tests passed, and `git diff --check` passed.