# Checkpoint

Resolved: Added `GetCveContentTypes` for OS-family CVE sources and retained `NewCveContentType`. Updated source URLs, field ordering, title and summary ordering, CVSS v3 scores, and both detector and reporter change detection to include family sources. Mapped `NEGLIGIBLE` to the low severity range and rough score.

Verification: `GOPROXY=off GOTOOLCHAIN=local go test ./models ./detector ./reporter` passed. `git diff --check` passed. Regression tests cover Ubuntu API details and changes, source ordering, mappings, and severity.
