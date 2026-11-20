Updated `tsh` so `Run` applies runtime options after parsing and returns command errors to callers. Added the SSO login override, and changed auth and proxy startup to propagate OS-assigned listener addresses instead of configured `:0` addresses.

Regression tests cover SSO injection, CLI error returns, and assigned ports. `go test ./tool/tsh ./lib/client ./lib/service -count=1` passed.