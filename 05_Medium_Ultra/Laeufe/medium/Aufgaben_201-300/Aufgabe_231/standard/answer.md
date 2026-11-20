Updated [db.go](/app/detector/vuls2/db.go) so schema mismatches force a download, or return an error when `SkipUpdate` is enabled. `newDBConnection` now reads and validates metadata and includes the database path in connection and metadata errors. Added mismatch cases in [db_test.go](/app/detector/vuls2/db_test.go).

`go test ./detector/vuls2` and `git diff --check` passed.