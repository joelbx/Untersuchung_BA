Implemented the SSO mock hook, runtime listener address propagation, and error returns through tsh handlers and `Run`.

Verification passed: `go test ./tool/tsh ./lib/client ./lib/service` and `git diff --check`. The checkpoint is recorded in `.codex-role-output/checkpoint.md`.