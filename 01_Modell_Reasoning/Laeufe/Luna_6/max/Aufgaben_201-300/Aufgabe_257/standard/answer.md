Implemented the SSO login override and wired it through `makeClient`. `Run` now accepts runtime options after parsing and returns command errors; tsh handlers and `refuseArgs` return errors instead of exiting.

Auth and Proxy configuration, logs, downstream components, and listener reload descriptors now use OS-assigned addresses, including the SSH proxy listener.

Verification passed: `go test ./tool/tsh ./lib/client ./lib/service` and `git diff --check`.

Changed files: [api.go](/app/lib/client/api.go), [service.go](/app/lib/service/service.go), [signals.go](/app/lib/service/signals.go), [tsh.go](/app/tool/tsh/tsh.go), [db.go](/app/tool/tsh/db.go).