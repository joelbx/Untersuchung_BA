Implemented multi-source CVE content handling for Ubuntu, Debian, and Red Hat family hosts. Family sources now contribute to update detection, source URLs, CPEs, references, CWE IDs, titles, summaries, and CVSS v3 results. `NEGLIGIBLE` maps to `LOW` for severity ranges and rough scores.

Added regression tests for family mappings, severity mapping, and Ubuntu API update detection.

Validation passed: `go test ./models ./reporter` and `git diff --check`.