# Checkpoint

Task: distinguish newly detected and resolved vulnerabilities in diff reports.
Status: implementation complete.

Changes: added DiffStatus, CveIDDiffFormat, CountDiff; diff filters by plus/minus, marks CVEs, and sources packages from the matching scan. Report and TUI commands accept --diff-plus and --diff-minus; plain --diff includes both. Displayed CVE IDs use status prefixes in list, full text, CSV, Slack, Telegram, and TUI summary.

TDD: regression tests were run before implementation and failed for the missing API. The no-previous-scan test was run before its fix and failed on the missing plus status.

Checks: `GOPROXY=off go test ./report ./models -count=1` passed. `GOPROXY=off go test ./...` passed. Both emitted a compiler warning from github.com/mattn/go-sqlite3 (`sqlite3-binding.c:128049: warning: function may return address of local variable`). `git diff --check` passed.

Tooling: `rg` unavailable (`/bin/bash: rg: command not found`); used `find` and `grep`.
