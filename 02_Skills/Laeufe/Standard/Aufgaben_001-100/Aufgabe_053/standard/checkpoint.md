# Checkpoint

Task: make `oval.major("")` return `""` while preserving non-empty behavior and API.

Change: added an early return for zero-length input in `oval/util.go` and an empty-input case in `oval/util_test.go`. Existing parsing path for non-empty input is unchanged.

Verification:
- `GOPROXY=off GOSUMDB=off go test ./oval -run '^Test_major$' -count=1` — passed.
- `GOPROXY=off GOSUMDB=off go test ./oval -count=1` — passed.
- `git diff --check` — passed.

The Go builds emitted an existing warning from the cached `github.com/mattn/go-sqlite3` C dependency; the tests passed. `rg` is unavailable (`/bin/bash: rg: command not found`), so inspection used `grep` and `find`.
