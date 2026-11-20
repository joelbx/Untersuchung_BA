Added [parse_duration](/app/qutebrowser/utils/utils.py:255) for decimal hour, minute, and second components, while preserving bare integers as milliseconds. Updated [:later](/app/qutebrowser/misc/utilcmds.py:45) to use it and reject invalid durations.

Verification: 194 tests passed across the affected unit test modules; `git diff --check` passed.