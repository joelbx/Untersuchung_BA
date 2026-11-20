# Checkpoint

Task: Repair Red Hat-family OVAL advisory and fix-state processing.

Changes:
- Upgraded cached goval-dictionary dependency to v0.9.5 for AffectedResolution support.
- Filtered distro advisories by family-specific title prefix; skipped unsupported definitions.
- Propagated package resolution state through OVAL evaluation, HTTP/DB collection, fix status conversion, and Red Hat result merging.
- Removed Gost RedHat DetectCVEs and its client selection; Red Hat and rebuild package CVE detection now uses OVAL.
- Added focused tests for advisory IDs, resolution states, and fix status propagation.

Verification:
- `GOPROXY=off GOSUMDB=off go test ./oval ./gost ./detector ./models` exited 0 (all listed packages reported ok).
- `git diff --check` exited 0.
