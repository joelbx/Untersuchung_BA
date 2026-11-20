# Checkpoint

Task completed: added `GetInstance[T any](constructor func() T) T` to `utils/singleton/singleton.go` and regression tests in `utils/singleton/get_instance_test.go`.

Root cause: the existing `Get` API requires a placeholder and returns `interface{}`. Its string key removes a leading `*`, so it cannot keep value and pointer types independent. The new API uses exact `reflect.Type` keys and a typed entry with `sync.Once`. A typed entry also handles a nil interface result without a failing assertion.

Reproduction before fix: `GOPROXY=off GOSUMDB=off go test ./utils/singleton -run TestGetInstance -count=1` failed to compile with `undefined: singleton.GetInstance`. The nil interface regression test subsequently reproduced a panic in the first implementation; a typed entry resolved it.

Verification after fix:
- `GOPROXY=off GOSUMDB=off go test ./utils/singleton -count=1` passed.
- `GOPROXY=off GOSUMDB=off go test -race ./utils/singleton -run TestGetInstance -count=1` passed, including 20,000 concurrent callers.
- `GOPROXY=off GOSUMDB=off go test ./scheduler ./db ./server/events ./core/scrobbler` passed. SQLite emitted a compiler warning but no test failed.
- `git diff --check` passed.

The original `Get` API remains available for current callers.
