# Checkpoint

Implemented trusted reverse proxy authentication using configurable `ReverseProxyWhitelist` and `ReverseProxyUserHeader` (default `Remote-User`). The whitelist matcher accepts IPv4/IPv6 CIDRs and addresses with ports, ignores malformed entries, disables auth for an empty list, and supports `@` for Unix socket requests. Trusted header users are looked up or created (the first user becomes admin), receive a JWT and Subsonic credentials, and have last login updated. The index only receives `auth` when that flow succeeds; the UI initializes local storage from that payload.

Log redaction now recursively handles string-keyed nested maps and formats non-string values before regex redaction while retaining map keys.

Verification: `go test ./server/app ./log ./conf` passes; `git diff --check` passes. No git history, index baseline, or harness configuration changed.
