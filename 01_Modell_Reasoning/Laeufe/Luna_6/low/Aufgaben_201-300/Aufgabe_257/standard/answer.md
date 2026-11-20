Implemented the SSO injection hook, error-returning tsh handlers and `Run` options, and runtime listener address propagation for auth and proxy services.

Existing focused tests pass: `go test ./tool/tsh ./lib/client ./lib/service`. `git diff --check` is clean.