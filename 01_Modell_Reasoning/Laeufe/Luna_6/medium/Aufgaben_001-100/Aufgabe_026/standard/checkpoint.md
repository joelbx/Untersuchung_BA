# Checkpoint

Implemented multi-source CVE content family mapping and integrated it into source URL retrieval, CPE/reference/CWE ordering, title/summary prioritization, CVSS v3 scores, and detector/reporter change detection. Added NEGLIGIBLE handling as LOW for score ranges and rough score estimates. Kept the legacy single-type mapper intact.

Validation passed: `go test ./models ./detector ./reporter`; `git diff --check`.
