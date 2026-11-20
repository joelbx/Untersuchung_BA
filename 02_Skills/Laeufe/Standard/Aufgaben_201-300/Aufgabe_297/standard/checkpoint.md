# Checkpoint

Implemented trusted reverse proxy login using `ReverseProxyWhitelist` and `ReverseProxyUserHeader` (default `Remote-User`). Whitelist validation accepts IPv4/IPv6 CIDRs, exact IPs, IP:port peers and entries, and `@` for Unix sockets. Invalid entries are skipped. The server no longer applies `RealIP` middleware, so forwarded headers cannot replace the connection peer for authentication checks.

Trusted requests with a username create the user when absent (first user is admin), update LastLoginAt, create a signed token and Subsonic salt/token, and expose the auth payload in the UI config. The UI stores those fields in local storage. Untrusted or unauthenticated requests have no auth object. Logs no longer print the UI config; nested map redaction preserves keys and redacts sensitive values.

Checks completed successfully:
- `GOPROXY=off go test ./server/app ./log ./server ./conf`
- `CI=true npm test -- --watch=false --runInBand` (11 suites, 35 tests)
- `npm run lint`
- `./node_modules/.bin/prettier --check src/authProvider.js src/authProvider.test.js`
- `git diff --check`

`rg` was unavailable (`/bin/bash: rg: command not found`); local grep/find were used. No other tooling blocked a check.
