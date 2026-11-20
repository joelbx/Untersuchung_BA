# Port scanner implementation checkpoint

Implemented per-server `PortScanConf` TOML configuration, case-insensitive scan technique mapping, validation (binary path, technique count/support, privilege rules, source port and local capabilities), and loader activation of external scanning when a binary path is supplied. Added nmap invocation with requested port/host list and parsing of grepable output, retaining native `net.DialTimeout` scanning when external mode is off. Added the commented discovery template section.

Validation run: `go test ./config ./scanner ./models` passed after resolving the package-level `exec` naming collision; the final scanner/config rerun also passed. `git diff --check` passed.
