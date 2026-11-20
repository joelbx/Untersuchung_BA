Issue #3292: Refactor slice chunk utilities to Go 1.23 iterators.
Status: implemented and verified.
Changes: removed BreakUp and RangeByChunks; CollectChunks now accepts iter.Seq first and chunk size second, reuses a collection buffer and clones yielded chunks; added lazy SeqFunc; migrated all repository callers and updated slice tests.
Validation: GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test ./utils/slice ./scanner ./persistence ./core (all passed).
