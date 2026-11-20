# Checkpoint

Resolved issue #3292 in checked-out files.

- Removed `BreakUp` and `RangeByChunks` from `utils/slice/slice.go`.
- Changed `CollectChunks` to `(iter.Seq[T], int)`, reusing an internal buffer and cloning yielded chunks to avoid aliasing.
- Added lazy `SeqFunc[I, O]` and tests for lazy evaluation, early stop, chunk independence, and zero chunk size behavior.
- Updated slice callers to `slices.Chunk` and the sequence caller to the new `CollectChunks` order.

Checks executed:
- `gofmt -w utils/slice/slice.go utils/slice/slice_test.go scanner/refresher.go scanner/tag_scanner.go persistence/playlist_repository.go persistence/playqueue_repository.go persistence/sql_genres.go core/playlists.go` — passed.
- `GOTOOLCHAIN=local GOPROXY=off go test ./utils/slice ./scanner ./persistence ./core` — passed.
- `git diff --check` — passed.

Tooling note: `rg` is unavailable (`/bin/bash: rg: command not found`); local `grep` and `find` were used for searches. No check remains blocked.
