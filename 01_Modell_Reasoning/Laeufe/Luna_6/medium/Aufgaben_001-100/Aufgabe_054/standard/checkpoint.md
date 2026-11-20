# Checkpoint

Implemented `GetInstance[T]` in `utils/singleton/singleton.go`. It caches entries by the full reflected type, preserving separate instances for `T` and `*T`, and uses `sync.Once` so concurrent callers initialize each type once.

Added coverage for concrete return types, repeat retrieval, distinct value and pointer caches, and 20,000 concurrent calls. Verification: `go test ./utils/singleton` passes.
