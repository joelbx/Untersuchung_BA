Task: optional per-server external nmap scanning on the Vuls host.
Completed: configuration model and scan technique mappings; validation of path, techniques, privilege, source port, and capabilities; TOML load flag; external XML scan and native fallback; discover template; focused tests.
Verification: go test ./config ./scanner ./subcmds passed; git diff --check passed.
No git history, index baseline, or harness configuration changes.
