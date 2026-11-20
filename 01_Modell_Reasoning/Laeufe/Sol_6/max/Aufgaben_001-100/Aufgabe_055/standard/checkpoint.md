# Trivy OS version parsing

Status: implementation complete; relevant tests pass.

Changes: Trivy parser stores OS Name in Release, uses ArtifactName for ServerName (adding :latest to untagged container images), and leaves Optional nil. Package CVE detection skips incomplete, unsupported, and Trivy results; reuse checks ScannedBy.

Verification: `GOPROXY=off GOSUMDB=off go test ./contrib/trivy/parser/v2 ./detector` and `GOPROXY=off GOSUMDB=off go test ./contrib/trivy/...` passed.
