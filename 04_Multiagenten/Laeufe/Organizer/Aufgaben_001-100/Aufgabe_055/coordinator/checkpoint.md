Task: implement Trivy OS version metadata and package CVE detection gating.
Status: code and focused tests edited; gofmt applied; relevant Go package tests running with GOPROXY=off.
Changes: parser uses ArtifactName (+ :latest for untagged container images), Metadata.OS.Name for Release, nil Optional; detector uses ScannedBy for Trivy CVE reuse and gates OVAL/GOST on metadata and supported scan types.
Constraints: local code/tests only; no git history, index baseline, or harness configuration changes.
