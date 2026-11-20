Diff reports now mark newly detected CVEs with `+` and resolved CVEs with `-`, omit unchanged CVEs, and use package data from the corresponding scan. Use `-diff-plus=false` or `-diff-minus=false` to show only one type; both are enabled by default.

Added the requested `DiffStatus`, `CveIDDiffFormat`, and `CountDiff` interfaces. Relevant tests passed: `go test ./models ./report ./subcmds`.