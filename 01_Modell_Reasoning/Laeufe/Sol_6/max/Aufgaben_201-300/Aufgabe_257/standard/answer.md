Resolved the tsh test environment issue. `Run` and its command handlers now return errors for callers to assert, and runtime options can inject an SSO login handler through the new `SSOLoginFunc` interface. Auth, proxy, and related service configuration now use bound listener addresses and assigned ports.

The affected package suites pass: `go test ./tool/tsh ./lib/client ./lib/service`.