# Checkpoint

Completed: added `GetInstance[T]` in `utils/singleton/singleton.go`. Its cache uses exact `reflect.Type` keys, separating `T` and `*T`; per-entry `sync.Once` guarantees one constructor call and safely returns the same typed result, including nil interface values.

Added acceptance coverage to the existing `utils/singleton/singleton_test.go`: independent value/pointer caches and 20,000 concurrent calls with a single constructor execution and shared instance.

Verification passed: `go test ./utils/singleton`, `go test -race ./utils/singleton`, and `git diff --check`.
