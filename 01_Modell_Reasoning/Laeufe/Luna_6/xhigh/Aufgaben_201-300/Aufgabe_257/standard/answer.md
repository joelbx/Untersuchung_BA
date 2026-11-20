Implemented the SSO login override, error-returning tsh command handlers, and runtime listener address propagation for Auth and Proxy. Startup logs now report bound addresses, and the proxy SSH listener is retained in `proxyListeners`.

Verification passed: `go test ./tool/tsh ./lib/client ./lib/service` and `git diff --check`.

Key changes: [tsh.go](/app/tool/tsh/tsh.go), [db.go](/app/tool/tsh/db.go), [api.go](/app/lib/client/api.go), [service.go](/app/lib/service/service.go), [signals.go](/app/lib/service/signals.go).