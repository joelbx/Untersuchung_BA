# Checkpoint

Issue: Ensure `oval.major("")` returns `""` without changing non-empty parsing behavior.

Implemented an early return for the zero-length input in `oval/util.go` and added an empty-input case to `Test_major` in `oval/util_test.go`.

Verification: `go test ./oval` passed, and `go test ./oval -run '^Test_major$' -count=1` passed. Both builds emitted an existing warning from `github.com/mattn/go-sqlite3` (`sqlite3-binding.c` may return the address of a local variable).
