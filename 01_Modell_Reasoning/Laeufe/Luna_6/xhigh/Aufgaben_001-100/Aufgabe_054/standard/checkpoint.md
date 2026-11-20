# Checkpoint

Implemented `singleton.GetInstance[T]` in `utils/singleton/singleton.go`. The generic API caches by exact `reflect.Type`, creates each entry with `sync.Once`, and returns the stored value through a typed box. This keeps `T` and `*T` independent while leaving the legacy `Get` behavior intact.

Added tests in `utils/singleton/singleton_test.go` for repeated value and pointer retrieval, independent type caches, and 20,000 concurrent calls with exactly one constructor invocation.

Verification passed:
- `go test ./utils/singleton`
- `go test -race ./utils/singleton`
- `git diff --check`
