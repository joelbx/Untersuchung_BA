Diff reports now mark newly detected CVEs with `+` and resolved CVEs with `-`, exclude unchanged CVEs, and use package data from the matching scan. The new `DiffStatus`, `CveIDDiffFormat`, and `CountDiff` interfaces are in [models/vulninfos.go](/app/models/vulninfos.go:16).

`-diff` shows both types by default. Use `-diff -diff-minus=false` for only new CVEs, or `-diff -diff-plus=false` for only resolved CVEs.

Verified with `go test ./models ./report ./subcmds` and `git diff --check`.