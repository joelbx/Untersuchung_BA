Updated tsh so `Run` applies runtime options after parsing and defaults, then returns command errors to its caller. Command handlers, including the database handlers, and `refuseArgs` now return errors. Added `client.SSOLoginFunc` and wired the injectable SSO handler through tsh into client login. Auth and proxy startup now propagate bound listener addresses, including the SSH proxy address, when ports are assigned dynamically.

`git diff --check` and `go test ./tool/tsh ./lib/client ./lib/service -count=1` passed.

I adopted both delegated patches: agent-1 handled service listeners, and agent-2 handled the tsh handlers. I integrated the client hook, database handlers, tests, and final cleanup.