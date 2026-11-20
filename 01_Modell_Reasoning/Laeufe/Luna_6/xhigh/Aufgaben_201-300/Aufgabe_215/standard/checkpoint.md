# Checkpoint

Task: Resolve HTTPS support in `/app`.

Completed:
- Added `Scheme` (`HTTP`, `HTTPS`) and string/JSON representation.
- Made `configure(path)` use an isolated Viper instance, honor `FLIPT_*` overrides, map YAML values over `defaultConfig()`, normalize scalar/list CORS origins, and call `validate()` without wrapping load or validation errors.
- Added HTTP/HTTPS ports, TLS paths, HTTPS prerequisite validation, and TLS for REST/UI and gRPC serving.
- Updated configuration examples and documentation.
- Ran `go test ./cmd/flipt` and `go test ./...`; both passed. `git diff --check` passed.

No credential contents, private process files, benchmark/evaluator artifacts, or external research were accessed. Git history and index baseline were not changed.
