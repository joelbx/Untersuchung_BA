# Checkpoint

Task: add `-wp-ignore-inactive` configuration and WordPress package filtering.
Workflow: test first, verify failure, implement, run focused and full existing tests.
Tooling: `rg` unavailable (`/bin/bash: rg: command not found`); using `grep`/`find`.

Implementation: registered `-wp-ignore-inactive` for `report`; added `Config.WpIgnoreInactive` with TOML loading; `FillWordPress` filters inactive packages before plugin/theme lookup; `removeInactives` returns nil when empty.
Red: focused tests failed for missing flag, TOML setting, unfiltered packages, and unwanted API paths.
Green: `GOPROXY=off GOSUMDB=off go test ./wordpress ./commands ./config -run 'Test(RemoveInactives|FillWordPressSkips|ReportFlagEnables|TOMLLoaderEnables)' -count=1` passed.
Full suite: `GOPROXY=off GOSUMDB=off go test ./...` passed. Existing go-sqlite3 C compiler warning was emitted; no test failed.
Diff check: `git diff --check` passed.
