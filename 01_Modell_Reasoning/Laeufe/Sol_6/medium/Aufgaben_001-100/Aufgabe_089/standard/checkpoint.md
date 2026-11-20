Task: Fix referential validation consistency for validate, import, and filesystem snapshots.
Status: Complete.
Changes: internal/cue.Validate now returns a multi-error with file/line/column details and checks variant/segment references; exported cue.Unwrap. SnapshotFromFS and SnapshotFromPaths validate each file and return *StoreSnapshot. Import validates before writes. Updated valid fixtures and CUE schema to reflect accepted snapshot inputs. Added regression tests for references, snapshot paths, and repeated invalid imports.
Verification: go test ./cmd/flipt ./internal/cue ./internal/storage/fs/... passed; git diff --check passed.
