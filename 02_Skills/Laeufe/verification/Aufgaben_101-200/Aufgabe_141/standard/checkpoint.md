# Checkpoint

- Task: add `-wp-ignore-inactive` configuration and filter inactive WordPress plugins and themes during vulnerability lookup.
- Initial search: `rg` is unavailable (`/bin/bash: rg: command not found`); using local `grep` and `find`.
- Added the flag to scan, report, server, and tui commands; added `WpIgnoreInactive` to the config schema and TOML loading; filtered inactive packages before WordPress vulnerability requests and when collecting scan results.
- Verification: `GOPROXY=off GOSUMDB=off go test ./wordpress ./config ./commands ./scan ./report` exited 0. `git diff --check` exited 0. The C compiler emitted a pre-existing warning in the sqlite3 dependency.
