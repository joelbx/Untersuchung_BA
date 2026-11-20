Implemented trusted reverse proxy login in `/app`. Administrators can configure `ReverseProxyWhitelist`, `ReverseProxyUserHeader` (default `Remote-User`), and an optional `ReverseProxyDefaultUser`. Trusted requests receive a session in the frontend configuration; untrusted requests receive no `auth` field. The change also provisions users on first proxy login, stores the session in the UI, and redacts sensitive values in nested log maps.

Added configuration guidance in [README.md](/app/README.md) and updated the required [checkpoint](/app/.codex-role-output/checkpoint.md).

Verification passed: `go test ./...`, the existing frontend suite, the new frontend session test, and `git diff --check`.