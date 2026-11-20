# Checkpoint

Task completed: implement Trivy OS release extraction and related package CVE detection behavior.

Changes:
- Parser stores `Metadata.OS.Name` in Release, uses Metadata.OS.Family with result type fallback, and sets ArtifactName as ServerName for OS and library scans. Untagged container images receive `:latest`; Optional is nil.
- Trivy scan reuse checks `ScannedBy`. OVAL/GOST run only for supported non-Trivy results with family, release, and packages; FreeBSD, Raspbian, and pseudo results are skipped with logged reasons. Detector errors are logged and returned.
- Updated existing Trivy parser expectations.

Validation passed:
- `go test ./contrib/trivy/parser/v2 ./detector`
- `git diff --check`
