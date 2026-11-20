Updated Trivy parsing to store the OS version in `Release`, use `ArtifactName` for `ServerName` with `:latest` for untagged container images, and leave `Optional` nil. Package CVE detection now uses `ScannedBy` to recognize Trivy results and skips OVAL/GOST for incomplete or unsupported scans.

Updated regression tests. `go test ./contrib/trivy/parser/v2 ./detector` and `git diff --check` passed.