# Checkpoint

Task: add audit logging support for token creation and deletion.

Root cause: token audit emitters already existed, but `NewChecker` rejected `token` and omitted it from wildcard expansion. gRPC initialization passed only sink-enabled status to the authentication server, so deletion ignored the configured event filter.

Reproduction: `GOTOOLCHAIN=local GOPROXY=off go test ./internal/server/audit -run TestCheckerTokenEvents -count=1` failed before the fix with `invalid noun: token` and missing token wildcard matches.

Change: add token to checker nouns and wildcard mapping; construct the checker before authentication initialization when an audit sink is enabled; pass `checker.Check("token:deleted")` to the authentication gRPC setup, which supplies it to the existing audit logging option. Document token filtering.

Verification: `GOTOOLCHAIN=local GOPROXY=off go test ./internal/server/audit ./internal/server/auth ./internal/cmd -count=1` passed. `git diff --check` passed. `rg` was unavailable (`/bin/bash: line 1: rg: command not found`), so local searches used `find` and `grep`.
