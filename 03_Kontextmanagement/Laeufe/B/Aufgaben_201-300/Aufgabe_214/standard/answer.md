Implemented per-server `nmap` scanning with technique and source-port validation, while preserving native scanning when no external scanner is configured. The discovery template now includes a commented `portscan` example.

`GOPROXY=off go test ./config ./scanner ./subcmds` and `git diff --check` passed. The external scan test used a local stub executable; it did not run a real `nmap` scan.