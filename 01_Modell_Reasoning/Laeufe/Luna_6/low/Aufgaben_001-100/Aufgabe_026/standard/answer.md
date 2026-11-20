Implemented multi-source CVE content handling across family mappings, change detection, source URLs, CPEs, references, CWE IDs, titles, summaries, and CVSS v3 retrieval. Added `NEGLIGIBLE` handling for LOW severity ranges and rough scores.

`NewCveContentType` remains available for single-type mappings. The checkpoint is recorded in `.codex-role-output/checkpoint.md`.

Verification passed: `go test ./models ./detector ./reporter` and `git diff --check`.