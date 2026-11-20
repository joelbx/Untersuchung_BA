# Checkpoint

Implemented per-server external nmap port scanning. Added `config.PortScanConf`, technique mapping and validation (binary, technique count/support, privilege restrictions, source port, and non-root scanner capabilities). The TOML loader sets `IsUseExternalScanner` from `scannerBinPath`; scan and configtest validation check port scan settings when the port module is enabled. The scanner invokes nmap with argument slices, reads XML output, and retains native scanning when the external scanner is disabled. The discover template includes a commented portscan example.

Checks: `GOPROXY=off GOSUMDB=off go test ./config ./scanner ./subcmds` passed. `git diff --check` passed. A pre-existing sqlite3 C compiler warning appeared, without test failure. No dependencies downloaded.
