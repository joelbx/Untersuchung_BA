Updated [db.go](/app/detector/vuls2/db.go) to report the database path on connection and metadata errors, validate metadata and schema versions, and handle schema mismatches before applying `SkipUpdate`.

`go test ./detector/vuls2` did not finish during the run, so I stopped it; the test result is unverified.