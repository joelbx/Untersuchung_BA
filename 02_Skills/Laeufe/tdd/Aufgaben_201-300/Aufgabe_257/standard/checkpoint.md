# Checkpoint

Task: make tsh errors recoverable, inject SSO login, and propagate bound listener addresses.

Assigned skill: test-driven-development. Will add a failing test before production changes and run relevant existing tests.

Environment: `rg` unavailable (`/bin/bash: rg: command not found`); using grep/find.

RED: `go test ./tool/tsh ./lib/client -run 'TestRunReturnsParseError|TestMockSSOLoginOverride|TestSSOLoginUsesConfiguredOverride' -count=1` failed at compile because Run had no error result and the SSO override fields/type were absent. This is the expected missing interface; runtime assertion cannot compile until it exists.

RED: `go test ./lib/service -run '^TestMonitor$' -count=1` failed at service_test.go:120 because `process.Config.Auth.SSHAddr.Addr` remained `127.0.0.1:0` after startup.

GREEN: `go test ./tool/tsh ./lib/client -run 'TestRunReturnsParseError|TestMockSSOLoginOverride|TestSSOLoginUsesConfiguredOverride' -count=1` passed. `go test ./tool/tsh ./lib/client ./lib/service -run 'TestRunReturnsParseError|TestMockSSOLoginOverride|TestSSOLoginUsesConfiguredOverride|TestMonitor' -count=1` first failed because the tsh test lacked a required proxy address, then passed after fixing its setup. `go test ./tool/tsh -run '^TestRunAppliesOptionsAfterParsing$' -count=1` passed. Final `go test ./tool/tsh ./lib/client ./lib/service` passed.

Repository-wide check: `go test ./...` started and printed success/no-test results for the root, api/client, api/client/proto, api/constants, api/defaults, api/types, api/types/events, api/types/wrappers, api/utils, examples/bench, examples/go-client, and examples/jwt packages. It produced no additional output for several minutes and was interrupted with Ctrl-C (exit code 1). No test failure was reported before interruption; the status of the remaining packages is unknown. This was a time limit on a long-running full suite, not an offline tooling error.

Additional RED: after changing `TestMonitor` to use `AuthServers: localhost:0`, `go test ./lib/service -run '^TestMonitor$' -count=1` failed at service_test.go:121: expected the bound `127.0.0.1:<port>` but got `localhost:0`. GREEN: same command passed after propagating the bound auth address to port-zero auth server entries.

Final targeted verification: `go test ./tool/tsh ./lib/client ./lib/service` passed after the auth alias fix. `git diff --check` passed.

Additional broad compile attempt: `go test ./... -run '^$'` was interrupted with Ctrl-C (exit code 1) after the same initial package results; Go printed multiple `/usr/local/go/pkg/tool/linux_amd64/link: signal: interrupt` and `vet: signal: interrupt` messages. It was interrupted to release resources for the targeted suites. The remaining packages were not compiled or tested by this attempt.
