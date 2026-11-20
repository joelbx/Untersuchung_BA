# Checkpoint

Investigating validation and snapshot loading. External research unavailable; using local code and tests only.

## Status
- Started root cause investigation; no source edits yet.

## Root cause and hypothesis
- CUE validates field shapes only; no referential key lookup exists. `Validate` returns CUE errors through `Result` but no reference errors.
- Snapshot assembly checks missing segments but silently skips missing variants, so invalid files can become snapshots.
- Import creates resources before failing on references, explaining different results on retry when DB state remains.
- Hypothesis: validating references against keys declared in each document before import/snapshot construction will consistently reject invalid files. YAML nodes provide source locations.
- Existing fixtures labeled valid contain undeclared variant keys; their data must be corrected to satisfy the new contract.

## Resolution
- Reproduced the reference gap with `GOPROXY=off go test ./internal/cue -run TestReferenceReproduction -count=1`: failed because Validate returned nil for missing segment and variant.
- Added source-positioned reference checks and multi-error unwrapping; changed Validate to return error only.
- Added validation before CLI import creates or modifies database resources; repeated invalid imports now return the same errors.
- Exported StoreSnapshot, SnapshotFromFS, and SnapshotFromPaths. Snapshot constructors validate file contents before assembly.
- Updated old fixtures with concrete variant names and float rollout percentages required by the existing CUE schema.
- Added regression tests for references, boolean rules, both snapshot constructors, and repeated import attempts.

## Verification
- `GOPROXY=off go test ./internal/cue/... ./internal/storage/fs/... ./internal/ext/... ./cmd/flipt -count=1` passed (exit 0).
- `git diff --check` passed (exit 0).
