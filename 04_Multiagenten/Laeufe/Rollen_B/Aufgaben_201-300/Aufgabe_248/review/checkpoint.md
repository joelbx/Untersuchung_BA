VERDICT: ACCEPT

Reviewed the checked-out patch and affected call sites in `core`, `persistence`, `scanner`, and `utils/slice`. `BreakUp` and `RangeByChunks` are removed, `CollectChunks` takes the sequence first, and `SeqFunc` maps lazily. Cloning yielded chunks prevents aliasing when the internal buffer is reused. No code defects found.

Tests: `GOPROXY=off GOSUMDB=off go test -mod=readonly ./utils/slice ./persistence ./scanner ./core` passed for all four packages. `git diff --check` passed. No TEST_ENVIRONMENT_PROBLEM.
