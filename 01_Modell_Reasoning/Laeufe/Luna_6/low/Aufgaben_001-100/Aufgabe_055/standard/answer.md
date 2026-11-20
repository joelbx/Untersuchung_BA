Implemented the Trivy metadata and package detection changes.

- Parser stores the OS version from `Metadata.OS.Name`, uses `ArtifactName` for `ServerName`, appends `:latest` to untagged container image names, and clears `Optional`.
- Package CVE detection now runs OVAL and GOST only when `isPkgCvesDetactable` allows it; errors are logged and returned.
- Trivy result reuse now checks `ScannedBy`.
- Updated parser expectations and added metadata coverage.

Verification passed: `go test ./contrib/trivy/parser/v2 ./detector` and `git diff --check`. The checkpoint is at [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md).