Added per-server `nmap` scanning with TOML settings, scan technique and source port validation, capability checks, XML result parsing, and native scanner fallback. The discover template now includes a commented `portscan` example.

Verification: `GOPROXY=off go test ./...` passed. The external scanner test uses a fake executable; a live `nmap` scan was not run.