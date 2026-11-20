# Checkpoint

Task: support Trivy OS version and artifact metadata; gate package CVE detection; identify Trivy scans by ScannedBy.
Status: implemented and verified.

Changes:
- Trivy parser sets ServerName from ArtifactName, appends :latest to untagged container images, sets Release from Metadata.OS.Name, and clears Optional.
- Package CVE detection skips missing or unsupported OS metadata, empty package sets, and Trivy results; OVAL and GOST errors are logged and returned.
- Trivy result recognition uses ScannedBy.

TDD: parser fixture expectations and new detector tests failed before implementation; stale Release test failed before its fix.
Verification: `GOPROXY=off GOSUMDB=off go test ./contrib/trivy/parser/v2 ./detector -count=1` passed; `GOPROXY=off GOSUMDB=off go test ./...` passed.
