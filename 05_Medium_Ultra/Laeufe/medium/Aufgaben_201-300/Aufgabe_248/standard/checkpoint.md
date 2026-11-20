Issue #3292 complete. Removed BreakUp and RangeByChunks. CollectChunks now takes (iter.Seq[T], int), reuses a buffer, and clones yielded chunks to prevent aliasing. Added lazy SeqFunc. Migrated all Go call sites in scanner, persistence, and core; updated slice tests.
Verification: GOPROXY=off GOSUMDB=off go test ./utils/slice ./persistence ./scanner ./core passed. git diff --check passed.
