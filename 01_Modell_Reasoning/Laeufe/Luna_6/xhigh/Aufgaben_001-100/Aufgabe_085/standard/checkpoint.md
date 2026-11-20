# Checkpoint

Completed vulnerability diff reporting changes:

- Added `DiffStatus` (`+`/`-`), `VulnInfo.CveIDDiffFormat`, and `VulnInfos.CountDiff`.
- Changed diff comparison to select added and/or resolved CVEs, label each result, and source associated package records from the current or previous scan respectively.
- Added `-diff-plus` and `-diff-minus` command options, both enabled by default, and applied markers/counts in report output.
- Updated the existing report diff test for the new comparison signature and status field.

Validation passed: `go test ./models ./report`, `go test ./subcmds`, `go test ./config`, and `git diff --check`.
