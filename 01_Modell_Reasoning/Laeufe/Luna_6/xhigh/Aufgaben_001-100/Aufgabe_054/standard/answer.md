Implemented `GetInstance[T]` in [singleton.go](/app/utils/singleton/singleton.go:48), with an exact-type cache and `sync.Once` so each type is constructed once under concurrency. Value and pointer types have independent instances.

Added coverage in [singleton_test.go](/app/utils/singleton/singleton_test.go:85), including 20,000 concurrent calls.

Verified: `go test ./utils/singleton`, `go test -race ./utils/singleton`, and `git diff --check` all passed.