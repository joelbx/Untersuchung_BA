VERDICT: FIX
CODE_DEFECT: db/backup.go:124-131 accepts any valid SQLite file after PRAGMA integrity_check and copies it over the live database. A healthy unrelated SQLite database passes this check; restore should verify recognizable Navidrome backup/schema metadata before calling copySQLite, and reject the live database itself as a source.
TESTS: GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test ./db ./cmd ./conf — PASS (db 1.067s; cmd/conf have no test files). GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test ./scheduler — PASS (no test files).
TEST_ENVIRONMENT_PROBLEM: none.
