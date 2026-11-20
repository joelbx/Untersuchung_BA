Task: add optional per-server nmap port scanning.
Implemented config.PortScanConf, case-insensitive scan type mapping, validation, TOML load flag setup, nmap scan execution with native fallback, and commented discover config example.
Verification: go test ./config ./scanner ./models ./subcmds passed.
Follow-up review: checking requirements coverage and working tree.
