# Checkpoint

Task: Implement generic `singleton.GetInstance` with per-type caching and concurrency safety.

Completed: Added generic `GetInstance[T any](constructor func() T) T`, keyed by exact `reflect.Type` and synchronized per type with `sync.Once`. Existing `Get` remains compatible. Added tests for typed value reuse, `T` versus `*T` independence, and 20,000 concurrent pointer requests.

TDD: The new tests initially failed to compile with `undefined: singleton.GetInstance`, the expected missing API. After implementation, `GOTOOLCHAIN=local GOPROXY=off go test ./utils/singleton -count=1` passed. `GOTOOLCHAIN=local GOPROXY=off go test -race ./utils/singleton -run '^TestGetInstance' -count=1` passed. `GOTOOLCHAIN=local GOPROXY=off go test ./...` passed; compiler emitted existing C/C++ deprecation/return-address warnings in taglib and sqlite3.

Environment: `rg` unavailable (`/bin/bash: line 1: rg: command not found`); used `find` and `grep` for discovery. No downloads requested.

Final verification: After adding a readiness barrier so all 20,000 goroutines wait before release, reran `GOTOOLCHAIN=local GOPROXY=off go test -race ./utils/singleton -run '^TestGetInstance' -count=1` and `GOTOOLCHAIN=local GOPROXY=off go test ./...`; both passed. `git diff --check` passed. Full suite still prints the existing sqlite3 and taglib compiler warnings.
