# Checkpoint

Task: fix RPM installed package, repoquery, source filename, and update candidate parsing in `scanner/redhatbase.go`.

Initial state: working tree clean. `rg` is unavailable (`/bin/bash: rg: command not found`); using `grep` for local searches.

Changes: preserve literal spaces in RPM query columns; share epoch/version/release formatting for source packages; accept and validate hyphen-delimited source RPM architecture; handle `(none)` update epochs. Added regression cases for empty releases, filename variants, and update epochs.

Checks: `gofmt -w scanner/redhatbase.go scanner/redhatbase_test.go` and `git diff --check` completed. Targeted scanner tests passed: `GOTOOLCHAIN=local GOPROXY=off go test ./scanner -run 'Test_redhatBase_parseInstalledPackages|TestEmptyReleaseRPMQueries|TestSplitFileNameVariants|TestParseYumCheckUpdate' -count=1`. The first full scanner run found a tab-delimited RPM fixture; after adding tab support, `GOTOOLCHAIN=local GOPROXY=off go test ./scanner -count=1` passed.
