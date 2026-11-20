Removed `BreakUp` and `RangeByChunks`, migrated their callers to Go’s `slices.Chunk`, changed `CollectChunks` to accept `(iter.Seq[T], chunkSize)`, and added lazy `SeqFunc`. `CollectChunks` reuses its collection buffer while copying yielded chunks so retained chunks stay independent.

Tests passed: `go test ./utils/slice ./scanner ./persistence ./core`.