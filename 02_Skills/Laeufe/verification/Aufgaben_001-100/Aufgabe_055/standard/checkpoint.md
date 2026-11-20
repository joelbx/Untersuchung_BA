# Checkpoint

Task: support OS version and consistent Trivy metadata; gate package CVE detection and reuse by scanner identity.

Initial search: `rg -n "setScanResultMeta|isPkgCvesDetactable|DetectPkgCves|reuseScannedCves|trivy-target|ScannedBy" contrib/trivy detector | head -200` could not run because `rg` is unavailable (`/bin/bash: rg: command not found`). Using local `grep`/`find` instead.

Verification pending.

Implementation: Trivy parser now uses ArtifactName (with :latest for untagged container images), copies Metadata.OS.Name into Release, and clears Optional. The detector identifies Trivy via ScannedBy and skips OVAL/GOST for missing or unsupported metadata, logging skip reasons and returned detector errors. Updated parser expectations and added focused metadata and detector tests.

Verification:
- `GOPROXY=off GOTOOLCHAIN=local go test ./contrib/trivy/parser/v2 ./detector` exited 0: both packages reported `ok` (final run: parser cached; detector 0.015s).
- `git diff --check` exited 0.
