Diff reports now mark newly detected CVEs with `+` and resolved CVEs with `-`. The `-diff-plus` and `-diff-minus` flags select either type or both; unchanged CVEs are excluded. Package details come from the scan in which each CVE appeared.

Added `DiffStatus`, `CveIDDiffFormat`, and `CountDiff`. Verification passed: `go test ./report ./models ./subcmds` and `git diff --check`.