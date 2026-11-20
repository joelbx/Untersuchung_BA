# Checkpoint

Task: make tsh command errors return to callers, inject SSO login, and propagate bound auth/proxy listener addresses.

Changes:
- `Run` returns errors and accepts post-parse `func(*CLIConf)` options; command handlers in `tool/tsh/tsh.go` and `tool/tsh/db.go` return errors. `main` retains CLI fatal behavior.
- Added `client.SSOLoginFunc`, `Config.MockSSOLogin`, tsh configuration propagation, and the SSO override call.
- Auth and proxy startup store bound listener addresses in configuration before dependent components use them. SSH proxy listener is retained in `proxyListeners`.
- Added tests for returned CLI errors, SSO override/propagation, and assertions on assigned Auth, web proxy, and SSH proxy ports.

Checks:
- `rg` unavailable: `/bin/bash: rg: command not found`; used grep.
- `go test ./tool/tsh ./lib/client ./lib/service -run '^$'`: passed (compile check).
- `go test ./tool/tsh ./lib/client -run '^(TestRunReturnsErrors|TestMakeClientPropagatesSSOLogin|TestSSOLoginOverride)$' -count=1`: passed.
- `go test ./tool/tsh -run '^TestTshMain$' -count=1`: passed.
- `go test ./tool/tsh ./lib/client ./lib/service -run '^(TestTshMain|TestClientAPI|TestGetAdditionalPrincipals)$' -count=1`: passed.
- `go test ./tool/tsh ./lib/client ./lib/service -run '^(TestTshMain|TestClientAPI|TestGetAdditionalPrincipals|TestRunReturnsErrors|TestMakeClientPropagatesSSOLogin|TestSSOLoginOverride)$' -count=1`: passed.
- `go test ./tool/tsh -run '^(TestRunReturnsErrors|TestMakeClientPropagatesSSOLogin|TestTshMain)$' -count=1`: passed after adding the runtime option assertion.
- `git diff --check`: passed.
