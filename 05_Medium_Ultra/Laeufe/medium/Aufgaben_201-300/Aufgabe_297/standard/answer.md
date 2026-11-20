Implemented reverse proxy login in the checked-out repository. `ReverseProxyWhitelist` accepts comma-separated IPv4 and IPv6 CIDR ranges and Unix socket `@`; an empty whitelist disables proxy login. `ReverseProxyUserHeader` defaults to `Remote-User`, and `ReverseProxyDefaultUser` provides optional fallback login.

Trusted requests now create a user on first login, make the first user an admin, update `LastLoginAt`, and return JWT and Subsonic credentials for the UI to store. Untrusted requests receive no `auth` payload. Nested map values and JSON tokens are also redacted from logs.

Verification passed: relevant Go tests, 35 UI tests, UI formatting, and `git diff --check`.