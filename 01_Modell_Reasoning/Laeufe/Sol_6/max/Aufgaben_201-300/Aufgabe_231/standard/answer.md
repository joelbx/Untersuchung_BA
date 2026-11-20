Updated [db.go](/app/detector/vuls2/db.go:31) to validate database metadata and schema version, with the database path in connection and metadata errors. A mismatch now forces a download, or returns an explicit error when `SkipUpdate` is enabled.

Added regression cases in [db_test.go](/app/detector/vuls2/db_test.go:105). `GOPROXY=off GOSUMDB=off go test ./detector/vuls2` passed.