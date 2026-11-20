# Checkpoint

Implemented canonical OS family identifiers and exact EOL release mapping in `config/os.go`, date-boundary evaluators, scan-result EOL warnings, and per-warning scan-summary rendering. Centralized version parsing in `version.Major`, exposed as `util.Major`, and replaced the duplicated config and OVAL parsing. Added mapping, boundary, warning, summary, and version tests.

Verification:
- `GOPROXY=off GOSUMDB=off go test ./...` passed before the final `util/major_test.go` addition.
- `GOPROXY=off GOSUMDB=off go test ./config ./util ./scan ./report ./oval` passed after all edits.
- `git diff --check` passed.

The Go toolchain printed a C compiler warning from the existing `github.com/mattn/go-sqlite3` dependency; tests passed.
