# Checkpoint

Objective: make tsh command handlers return errors, support runtime SSO login injection, and propagate bound auth/proxy addresses.
Status: implementation complete. `Run` accepts post-parse options and returns handler errors; CLI handlers return errors; client SSO hook is injectable; auth and proxy config uses listener addresses after binding. Focused tests passed in tool/tsh, lib/client, and lib/service.
