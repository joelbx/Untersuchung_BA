Added per-server `nmap` scanning with the requested scan techniques, source port option, validation, and result parsing. Servers without an external scanner path continue to use the native scanner. The discover template now includes a commented `portscan` example.

`go test ./...` and `git diff --check` pass.