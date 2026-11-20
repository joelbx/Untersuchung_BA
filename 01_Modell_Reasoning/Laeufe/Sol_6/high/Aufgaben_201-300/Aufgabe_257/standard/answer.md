Updated the repository so `tsh.Run` applies runtime options after parsing and returns command errors to its caller. Command handlers, including database handlers, now return errors instead of exiting. A new `client.SSOLoginFunc` lets tests inject a mocked SSO response.

Service startup now propagates OS assigned listener addresses, including ports assigned from `:0`, to auth and proxy configuration. Added focused tests for SSO injection, returned tsh errors, and bound listener addresses.

Verification passed: `go test ./tool/tsh ./lib/client ./lib/service` and `git diff --check`.