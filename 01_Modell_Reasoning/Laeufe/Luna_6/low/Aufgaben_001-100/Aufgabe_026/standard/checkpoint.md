# Checkpoint

Implemented multi-source CVE content support for OS families.

- Added `GetCveContentTypes` with multi-source mappings for RedHat-derived, Debian/Raspbian, and Ubuntu families.
- Updated source URL, CPE, reference, CWE, title/summary, CVSS v3, and CVE update detection ordering to include the mapped family sources.
- Kept `NewCveContentType` as the single-source compatibility API.
- Mapped `NEGLIGIBLE` to the LOW severity range and rough score.
- Verification: `go test ./models ./detector ./reporter` passed; `git diff --check` passed.
