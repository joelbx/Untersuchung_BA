# Checkpoint

Task: ensure oval.major("") returns "" while preserving non-empty behavior and API.
Changes: added an exact-empty-input return in oval/util.go and an empty-input case in Test_major.
Red verification: `GOPROXY=off GOSUMDB=off go test ./oval -run '^Test_major$' -count=1` failed before the fix with `panic: runtime error: slice bounds out of range [:-1]` at oval/util.go:288.
Green verification: `GOPROXY=off GOSUMDB=off go test ./oval -count=1` exited 0 (`ok github.com/future-architect/vuls/oval 0.007s`). The compiler printed a warning from sqlite3-binding.c; tests still passed.
Note: `rg` is unavailable (`/bin/bash: rg: command not found`); used local fallback tools.
Final review: `git diff --check` exited 0. `gofmt -l oval/util.go oval/util_test.go` lists both files solely because this Go version would add `//go:build !scanner` above the repository's existing `// +build !scanner` headers; `gofmt -d` showed no formatting changes to the edited lines.
