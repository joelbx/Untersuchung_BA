Implemented added and resolved vulnerability diffs. New CVEs carry `+`; resolved CVEs carry `-`, and their package data comes from the scan where each CVE appears. Reports display the markers, and summaries count each type.

Use `-diff-plus=false` or `-diff-minus=false` to select one type; both are enabled by default. The comparison and display helpers are in [report/util.go](/app/report/util.go:528) and [models/vulninfos.go](/app/models/vulninfos.go:161).

Validation passed: `go test ./models ./report`, `go test ./subcmds`, `go test ./config`, and `git diff --check`. Checkpoint: [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md).