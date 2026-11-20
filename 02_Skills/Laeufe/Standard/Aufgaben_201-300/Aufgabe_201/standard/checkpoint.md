# Checkpoint

Task: support string and keys/operator object formats for rule `segment`.

Completed: unified `Rule.Segment` with `SegmentEmbed`, `IsSegment`, `SegmentKey`, and `Segments`; strict YAML decoding and marshaling; import/export and filesystem snapshot conversion; SQL rule and rollout single-key OR fallback on reads and writes; requested fixtures and focused tests.

Verification: `go test ./internal/ext ./internal/storage/fs/... ./internal/storage/sql/...` passed. `git diff --check` passed. `rg` was unavailable, so repository searches used `grep` and `find`.
