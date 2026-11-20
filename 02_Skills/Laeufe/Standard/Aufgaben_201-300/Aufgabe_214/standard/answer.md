Added per-server `nmap` scanning with technique, privilege, binary, and source-port validation. Servers without `scannerBinPath` continue using the built-in scanner. The discover template now includes a commented `portscan` example.

`GOPROXY=off GOSUMDB=off go test ./config ./scanner ./subcmds` and `git diff --check` passed.