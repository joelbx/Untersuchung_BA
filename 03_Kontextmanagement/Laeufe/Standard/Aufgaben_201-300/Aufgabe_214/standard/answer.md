Added per-server external nmap scanning with technique, privilege, source port, and scanner path validation. Servers without an external scanner path continue using the built-in scanner. The discover template now includes a commented `portscan` example.

Verified with `GOPROXY=off go test ./config ./scanner ./subcmds` and `git diff --check`.