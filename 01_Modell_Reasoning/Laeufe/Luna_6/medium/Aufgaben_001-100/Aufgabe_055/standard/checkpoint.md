# Checkpoint

Implemented the Trivy metadata and detector changes:

- Parser records `Metadata.OS.Name` in `Release` (empty when OS metadata is absent), uses `ArtifactName` for every report, appends `:latest` to untagged container images, and clears `Optional`.
- Detector identifies Trivy results through `ScannedBy`, gates OVAL/GOST through `isPkgCvesDetactable`, logs skip reasons, and logs and returns detection errors.
- Updated existing parser fixtures for the new output metadata.

Verification: `go test ./contrib/trivy/parser/v2 ./detector` passes. `git diff --check` passes.
