# Checkpoint: image digest support

## Issue
Support image references by either tag or digest throughout config, scanning, and reporting. Reject missing or conflicting identifiers with the specified validation errors.

## Initial state
- Repository: `/app`
- No `AGENTS.md` files were found under the parent workspace.
- Working tree was clean at inspection.

## Plan
1. Trace image structs, validation, conversion, scan domains, and report identifiers.
2. Add digest support and use the full image reference consistently.
3. Run relevant existing tests and record results.

## Implementation progress
- Added `Digest` and `(*Image).GetFullName()` to config image data; added `Digest` to scan result images.
- Updated image validation for exactly one of tag or digest, with the required messages.
- Propagated digest during model conversion, used the full reference for image scans and detection logs, made per-image server names index based, and updated report UUID identifiers to use `name:tag` or `name@digest` plus `@serverName`.
- Next: run existing tests for the touched packages and review the final diff.

## Verification
- `go test -vet=off ./config ./models ./scan ./report`: config, scan, and report passed; models failed in existing `TestScan` with `no vuln found : actual: []`.
- `go test -vet=off ./models -run '^$'`: passed (package compiles).
- Plain `go test ./config ./models ./scan ./report` additionally reports pre-existing vet warnings in `models/library.go` (int-to-string conversions); the report implementation compile error found in that run was fixed before the second pass.
- `git diff --check`: passed.
