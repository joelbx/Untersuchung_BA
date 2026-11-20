# Checkpoint

Issue: make tsh and service listener behavior testable by returning CLI errors, supporting an injectable SSO login handler, and propagating actual listener addresses after binding.

Completed:
- Added `client.SSOLoginFunc`, `Config.MockSSOLogin`, mock dispatch in `TeleportClient.ssoLogin`, and tsh `WithMockSSOLogin` runtime configuration propagated by `makeClient`.
- Converted tsh command handlers, including database handlers, to return errors. `Run` now returns parse and handler errors, applies runtime options after parsing, and `main` reports errors at the process boundary.
- Updated auth and proxy setup to propagate listener-assigned addresses into service config and matching dependent addresses. The SSH proxy listener is retained in `proxyListeners`, and startup logs use bound addresses.

Verification completed: `go test ./tool/tsh ./lib/client ./lib/service` passed. `git diff --check` passed.
