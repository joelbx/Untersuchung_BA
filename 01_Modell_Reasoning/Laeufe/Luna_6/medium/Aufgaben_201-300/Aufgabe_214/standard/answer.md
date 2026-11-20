Implemented external nmap scanning per server, with native scanning retained as the default. Added scan technique mapping and validation, source port and capability checks, loader activation when `scannerBinPath` is set, and a commented `portscan` example in the discovery template.

**Verification:** `go test ./config ./scanner ./models` passed, and `git diff --check` passed.