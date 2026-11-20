Removed `BreakUp` and `RangeByChunks`, changed `CollectChunks` to accept an `iter.Seq` followed by chunk size, and added lazy `SeqFunc` in [slice.go](/app/utils/slice/slice.go). Updated all callers and tests. Collected chunks have independent backing arrays.

Verification passed: `go test ./utils/slice ./scanner ./persistence ./core` and `git diff --check`.