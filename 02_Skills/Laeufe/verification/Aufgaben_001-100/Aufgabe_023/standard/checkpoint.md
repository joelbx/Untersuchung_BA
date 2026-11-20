# Checkpoint

Task: Make authentication database initialization and cleanup depend on enabled methods that require a database.

Implemented `RequiresDatabase` metadata for every authentication method: token, OIDC, GitHub, and Kubernetes require DB; JWT does not. `AuthenticationConfig.RequiresDatabase` and `ShouldRunCleanup` inspect enabled methods. Authentication startup uses in-memory auth storage and still installs JWT interceptors when no method needs DB. Cleanup skips disabled and non-DB methods. Added config and Local/Git/OCI startup tests; adjusted cleanup test for JWT.

Initial search tool `rg` was unavailable (`/bin/bash: rg: command not found`); used local grep/find.

Verification: `GOPROXY=off GOSUMDB=off go test -count=1 ./internal/config ./internal/cmd ./internal/cleanup` exited 0: config 0.219s, cmd 0.515s, cleanup 15.010s. An earlier run had a compile failure (`internal/cmd/authn.go:148:9: undefined: err`); fixed by declaring `err` within the auth-required branch before rerunning. `git diff --check` exited 0. Restored unrelated Go tooling change to go.work.sum.
