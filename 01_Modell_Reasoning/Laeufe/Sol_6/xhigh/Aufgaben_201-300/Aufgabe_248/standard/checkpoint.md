# Issue 3292 checkpoint

Completed: removed BreakUp and RangeByChunks; migrated their callers to Go 1.23 iterator APIs. CollectChunks now accepts (iter.Seq[T], chunk size), reuses its internal buffer, and clones yielded chunks to avoid aliasing. Added lazy SeqFunc and updated slice tests for retained chunks and early stopping.

Verification: GOTOOLCHAIN=local GOPROXY=off go test ./utils/slice ./core ./scanner ./persistence passed. After the final slice edge-case and early-stop changes, go test ./utils/slice passed. git diff --check passed.
