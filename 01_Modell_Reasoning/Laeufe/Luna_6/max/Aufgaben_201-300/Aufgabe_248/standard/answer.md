Implemented Issue #3292.

- Removed `BreakUp` and `RangeByChunks`, and migrated their callers to Go’s `slices.Chunk`.
- Changed `CollectChunks` to accept the sequence before the chunk size. It reuses an internal buffer and clones yielded chunks to prevent aliasing.
- Added lazy `SeqFunc` mapping and updated callers and existing tests for the new API.

Verification passed: `go test ./utils/slice ./core ./scanner ./persistence`

Key changes: [slice.go](/app/utils/slice/slice.go), [sql_genres.go](/app/persistence/sql_genres.go), [slice_test.go](/app/utils/slice/slice_test.go).