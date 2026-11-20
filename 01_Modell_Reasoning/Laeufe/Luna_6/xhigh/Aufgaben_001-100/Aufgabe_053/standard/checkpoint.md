# Checkpoint

Task complete: `oval.major("")` returns `""` through an early zero-length guard. Parsing for all non-empty inputs continues through the pre-existing logic.

Regression coverage: `Test_major` includes empty input.

Verification: `GOPROXY=off go test ./oval` passed. `git diff --check` passed. The Go build emitted an existing C compiler warning from `github.com/mattn/go-sqlite3`.
