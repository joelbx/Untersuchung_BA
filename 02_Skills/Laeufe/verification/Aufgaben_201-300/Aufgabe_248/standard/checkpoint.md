# Issue #3292 checkpoint

Task: migrate slice chunk utilities to Go iterators, remove legacy APIs, add `SeqFunc`.

Initial inspection: `rg` is unavailable (`/bin/bash: rg: command not found`); using local `grep`/`find` instead. Verification pending.

Implementation: removed `BreakUp` and `RangeByChunks`; migrated all Go call sites to sequence-based `CollectChunks`; added lazy `SeqFunc`. `CollectChunks` clones yielded chunks and reuses its collection buffer. Updated slice tests for the new API, independent chunks, and lazy mapping.

Verification completed: `GOTOOLCHAIN=local GOPROXY=off go test ./utils/slice ./scanner ./persistence ./core` exited 0; all four packages reported `ok`. `git diff --check`, `gofmt -l` over changed Go files, and a Go-source search for removed APIs exited 0.
