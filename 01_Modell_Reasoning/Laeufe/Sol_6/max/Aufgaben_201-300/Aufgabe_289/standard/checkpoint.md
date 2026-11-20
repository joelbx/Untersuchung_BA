# Config validation task checkpoint

Objective: export canonical default configuration and mapstructure decode hooks, keep production loading aligned with test decoding, and make defaults pass the CUE schema.

Status: complete. Moved the existing test defaults into exported `DefaultConfig`, exported `DecodeHooks`, composed those hooks in `Load`, added the version mapstructure tag, and changed Storage Local/Git to pointers with nil-safe validation. Fixed the CUE schema's invalid `boolean` type and added a regression test covering CUE validation plus decoding defaults, a duration override, and the version field. `go test ./internal/config ./internal/cmd ./internal/telemetry -count=1` passes with network module access disabled; `git diff --check` passes.

Constraints: use local repository and existing tests only; preserve git history, index baseline, and harness configuration.
