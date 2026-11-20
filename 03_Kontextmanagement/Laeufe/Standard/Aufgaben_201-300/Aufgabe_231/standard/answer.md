Updated the Vuls2 database logic to check schema versions before deciding whether to skip or download an update. A mismatch now forces a download when updates are enabled and returns a path-aware error when `SkipUpdate` is enabled. The connection also validates metadata before use.

Added tests for both mismatch cases and metadata errors. `go test ./detector/vuls2` passes.