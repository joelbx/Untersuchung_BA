# Singleton generic retrieval

- Goal: add `GetInstance[T](constructor func() T) T` with one construction per type and safe concurrent access.
- Repository status at start: clean.
- Implemented a `sync.Map` keyed by the exact reflected type, with a typed entry guarded by `sync.Once`.
- Migrated the four production callers from `Get` to `GetInstance`.
- Added tests for value and pointer separation, a nil interface result, and 20,000 concurrent first calls.
- Verified: `go test ./utils/singleton`, `go test -race ./utils/singleton`, and `go test ./server/events ./core/scrobbler ./scheduler ./db` with `GOPROXY=off GOSUMDB=off`; all passed. `git diff --check` passed.
