# Checkpoint

- Repository: `/app`
- Initial working tree was clean.
- Implemented `ReverseProxyWhitelist` (comma-separated IPv4/IPv6 CIDRs and IP entries, `IP:port`, invalid-entry tolerance, and Unix socket `@`) and `ReverseProxyUserHeader` with default `Remote-User`.
- Preserved the socket peer before `RealIP` middleware; reverse proxy auth only runs for a whitelisted peer with a non-empty configured username header.
- Trusted requests create missing users (first user is admin), update login time, generate a JWT and Subsonic credentials, and place auth in the UI config. Untrusted requests have no auth object.
- Frontend persists the injected token, identity, role, avatar, and Subsonic credentials before auth checks. Log redaction handles sensitive map keys and nested map values.
- Verification passed: `go test ./server/app ./server ./log ./model/request`; `npm test -- --watchAll=false --runInBand` (10 suites, 34 tests); `npm run lint`; `git diff --check`.
