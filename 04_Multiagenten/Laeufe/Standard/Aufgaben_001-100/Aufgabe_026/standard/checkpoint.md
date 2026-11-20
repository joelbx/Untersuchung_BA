# Checkpoint

Issue resolved in checked-out files. Added OS-family multi-source CVE mapping and used it for change detection, source URLs, presentation ordering, and field retrieval. Extended CVSS v3 source handling and mapped NEGLIGIBLE severity to LOW. Added regression coverage for mapping, Ubuntu source data, score/summary ordering, and Ubuntu API update detection.

Validation: `go test ./models ./detector ./reporter` passed; `git diff --check` passed.
