# Checkpoint

Issue: `oval.major("")` must return an empty string while preserving parsing semantics for non-empty inputs.

Completed: added an early return for zero-length input in `oval/util.go` and added an empty-input regression case to `oval/util_test.go`.

Verification: `go test ./oval` passed. The compiler emitted a pre-existing warning from `github.com/mattn/go-sqlite3` C code.
