# Checkpoint

## Issue
Implement trusted reverse-proxy authentication using configurable user header and CIDR whitelist, initialize frontend auth state, and redact secrets in nested/map log values.

## Completed
- Added `ReverseProxyWhitelist` and `ReverseProxyUserHeader` config fields, with `Remote-User` as the default.
- Added whitelist validation for IPv4/IPv6 IP and CIDR values, optional host ports, and Unix socket `@` entries. Empty/malformed-only whitelist values do not authenticate.
- Added trusted-header login during UI config generation. Existing users have login time refreshed; first-time users are created, and the first user becomes admin. Successful auth returns a signed session token and the requested user/session fields.
- Added frontend initialization from the optional `auth` config payload using the standard local storage keys.
- Added recursive redaction for string-keyed maps, preserving keys, and stringification/redaction for other field types.

## Verification
- `go test ./server/app ./log ./conf` passed.
- `git diff --check` passed.

## Notes
- `rg` is unavailable in this environment; repository searches used `grep` and `find`.
