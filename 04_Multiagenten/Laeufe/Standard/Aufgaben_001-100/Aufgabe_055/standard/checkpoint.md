Task: Support OS release metadata in Trivy v2 scan results and gate package CVE detection accordingly.
Status: complete.
Changes: parser uses ArtifactName (adding :latest for untagged container images), Metadata.OS.Name for Release, and leaves Optional nil; package detection skips unsupported cases and Trivy; scanned CVE reuse uses ScannedBy.
Verification: go test ./contrib/trivy/parser/v2 ./detector passed; git diff --check passed.
