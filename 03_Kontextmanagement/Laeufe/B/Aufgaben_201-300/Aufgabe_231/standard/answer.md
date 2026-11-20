Resolved the Vuls2 schema mismatch handling in [db.go](/app/detector/vuls2/db.go). Connection and metadata errors now include the database path. A mismatched schema forces a download when updates are enabled and returns a clear error when `SkipUpdate` is set.

Added mismatch and connection lifecycle tests. `go test ./detector/vuls2 -count=1` passed using local dependencies.