# Checkpoint

Task: Refactor `detectScanDest` to return grouped, deduplicated, deterministically ordered ports by IP; update consumers and verify.

Initial note: `rg` is unavailable (`/bin/bash: rg: command not found`); using local `grep`/`find` instead.

Implementation:
- `detectScanDest` returns `map[string][]string`, expands wildcard addresses, deduplicates ports, and sorts each port slice.
- `execPortsScan` accepts the grouped map and sorts IP keys before dialing, retaining its flat open-endpoint output for status matching.
- Updated destination tests and added wildcard overlap, empty wildcard, and grouped dial coverage.

Verification (offline):
- `GOPROXY=off GOSUMDB=off go test ./scan -run 'Test_detectScanDest|Test_updatePortStatus|Test_findPortScanSuccessOn' -count=1`: exit 0.
- `GOPROXY=off GOSUMDB=off go test ./scan -count=1`: exit 0.
- `git diff --check`: exit 0.
- Both Go test runs printed an existing C compiler warning from `github.com/mattn/go-sqlite3`; tests passed.
