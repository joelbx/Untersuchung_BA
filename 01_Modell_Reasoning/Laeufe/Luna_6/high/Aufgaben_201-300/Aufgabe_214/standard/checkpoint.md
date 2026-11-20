# Port scanner support checkpoint

Implemented optional per-server nmap scanning.

- Added `PortScanConf`, the supported scan technique enum/mapping, case-insensitive parsing, zero detection, validation for scanner path, techniques, privileges, source port, and non-root capability checks.
- Added the configuration field, TOML loader activation of external scanning, and configtest/scan validation.
- Split native and external scan execution while retaining native scanning by default. External scanning invokes local nmap and parses grepable results.
- Added the commented `portscan` example to the generated config template.

Verification: `go test ./config ./scanner ./subcmds` passed; `git diff --check` passed. The build emitted the existing sqlite3 C compiler warning.
