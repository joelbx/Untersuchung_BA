`major("")` now returns `""`; I added an empty-input regression case while preserving existing parsing for non-empty versions. I also added the three requested report API functions, using the existing detection logic.

Verification: `GOPROXY=off go test ./oval ./report` passed, and `git diff --check` passed. The test build emitted a SQLite C compiler warning.