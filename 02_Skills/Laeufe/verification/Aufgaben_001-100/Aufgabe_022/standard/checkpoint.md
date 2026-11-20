# Checkpoint

Task: Fix RPM installed-package parsing for non-standard source filenames and epoch-bearing source filenames.

Changes: Both installed-package parsing paths append a warning and retain the binary package when `SOURCERPM` cannot be parsed. `splitFileName` moves a numeric filename epoch into the parsed version, leaving the source name clean. Tests cover the affected line parsers and scan continuation with a valid later package.

Verification: `gofmt -w scanner/redhatbase.go scanner/redhatbase_test.go && git diff --check && GOPROXY=off GOSUMDB=off go test ./scanner -count=1` exited 0; output: `ok github.com/future-architect/vuls/scanner 0.090s`. Focused installed-package tests also exited 0.

Tooling: `rg` unavailable (`/bin/bash: rg: command not found`); used local grep. No downloads requested.
