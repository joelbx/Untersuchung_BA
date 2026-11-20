Updated [db.go](/app/detector/vuls2/db.go) to validate connection and metadata errors with the database path, reject schema mismatches, and force a download when updates are allowed. Added mismatch cases to [db_test.go](/app/detector/vuls2/db_test.go).

`go test ./detector/vuls2` and `git diff --check` passed.