Implemented Trivy OS version parsing and metadata handling. Scan results now use `ArtifactName` for `ServerName`, add `:latest` to untagged container images, store `Metadata.OS.Name` in `Release`, and leave `Optional` nil.

Package CVE detection now skips OVAL and GOST for the specified unsupported results, while Trivy CVE reuse identifies results through `ScannedBy`. Updated the parser expectations and added edge case tests.

Verification passed: `go test ./contrib/trivy/parser/v2 ./detector` and `git diff --check`.