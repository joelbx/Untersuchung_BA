# Checkpoint

Task: ensure `oval.major("")` returns `""` while preserving non-empty behavior and API compatibility.

Status: investigating root cause and existing tests. Working tree was clean at start. `rg` is unavailable (`/bin/bash: line 1: rg: command not found`), so repository searches use local `find` and `grep`.

Root cause: `major` splits the input, then slices at `strings.Index(ver, ".")`. Empty input gives index `-1`, so `ver[0:-1]` panics. Existing `Test_major` covered only dotted versions. The new empty-input case reproduces the panic with `GOPROXY=off GOSUMDB=off go test ./oval -run '^Test_major$' -count=1` (exit 1, slice bounds out of range at `oval/util.go:288`). Hypothesis: an early return for exactly `""` fixes the case without changing the path for non-empty inputs.

Resolved: added that early return and kept the regression case in `Test_major`. Verification passed: `GOPROXY=off GOSUMDB=off go test ./oval -run '^Test_major$' -count=1`, `GOPROXY=off GOSUMDB=off go test ./oval -count=1`, and `git diff --check`. Both Go test commands emitted an existing C compiler warning from `go-sqlite3` but exited 0.
