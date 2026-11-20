# Fault localization checkpoint

Inspected `tool/tsh/tsh.go`, `tool/tsh/db.go`, `lib/client/api.go`, `lib/service/service.go`, and existing tests. No project source or tests changed.

- `Run(args []string)` is void and calls `utils.FatalError` for parse, executable path, and dispatch errors. Its handlers also return void and exit. `refuseArgs` exits. Database handlers are in `tool/tsh/db.go`, including an additional fatal call in `databaseLogin`.
- `CLIConf` and `client.Config` lack an SSO override; `TeleportClient.ssoLogin` always calls `SSHAgentSSOLogin`. `makeClient` builds a default config but has no propagation point for a callback.
- Auth binds `cfg.Auth.SSHAddr` at service.go:1215, then uses the configured `:0` in logs and advertised address at 1249 and 1276. `NewTeleport` copies `cfg.Auth.SSHAddr` to `AuthServers` before binding when no auth servers are supplied (605), requiring update after bind.
- Proxy listener setup at 2212-2320 binds web, tunnel, and kube listeners but does not capture their assigned addresses. SSH listener is bound later at 2559 and absent from `proxyListeners`. Proxy settings, web handler, regular SSH proxy, kube dial address, and logs still use config addresses.
- Existing `lib/service/service_test.go:96-116` exercises random auth port for diagnostic readiness; it does not establish end-to-end tsh SSO or proxy address propagation. Existing tsh tests do not call `Run`.
