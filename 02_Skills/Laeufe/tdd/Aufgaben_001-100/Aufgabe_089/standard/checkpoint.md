# Checkpoint

Task: fix referential validation and snapshot loading in `/app`.

Status: implementation complete; targeted tests pass.

Changes:
- `internal/cue.Validate` returns one error with individually unwrap-able, positioned validation issues. Rule segment and variant references are checked, including boolean flag rules and multi-segment rules.
- `SnapshotFromFS` and `SnapshotFromPaths` validate files before constructing an exported `StoreSnapshot`.
- CLI validation renders the new error shape. Valid CUE fixtures were corrected to reference existing variants; snapshot fixtures now use decimal percentages accepted by the schema. Variant names are optional in the schema, matching existing imported state.

TDD: `TestValidate_UnknownReferences` first failed because validation returned nil. `TestSnapshotRejectsUnknownVariantOnEveryLoad` first failed because snapshot creation returned nil error. `TestValidate_Failure` was extended and failed because schema errors prevented reference checks; it now passes.

Verification: `GOTOOLCHAIN=local GOPROXY=off go test ./internal/cue ./internal/storage/fs ./cmd/flipt -count=1` passed. `git diff --check` passed.

Full-suite limit: `GOTOOLCHAIN=local GOPROXY=off go test ./... -count=1` failed in `go.flipt.io/flipt/internal/cache/redis`: `TestSet`, `TestGet`, and `TestDelete` cannot start Redis because `Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?`. All other packages reported pass or no test files. No dependencies were downloaded.
