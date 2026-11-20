VERDICT: ACCEPT

I found no correctness or regression issue in the checked-out patch. The removed functions’ call sites use `CollectChunks`, and yielded chunks have independent backing arrays.

Tests passed: `GOPROXY=off GOSUMDB=off go test -mod=readonly ./utils/slice ./persistence ./scanner ./core` — all four packages passed. `git diff --check` also passed.

TEST_ENVIRONMENT_PROBLEM: None. Review recorded in [checkpoint.md](/app/.codex-role-output/checkpoint.md).