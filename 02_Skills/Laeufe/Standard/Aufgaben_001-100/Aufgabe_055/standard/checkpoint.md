# Checkpoint

Task: support OS version metadata in Trivy scan results and gate package CVE detection.

Implemented:
- Trivy parser sets `Release` from `Metadata.OS.Name` (empty when absent), sets `ServerName` from `ArtifactName`, adds `:latest` to untagged container image names, and leaves `Optional` nil.
- Package CVE detection runs OVAL and GOST only when OS family, release, and packages are present and the result is neither Trivy nor FreeBSD, Raspbian, or pseudo.
- Trivy CVE reuse identifies results through `ScannedBy`.
- Updated parser expectations and added metadata and detector regression tests.

Verification:
- `GOPROXY=off GOSUMDB=off go test ./contrib/trivy/parser/v2 ./detector -count=1` passed.
- `git diff --check` passed.

Tooling: `rg` was unavailable (`/bin/bash: rg: command not found`); searches used local `grep` and `find`. No external research or downloads used.
