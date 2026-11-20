Removed `BreakUp` and `RangeByChunks`, changed `CollectChunks` to accept `(sequence, size)`, and added lazy `SeqFunc`. I migrated all callers and updated the slice tests. `CollectChunks` reuses its internal buffer while copying yielded chunks so retained chunks remain independent.

Tests passed for `./utils/slice`, `./core`, `./scanner`, and `./persistence`.