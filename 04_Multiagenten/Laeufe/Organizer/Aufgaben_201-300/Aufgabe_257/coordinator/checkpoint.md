# Checkpoint

Issue resolved in checked-out files.

- tsh Run accepts runtime options after parsing/default resolution and returns handler errors; main remains the process-level error handler.
- tsh and database command handlers return errors; refuseArgs returns errors.
- CLIConf, client.Config, and client.ssoLogin support an injected SSOLoginFunc.
- Auth and proxy listener addresses are updated from bound listeners, including proxy SSH, before dependent services and reported settings use them.
- Focused SSO and CLI tests added. `git diff --check` and `go test ./tool/tsh ./lib/client ./lib/service -count=1` passed.
- Adopted service patch from agent-1 and tsh patch from agent-2. Coordinator integrated client hook, database handlers, tests, and final cleanup.
