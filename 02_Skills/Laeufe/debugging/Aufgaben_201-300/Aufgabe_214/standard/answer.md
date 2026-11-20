Added per-server `nmap` port scanning with scan technique, privilege, source port, and scanner path validation. Servers without an external scanner path continue using the built-in scanner. The discover template now includes a commented `portscan` example.

Verified with `GOPROXY=off go test ./config ./scanner ./subcmds -count=1` and `git diff --check`.