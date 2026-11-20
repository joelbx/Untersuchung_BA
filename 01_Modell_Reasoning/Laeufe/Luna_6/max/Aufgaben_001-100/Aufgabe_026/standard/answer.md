Implemented multi-source CVE handling. Added `GetCveContentTypes` in [cvecontents.go](/app/models/cvecontents.go:357) and used it for source URLs, CPEs, references, CWE IDs, titles, summaries, and CVE change detection. Ubuntu API severity scores are included, and `NEGLIGIBLE` maps to LOW.

Updated the checkpoint at `.codex-role-output/checkpoint.md`.

Validation passed: `go test ./models ./detector ./reporter ./gost` and `git diff --check`.