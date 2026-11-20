Implemented vulnerability diff reporting with `+` for newly detected CVEs and `-` for resolved CVEs. Diff reports can include either type or both; both are included by default. Package details come from the scan where that CVE appeared.

Added `DiffStatus`, `CveIDDiffFormat`, and `CountDiff` in [vulninfos.go](/app/models/vulninfos.go:18). Wired filtering and status assignment into [util.go](/app/report/util.go:523), and added `-diff-plus` and `-diff-minus` options to the report and TUI commands.

Verification passed: `GOPROXY=off go test ./models ./report ./subcmds`.