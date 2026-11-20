Implemented schema-version validation in [db.go](/app/detector/vuls2/db.go:31). Mismatches now force a download when updates are allowed and return a path-bearing error when `SkipUpdate` is enabled. `newDBConnection` also reports path-bearing errors for connection and metadata failures and rejects nil metadata or an incompatible schema.

Added mismatch cases to the existing tests in [db_test.go](/app/detector/vuls2/db_test.go:88).

Verification: `go test ./detector/vuls2` and `git diff --check` passed.