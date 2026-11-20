# Checkpoint

Task: resolve missing OS end-of-life lookup and scan-summary warnings, centralize OS family identifiers and major-version parsing.

Initial state: identified distro constants and `Distro` in `config/config.go`, per-target warning storage in `models.ScanResult`, summary formatting in `report/util.go`, and duplicate major parsers in `gost` and `oval`.

Implemented centralized family identifiers and canonical EOL dates in `config/os.go`, including deterministic date lookup, strict boundary evaluators, Amazon release matching, and warning generation. Added shared major parsing used by `util.Major`, distro version parsing, `gost`, and `oval`. Scan results (including HTTP scans) now receive EOL warnings, and summaries render each warning in order with `Warning: `.

Verification: `GOPROXY=off go test ./config ./util ./scan ./models ./report ./gost ./oval ./internal/version` passed. `git diff --check` passed. Go emitted an existing C warning from `go-sqlite3`; it did not fail the tests.
