# Checkpoint

Issue: Ubuntu vulnerability output omitted details because family-specific CVE sources were treated as a single type.

Implementation:
- Added `GetCveContentTypes` with multi-source mappings for RedHat-based, Debian/Raspbian, and Ubuntu families, while retaining single-source mappings for recognized families and nil for unknown names.
- Updated URL, CPE, reference, CWE, title, summary, CVSS v3, and CVE change-detection source handling to include paired sources.
- Added Oracle and Microsoft to the shared content type list and included Oracle, Fedora, and Microsoft CVSS v3 values.
- Mapped `NEGLIGIBLE` to the LOW range and rough score; mapped Raspbian to Debian for the single-source helper.

Validation: `go test ./models ./detector ./reporter ./gost` passed; `git diff --check` passed.
