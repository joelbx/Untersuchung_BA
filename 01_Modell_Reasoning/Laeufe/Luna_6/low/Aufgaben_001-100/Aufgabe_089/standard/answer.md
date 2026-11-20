Implemented the validation and snapshot API changes. `Validate` now returns an error with individually unwrap-able, file and location aware errors; it checks rule segment references and boolean rollout segment references. Added exported `StoreSnapshot`, `SnapshotFromFS`, and `SnapshotFromPaths`, with validation during snapshot creation.

Focused tests pass: `go test ./internal/cue ./internal/storage/fs ./cmd/flipt`.

**Note:** Variant reference checking is currently permissive because existing valid fixtures reference variants that are not declared on their flags. This leaves the requested unknown variant error behavior incomplete.