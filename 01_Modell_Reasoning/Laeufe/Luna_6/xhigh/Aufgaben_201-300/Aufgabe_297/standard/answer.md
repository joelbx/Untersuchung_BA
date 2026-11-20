Implemented reverse proxy authentication with configurable `ReverseProxyWhitelist` and `ReverseProxyUserHeader` (default `Remote-User`). Whitelisted peers can sign in through the header; missing users are created, the first user becomes admin, and the UI receives current identity, JWT, and Subsonic credentials. The frontend stores those credentials before checking authentication. Untrusted requests receive no auth payload.

Whitelist checks use the original socket peer, support IPv4/IPv6 CIDRs and `IP:port` addresses, ignore invalid entries, and allow Unix sockets via `@`. Log redaction now handles sensitive keys and values in nested maps.

Updated [configuration.go](/app/conf/configuration.go), [auth.go](/app/server/app/auth.go), [serve_index.go](/app/server/app/serve_index.go), [server.go](/app/server/server.go), [request.go](/app/model/request/request.go), [redactrus.go](/app/log/redactrus.go), and [authProvider.js](/app/ui/src/authProvider.js).

**Verification passed:** Go suites for app, server, log, and request; UI tests (10 suites, 34 tests); UI lint; and `git diff --check`.