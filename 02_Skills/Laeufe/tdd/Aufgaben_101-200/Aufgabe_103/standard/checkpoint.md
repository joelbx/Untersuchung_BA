# Checkpoint

Task: fix RPM package, repoquery, source filename, and update candidate parsing in `scanner/redhatbase.go`.

Plan: inspect local code and tests; add regression tests and observe failures; implement minimal fixes; run relevant tests and the project suite.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); using local `grep`/`find` instead.

Result: regression tests initially failed for empty release fields, source `-src.rpm` filenames, malformed filenames, and update listings. The parser now preserves the empty release position, constructs source versions without a trailing hyphen, accepts supported source suffixes, rejects malformed names, and handles Amazon Linux 2 modularity and repoquery lines.

Verification: `go test ./scanner -count=1` passed. `GOPROXY=off GOSUMDB=off go test ./...` passed. `git diff --check` passed. No offline tooling prevented a check.
