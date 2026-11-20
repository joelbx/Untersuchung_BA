# Checkpoint

Task: implement Trivy OS version metadata handling and package CVE detection/reuse behavior.

Completed:
- Trivy results now use ArtifactName as ServerName, add `:latest` to untagged container images, copy Metadata.OS.Name into Release, clear Optional, and preserve the existing supported-result validation.
- Package CVE detection now uses `isPkgCvesDetactable` to skip unsupported/incomplete results and log reasons; OVAL/GOST errors are logged and returned.
- Trivy result reuse now checks ScannedBy. Updated existing parser expectations for the new metadata.

Verification: `go test ./contrib/trivy/parser/v2 ./detector` passes; `git diff --check` passes. No remaining `trivy-target` references in the Trivy parser or detector Go source.
