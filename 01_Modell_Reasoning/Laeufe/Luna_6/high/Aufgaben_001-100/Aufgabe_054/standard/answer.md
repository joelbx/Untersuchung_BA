Implemented `GetInstance[T]` with a type-specific cache and `sync.Once`, keeping value and pointer instances separate. Added coverage for 20,000 concurrent calls and separate value/pointer caches.

Verified with `go test ./utils/singleton`, `go test -race ./utils/singleton`, and `git diff --check`.