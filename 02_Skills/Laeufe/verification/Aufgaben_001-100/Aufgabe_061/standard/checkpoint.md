# Checkpoint

Task: Fix process-to-package association for multiple RPM architectures/versions and robust ownership parsing.

Changes:
- Shared `base.pkgPs` collects process executable and mapped file paths, port data, and associates owning package names; Debian and Red Hat `postScan` call it.
- Red Hat `getOwnerPkgs` parses RPM ownership output, ignores the three specified file errors, reports malformed/unexpected lines, deduplicates results, and matches installed name/version/release/architecture before association.
- `needsRestarting` uses the same owner lookup to avoid the exact FQPN mismatch.
- Added `TestParseOwnerPkgs` for mixed architectures/releases, duplicate owners, ignorable errors, and malformed output.

Verification: `gofmt -w scan/redhatbase.go scan/redhatbase_test.go && git diff --check && GOPROXY=off GOSUMDB=off go test ./scan -count=1` exited 0; scan package tests passed. The C compiler emitted an upstream sqlite3 warning.

Tooling: `rg` was unavailable (`/bin/bash: rg: command not found`); used local grep/find instead.
