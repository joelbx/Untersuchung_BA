Removed `BreakUp` and `RangeByChunks`, migrated existing callers, changed `CollectChunks` to accept an iterator first, and added the lazy `SeqFunc` mapper. `CollectChunks` reuses its buffer and clones emitted chunks to prevent aliasing.

Verification passed: `go test ./utils/slice ./scanner ./core` and `git diff --check`.