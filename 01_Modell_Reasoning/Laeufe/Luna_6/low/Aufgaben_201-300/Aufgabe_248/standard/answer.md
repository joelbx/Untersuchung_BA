Implemented the iterator refactor. Removed `BreakUp` and `RangeByChunks`, migrated their production callers, changed `CollectChunks` to accept the sequence first, and added lazy `SeqFunc`. Each yielded chunk gets its own backing array to prevent aliasing.

`go test ./utils/slice ./persistence ./scanner ./core` passed, and `git diff --check` passed.