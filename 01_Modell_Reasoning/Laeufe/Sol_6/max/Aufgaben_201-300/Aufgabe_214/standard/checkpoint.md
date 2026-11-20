# Port scanner support checkpoint

- Goal: add per-server external `nmap` scanning while retaining the native scanner.
- Status: complete. Added per-server TOML configuration, scan technique and capability validation, external `nmap` execution, native fallback, XML result correlation, and the discover template example.
- Verification: `GOPROXY=off GOSUMDB=off go test ./config ./scanner ./subcmds` and `git diff --check` passed. Scanner tests use a local fake executable because `nmap` is not installed in this workspace.
