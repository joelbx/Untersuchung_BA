Implemented trusted reverse proxy login with configurable header and IPv4/IPv6 CIDR whitelist, including Unix socket `@` support. Successful logins create or update users, issue a token, and initialize the frontend session. Log redaction now handles nested map values.

Verification passed: `go test ./server/app ./log ./conf` and `git diff --check`.

Checkpoint: [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md)