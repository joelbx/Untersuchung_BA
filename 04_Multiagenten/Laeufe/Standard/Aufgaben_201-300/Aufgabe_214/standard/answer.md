Added per-server external `nmap` scanning while retaining native scanning when no scanner path is configured. The change includes technique and source port validation, TOML loading, XML result parsing, and a commented `portscan` example in the discovery template.

Relevant tests pass: `go test ./config ./scanner ./subcmds`.