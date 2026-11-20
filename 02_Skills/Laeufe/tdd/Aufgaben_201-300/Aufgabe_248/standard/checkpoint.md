# Checkpoint

Task: refactor `utils/slice` chunk helpers for Go 1.23 iterators and add `SeqFunc`.

Completed:
- Removed `BreakUp` and `RangeByChunks` from `utils/slice/slice.go` and migrated all Go callers to `slices.Chunk` or `CollectChunks`.
- Changed `CollectChunks` to accept `(iter.Seq[T], int)`. It reuses a preallocated collection buffer and clones yielded chunks to keep them independent.
- Added lazy `SeqFunc` and tests for mapping, early termination, and chunk independence.
- The new API tests were run before implementation and failed to compile because `SeqFunc` was missing and `CollectChunks` had the old argument order. The chunk independence test alone passed against the old implementation, so it serves as a regression guard rather than a red test.

Verification:
- `GOTOOLCHAIN=local GOPROXY=off go test ./utils/slice ./core ./scanner ./persistence -count=1` passed.
- `GOTOOLCHAIN=local GOPROXY=off go test ./...` passed.
- `git diff --check` passed.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); used local `find`/`grep`.
