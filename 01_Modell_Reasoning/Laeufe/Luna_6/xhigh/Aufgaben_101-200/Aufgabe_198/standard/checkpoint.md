# Checkpoint

Task: Resolve Red Hat OVAL advisory identifiers, package fix-state handling, and remove Red Hat CVE detection via Gost.

Completed:
- Updated goval-dictionary to v0.9.5, which provides AffectedResolution.
- Restricted OVAL advisory IDs to the supported family prefixes and skipped appending unsupported advisories.
- Propagated OVAL resolution states through HTTP/database package collection and PackageFixStatus conversion.
- Removed RedHat.DetectCVEs and mapped Red Hat family Gost clients to the no-op client so OVAL provides detection.
- Added focused regression coverage.

Verification: GOPROXY=off go test ./oval ./gost ./detector passed; git diff --check passed.
