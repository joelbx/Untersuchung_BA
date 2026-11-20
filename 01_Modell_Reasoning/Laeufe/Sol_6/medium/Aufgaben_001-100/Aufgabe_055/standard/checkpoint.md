# Checkpoint

Completed: Trivy parser stores OS Name as Release, names every scan from ArtifactName with :latest for untagged container images, leaves Optional nil, and preserves existing unsupported-result validation. Package CVE detection now gates OVAL and GOST by OS/package metadata and scanner type. Trivy CVE reuse checks ScannedBy.

Verification: GOPROXY=off GOSUMDB=off go test ./contrib/trivy/parser/v2 ./detector passed; git diff --check passed.
