# Checkpoint

Task: add per-server external nmap port scanning with configuration validation and preserve native scanning.
Status: implementation complete; relevant package tests pass.
Changed: config/portscan.go, config/config.go, config/tomlloader.go, scanner/portscan.go, scanner/base.go, subcmds/discover.go; focused tests added.
