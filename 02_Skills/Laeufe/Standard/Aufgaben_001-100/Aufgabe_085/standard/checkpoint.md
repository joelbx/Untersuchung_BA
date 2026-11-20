# Checkpoint

Implemented plus/minus diff filtering, status fields and formatting, CLI flags, and package selection from the appropriate scan. `rg` is unavailable, so searches used local `grep`/`find`.

Verification: `go test ./models ./report ./subcmds && git diff --check` passed. The Go compiler emitted a pre-existing warning from `github.com/mattn/go-sqlite3` but tests passed.
