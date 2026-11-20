# Checkpoint

Task: ensure oval.major("") returns "" while preserving non-empty behavior and API.
Workflow: assigned test-driven-development skill; regression test before production edit.
Initial discovery: rg unavailable (/bin/bash: rg: command not found); using find/grep.

RED: `GOPROXY=off GOSUMDB=off go test ./oval -run '^TestMajorEmptyInputReturnsEmptyString$' -count=1` failed as expected: panic `slice bounds out of range [:-1]` at oval/util.go:288. Build emitted existing go-sqlite3 C warning.
GREEN: `GOPROXY=off GOSUMDB=off go test ./oval -run '^TestMajorEmptyInputReturnsEmptyString$' -count=1` passed.
SUITE: `GOPROXY=off GOSUMDB=off go test ./...` passed all packages. Both runs emitted the existing go-sqlite3 C compiler `-Wreturn-local-addr` warning.
