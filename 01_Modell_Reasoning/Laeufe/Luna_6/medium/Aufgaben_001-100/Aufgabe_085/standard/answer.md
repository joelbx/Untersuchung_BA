Implemented status-aware vulnerability diffs. New CVEs receive `+`, resolved CVEs receive `-`, and `--diff-plus` / `--diff-minus` let users choose which changes to include. Resolved entries use package data from the previous scan; new entries use the current scan.

Added `DiffStatus`, `CveIDDiffFormat`, and `CountDiff` to the models. Updated the existing diff test for the new status.

Verification: `go test ./report ./models` passed. `git diff --check` passed.