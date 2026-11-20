# Checkpoint

Task: Resolve the tsh SSO injection, dynamic listener address propagation, and error-return behavior issue.

Completed:
- Added `client.SSOLoginFunc`, `Config.MockSSOLogin`, and the override branch in `TeleportClient.ssoLogin`.
- Added `CLIConf.mockSSOLogin` propagation in `makeClient` and `RunOption` support applied after CLI parsing.
- Changed tsh command handlers (including database handlers) and `refuseArgs` to return errors; `Run` dispatches and returns them. Process exits remain only in `main`'s top-level error handling.
- Updated Auth and Proxy address configuration from bound listener addresses, and stored/used the SSH proxy listener in `proxyListeners`.

Verification:
- `go test ./tool/tsh ./lib/client ./lib/service` passed.
- `git diff --check` passed.
