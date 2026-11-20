# Checkpoint

Issue: tsh testability, SSO override, and bound listener addresses.

Process: investigating root causes before fixes. `rg` is unavailable (`/bin/bash: rg: command not found`); using local grep/find instead.

Checks: pending.

Root cause: handlers and `Run` terminate on errors; `makeClient` has no SSO override path. Auth computes advertised address from configured `:0` after binding. Proxy builds web settings before its SSH listener is bound, so web handler advertises `:0`; it also logs and passes configured addresses after binding.

Pattern: `kube`/`mfa` command handlers already return errors to `Run`. Listener objects provide `Addr()`, and `utils.NetAddr` stores `.Addr`. Hypothesis: binding proxy SSH before constructing web settings and replacing bound address values at each listener boundary will propagate assigned ports; returning handler errors through `Run` will permit assertions.

Pre-fix reproduction: adding an SSO injection test and compiling it should fail because `Config.MockSSOLogin` and `SSOLoginFunc` do not exist.

Implemented: `Run(args, opts...) error` applies options after parsing and returns handler errors. Every tsh command handler, including database handlers, returns errors; only `main` calls `utils.FatalError`. `refuseArgs` returns a bad parameter error. SSO callback type/field and tsh propagation are wired, with direct callback test. Auth, proxy SSH, web, tunnel, and kube listeners update configuration from `Addr()` after binding. Proxy SSH binds before web handler settings are made and is owned by `proxyListeners`.

Verification: Pre-fix `go test ./lib/client -run '^TestMockSSOLogin$' -count=1` failed as expected (`unknown field 'MockSSOLogin' in struct literal of type Config`). Final `go test ./tool/tsh ./lib/client ./lib/service -count=1` passed (all three packages). `go test ./lib/service -run '^TestMonitor$' -count=1` passed, including the new auth address assertion. `git diff --check` passed. No offline tooling blocked checks. No dependencies were downloaded.
