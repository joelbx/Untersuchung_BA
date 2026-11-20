Updated tsh to return command errors through `Run`, apply runtime options after parsing, and pass a mock SSO login handler to the client. Auth and proxy services now propagate OS-assigned listener addresses to their configuration and dependent components.

Verification passed: `go test -count=1 ./tool/tsh ./lib/client ./lib/service` and `git diff --check`.