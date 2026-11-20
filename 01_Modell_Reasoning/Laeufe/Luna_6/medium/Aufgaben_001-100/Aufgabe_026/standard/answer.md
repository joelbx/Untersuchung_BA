Implemented multi-source CVE handling for Ubuntu and other supported families. Added `GetCveContentTypes`, updated vulnerability data ordering and change detection to include family sources, expanded CVSS v3 source coverage, and mapped `NEGLIGIBLE` to LOW.

Validation passed: `go test ./models ./detector ./reporter` and `git diff --check`.