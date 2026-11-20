# Checkpoint

Issue: add per-server external nmap scanning, preserving native scanning.

Root cause: `base.execPortsScan` always used `net.DialTimeout`; `ServerInfo` had no port scan settings or validation. The new focused test initially failed with undefined `PortScanConf` and technique identifiers. A first compile exposed an `os/exec` import collision with scanner's `exec` function; aliasing the import resolved it. The existing scanner tests also depended on `findPortTestSuccessOn`, so its entry point was retained alongside `findPortScanSuccessOn`.

Implemented: TOML portscan configuration, technique mapping and validation, per-server external scanner selection, nmap XML parsing, discover template examples, and regression tests.

Checks: `GOPROXY=off go test ./config ./scanner ./subcmds -count=1` passed. The sqlite3 dependency emits a C compiler warning but does not fail. `rg` was unavailable (`/bin/bash: rg: command not found`); `find` and `grep` were used. No network downloads attempted.
