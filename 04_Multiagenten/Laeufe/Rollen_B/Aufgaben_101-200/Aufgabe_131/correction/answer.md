Fixed the polling cadence: attempts now start on fixed 5000 ms ticks, skip ticks while a call is pending, and stop after at most 5 calls. Added tests for delayed calls and overlapping-call prevention.

The reviewer’s exact test command passed (7 tests), the type check passed, and `git diff --check` found no whitespace issues.