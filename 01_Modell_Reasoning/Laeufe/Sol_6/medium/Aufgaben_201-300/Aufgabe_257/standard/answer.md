Updated tsh so `Run` and its command handlers return errors to callers, and runtime options can inject a mock SSO login. Auth and proxy services now propagate the addresses assigned when their listeners bind, including random ports.

Added tests for SSO injection, tsh error returns, and the auth listener address. `go test ./tool/tsh ./lib/client ./lib/service` passes.