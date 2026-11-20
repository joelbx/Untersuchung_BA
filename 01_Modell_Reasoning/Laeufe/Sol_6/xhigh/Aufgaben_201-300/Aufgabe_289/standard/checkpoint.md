# Checkpoint

Implemented `DefaultConfig` and exported `DecodeHooks`; `Load` composes the exported hooks. Changed storage sub-configurations to pointers and fixed the CUE `boolean` type typo. `GOPROXY=off GOSUMDB=off go test ./internal/config ./internal/cmd` passes, including direct CUE schema and duration hook checks. `git diff --check` passes.
