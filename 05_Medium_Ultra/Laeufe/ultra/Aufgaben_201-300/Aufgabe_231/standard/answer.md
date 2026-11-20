Updated [db.go](/app/detector/vuls2/db.go) to validate database metadata and schema version. A mismatch now forces a download, or returns a path-bearing error when `SkipUpdate` is enabled. Connection and metadata failures also report the database path.

Added mismatch and connection lifecycle coverage in [db_test.go](/app/detector/vuls2/db_test.go). The Vuls2 package tests pass offline: `GOPROXY=off GOSUMDB=off go test ./detector/vuls2 -count=1`.

Two subagents reviewed the behavior and test coverage; I integrated and verified the patch.