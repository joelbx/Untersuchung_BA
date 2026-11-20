Removed `BreakUp` and `RangeByChunks`, migrated their callers, and changed `CollectChunks` to accept a sequence first. Added lazy `SeqFunc` and made yielded chunks independent while reusing the collection buffer.

`go test ./utils/slice ./core ./scanner ./persistence` passes.