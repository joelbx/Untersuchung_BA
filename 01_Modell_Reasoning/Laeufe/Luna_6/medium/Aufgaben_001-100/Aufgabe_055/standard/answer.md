Implemented the Trivy metadata and detection changes. The parser now stores the OS version in `Release`, uses `ArtifactName` for `ServerName` (adding `:latest` to untagged container images), and clears `Optional`. Package detection is gated by `isPkgCvesDetactable`, and Trivy results are identified through `ScannedBy`.

Updated the parser fixtures to match the new metadata behavior.

Verification passed: `go test ./contrib/trivy/parser/v2 ./detector` and `git diff --check`.