Diff reports now mark newly detected CVEs with `+` and resolved CVEs with `-`. The new `-diff-plus` and `-diff-minus` flags let users include either type or both. Added `DiffStatus`, `CveIDDiffFormat`, and `CountDiff`; package details come from the scan that contains each CVE.

Verified with `go test ./models ./report ./subcmds` and `git diff --check`.