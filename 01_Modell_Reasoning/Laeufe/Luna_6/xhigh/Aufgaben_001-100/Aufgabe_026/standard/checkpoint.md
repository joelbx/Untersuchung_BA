# Checkpoint

Implemented multi-content CVE family mappings in `models/cvecontents.go` and applied them to URL retrieval, CPE/reference/CWE source ordering, title and summary prioritization, CVSS v3 score retrieval, and change detection in both `detector` and `reporter`. Kept single-type lookup and existing no-argument CVSS methods compatible. NEGLIGIBLE now maps like LOW for severity ranges and rough scores.

Verification passed with downloads disabled:
- `go test ./models ./detector ./reporter ./tui`
- `go test ./models ./gost`
- `git diff --check`
