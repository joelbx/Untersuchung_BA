Implemented Trivy OS version extraction, artifact-based server names with `:latest` for untagged container images, and nil `Optional` metadata. Package CVE detection now skips Trivy scans and unsupported or incomplete OS results, logging the reason; OVAL/GOST errors are logged and returned. Trivy scan reuse now checks `ScannedBy`.

Updated parser expectations and recorded progress in `.codex-role-output/checkpoint.md`.

Verification passed: `go test ./contrib/trivy/parser/v2 ./detector` and `git diff --check`.