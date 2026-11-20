Implemented status-aware diffs. CVEs found only in the current scan receive `+`; CVEs found only in the previous scan receive `-`. The diff function accepts plus/minus selectors, and resolved CVEs carry package data from the previous scan. Text, CSV, and TUI reports display the status prefix.

Added `DiffStatus`, `CveIDDiffFormat`, and `CountDiff`, with tests for status selection and package sourcing.

Verification: `go test ./models ./report` passed; `git diff --check` passed.