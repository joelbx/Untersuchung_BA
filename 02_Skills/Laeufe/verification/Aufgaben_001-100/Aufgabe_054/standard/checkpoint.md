# Checkpoint

- Task: add concurrency-safe generic `singleton.GetInstance[T]` with independent type keys.
- Implemented `GetInstance[T]` with `reflect.Type` keys, `sync.Map`, and a per-type `sync.Once`.
- Added tests for value and pointer independence, reuse, and 20,000 simultaneous calls.
- `GOPROXY=off go test -race ./utils/singleton` passed.
- `GOPROXY=off go test ./server/events ./core/scrobbler ./scheduler ./db` passed (sqlite3 emitted a C compiler warning).
- `git diff --check` passed.
