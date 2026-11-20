# Checkpoint

Implemented canonical EOL lookup in `config/os.go`, per-target scan EOL warnings, summary warning rendering, and shared major-version parsing. OS family identifiers now live with the EOL map.

TDD: Added tests first. Initial focused command `GOPROXY=off go test ./config ./util ./scan ./report -run 'Test(GetEOL|EOLEndDatesAreExclusive|Major$|EOLWarnings|ScanSummaryRendersWarningsInOrder)' -count=1` failed for missing GetEOL, Major, eolWarnings, and summary warning formatting. After implementation the focused command passed.

Verification: `GOPROXY=off go test ./...` passed after the final refactor. `git diff --check` passed. The test run emitted an existing C compiler warning from github.com/mattn/go-sqlite3 (`sqlite3-binding.c:128049`, possible address of local variable); no tests failed.
