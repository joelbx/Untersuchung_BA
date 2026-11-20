# Checkpoint

- Implemented `GetCveContentTypes` for Red Hat family, Debian family, and Ubuntu, with nil for unsupported families.
- Updated CVE change detection, source URL selection, CPE/reference/CWE ordering, title/summary priorities, and CVSS v3 source collection to include every mapped family source.
- Added `NEGLIGIBLE` severity handling as `LOW` and regression tests for family mapping, severity conversion, and Ubuntu API update detection.
- Validation: `go test ./models ./reporter` passed; `git diff --check` passed.
