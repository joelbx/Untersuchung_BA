Task: support per-server external nmap port scanning.
Status: implemented and verified.
Changes: config/portscan.go adds techniques, TOML fields, validation and capability checks; config loader enables external scanner per server; scanner/portscan.go executes nmap safely and parses XML; native scanner remains default; discover template has commented portscan example. Added config and scanner tests.
Verification: go test ./... passed; git diff --check passed. Existing sqlite3 C compiler warning is unrelated.
