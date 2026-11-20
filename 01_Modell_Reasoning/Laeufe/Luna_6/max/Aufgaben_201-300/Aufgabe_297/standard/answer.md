Implemented trusted reverse proxy authentication. The whitelist accepts comma separated IPv4/IPv6 CIDRs and IP entries with ports; an empty whitelist disables the feature, and `@` supports Unix sockets. Successful header authentication creates missing users (making the first user admin), updates last login, and supplies JWT and Subsonic credentials to initialize the UI session. Unauthenticated requests receive no `auth` config.

Added recursive redaction for sensitive values in nested maps and JSON log strings.

Verification passed: targeted Go tests, all 34 existing UI tests, UI lint, and `git diff --check`.

Key changes: [auth.go](/app/server/app/auth.go:79), [serve_index.go](/app/server/app/serve_index.go:54), [redactrus.go](/app/log/redactrus.go:58), and [authProvider.js](/app/ui/src/authProvider.js:80).