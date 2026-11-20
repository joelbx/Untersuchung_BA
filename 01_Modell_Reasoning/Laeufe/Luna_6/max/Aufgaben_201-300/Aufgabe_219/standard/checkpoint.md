# Checkpoint

Task: Add audit logging support for token creation and deletion events.

Plan:
- Located the event checker and auth gRPC initialization; no repository AGENTS.md guidance is present.
- Added `token` to named and wildcard audit resource mappings.
- Changed auth server initialization to pass whether the configured event checker enables `token:deleted`, and gate token deletion events on that value.
- Updated the audit filter noun list in the package README.
- `GOPROXY=off GOSUMDB=off GOTOOLCHAIN=local go test ./internal/server/audit ./internal/server/auth ./internal/cmd` passed.
- `git diff --check` passed and final diff review is complete.
