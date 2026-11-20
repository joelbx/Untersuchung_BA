# Checkpoint

Implemented `-wp-ignore-inactive` on the report command, where WordPress vulnerability API calls occur. Added `Config.WpIgnoreInactive` and TOML loading that preserves the CLI flag. `FillWordPress` filters inactive packages before theme/plugin lookups, and the existing report result filter honors the global setting. `removeInactives` returns nil when no packages remain.

Verification: `GOPROXY=off GOSUMDB=off go test ./wordpress ./commands ./config ./models ./report` passed. The dependency `github.com/mattn/go-sqlite3` emitted an existing C compiler warning during the run. `git diff --check` passed.

Initial `rg` search was unavailable (`/bin/bash: rg: command not found`); local grep was used. An initial test run was interrupted before completion to rerun with network access disabled. No checks remain blocked.
