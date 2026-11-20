Implemented multi-source CVE family handling for URLs, CPEs, references, CWE IDs, titles, summaries, CVSS v3 scores, and CVE change detection. Added `GetCveContentTypes`, preserved single-type lookup compatibility, and mapped NEGLIGIBLE like LOW for severity ranges and rough scores.

Verification passed: `go test ./models ./detector ./reporter ./tui`, `go test ./models ./gost` (with downloads disabled), and `git diff --check`.

Key changes: [cvecontents.go](/app/models/cvecontents.go), [vulninfos.go](/app/models/vulninfos.go), [detector/util.go](/app/detector/util.go), and [reporter/util.go](/app/reporter/util.go).