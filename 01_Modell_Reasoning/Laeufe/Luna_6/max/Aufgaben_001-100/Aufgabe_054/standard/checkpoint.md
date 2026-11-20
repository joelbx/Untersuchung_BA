# Checkpoint

Implemented `singleton.GetInstance[T]` in `utils/singleton/singleton.go`. The cache uses exact `reflect.Type` keys and per-type `sync.Once` initialization, keeping `T` and `*T` independent. A typed wrapper preserves nil interface results.

Added package coverage for value and pointer separation, reuse, nil interface results, and 20,000 concurrent calls.

Validation passed:
- `go test ./utils/singleton`
- `go test -race ./utils/singleton`
- `go test ./server/events ./core/scrobbler ./scheduler ./db`

The sqlite3 C compiler emitted a warning that `sqlite3SelectNew` may return a local address; the `db` tests passed.
