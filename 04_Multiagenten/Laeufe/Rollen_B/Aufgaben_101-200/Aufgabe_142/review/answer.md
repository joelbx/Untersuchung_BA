VERDICT: FIX

**Code defect:** [splitTemplate](/app/lib/utils/parse/parse.go:75) rejects ordinary single braces in plain literals and static template text. For example, `NewExpression("a{b}")` and `NewMatcher("a{b}")` now return malformed-template errors, although neither contains a `{{` or `}}` delimiter. Allow single braces and reject malformed double delimiters.

**Tests run:** `GOPROXY=off go test ./lib/utils/parse` and `GOPROXY=off go test ./lib/services` passed.

**TEST_ENVIRONMENT_PROBLEM:** `go test ./lib/utils/parse ./lib/services ./lib/srv` exited 1: `lib/srv` could not build because `linux/hidraw.h` is missing and sqlite3 lacks `pread64`/`off64_t`. `GOPROXY=off CGO_ENABLED=0 go test ./lib/srv` also exited 1 on missing platform symbols. The `lib/srv` tests therefore did not execute; its native build dependencies need to be available before that package can be verified.