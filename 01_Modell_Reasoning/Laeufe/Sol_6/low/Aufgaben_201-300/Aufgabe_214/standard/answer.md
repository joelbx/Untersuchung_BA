Added per-server `nmap` scanning with scan technique and source port validation, XML result parsing, and a commented `portscan` example in the generated config. Servers without an external scanner path continue to use native scanning.

`go test ./config ./scanner ./subcmds` passed.