Implemented per-server external nmap scanning. A configured `scannerBinPath` enables it; servers without one continue using the native scanner. The change adds technique, privilege, capability, and source-port validation, plus a commented `portscan` example in the discovery template.

`GOPROXY=off go test ./config ./scanner ./subcmds` and `git diff --check` pass.