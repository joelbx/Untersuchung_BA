Added `token` to the audit checker’s resource map and wildcard expansion, so configured token creation and deletion events can be selected. The gRPC auth setup now passes whether `token:deleted` is enabled, and the auth server emits deletion events only when that flag is true. Updated the audit filter documentation.

Relevant existing tests passed:

`GOPROXY=off GOSUMDB=off GOTOOLCHAIN=local go test ./internal/server/audit ./internal/server/auth ./internal/cmd`

`git diff --check` passed.