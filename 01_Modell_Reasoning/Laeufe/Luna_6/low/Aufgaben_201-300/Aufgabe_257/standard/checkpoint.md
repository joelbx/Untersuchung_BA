# Checkpoint

Implemented:
- Added `client.SSOLoginFunc` and `Config.MockSSOLogin`; `TeleportClient.ssoLogin` delegates to the injected function when present.
- Added runtime CLI injection through `CLIConf.mockSSOLogin` and `makeClient`.
- Changed tsh `Run` to return errors, accept variadic `RunOption` functions applied after parsing, and dispatch through error-returning handlers. Converted db handlers and removed handler-level fatal exits.
- Updated auth and proxy listener configuration/logging from OS-assigned listener addresses, including web, reverse tunnel, kube, and SSH proxy listeners.

Validation: `go test ./tool/tsh ./lib/client ./lib/service` passes. Final scan and diff review in progress.
