Removed `BreakUp` and `RangeByChunks`, changed `CollectChunks` to accept an iterator before the chunk size, and added the lazy `SeqFunc` mapper. Updated the affected call sites and added tests for lazy mapping and independent chunk storage.

`go test ./utils/slice ./scanner ./persistence ./core` and `git diff --check` pass.