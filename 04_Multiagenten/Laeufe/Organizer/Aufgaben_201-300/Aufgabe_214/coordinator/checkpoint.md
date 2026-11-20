Task: add per-server external nmap port scanning with configuration validation and preserve native fallback.
State: inspected repository layout; implementation pending. Working solo; no delegation.
Constraints: local code/tests only, no downloads, no git history/index/harness changes.
Implemented PortScanConf, server TOML wiring, validation, native/external dispatch, nmap grepable output parsing, and focused tests. Running package tests; check completion before final.
Final verification: GOTOOLCHAIN=local GOPROXY=off go test ./config ./scanner ./subcmds passed; git diff --check passed. No delegation used.
