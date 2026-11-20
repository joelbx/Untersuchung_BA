The change is centered in [utils/slice/slice.go](/app/utils/slice/slice.go:65): remove `BreakUp` and `RangeByChunks`, change `CollectChunks` from `(size, sequence)` to `(sequence, size)`, and add lazy `SeqFunc`.

Removing the old functions also requires migrating callers in the playlist and playqueue repositories, genre queries, and scanner. [core/playlists.go](/app/core/playlists.go:136) and [slice_test.go](/app/utils/slice/slice_test.go:113) use the old `CollectChunks` argument order. The tests also call `BreakUp`.

The behavior to preserve is empty input, a final partial chunk, and early termination on callback error or iterator stop. If `CollectChunks` reuses a buffer, each yielded chunk needs independent storage so retained chunks cannot change. The expected behavior for a nonpositive chunk size is unspecified.

I updated [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md) with these findings. Project source and tests were not edited or run; this run was limited to fault localization.