# Checkpoint

Task: align OS EOL data and Windows KB mappings, preserving existing entries; verify with relevant local Go tests.

Initial search: `rg --files ...` could not run because `rg` is unavailable (`/bin/bash: rg: command not found`). Using local `find` and `grep` instead.

Updated `config/os.go` with Fedora 37/38/40 cutoffs, SUSE Enterprise Desktop/Server 13/14 cutoffs, and macOS 11/15 status. Extended `scanner/windows.go` rollups for 19045, 22621, 22631, and 20348 using named fields in numeric revision order. Updated existing expected KB lists and added revision-boundary tests.

Verification in progress: `GOTOOLCHAIN=local GOPROXY=off go test ./config ./scanner` and targeted scanner test. `git diff --check` passed. The first Go test run is compiling the dependency tree.

Verification complete:
- `GOTOOLCHAIN=local GOPROXY=off go test ./config ./scanner` passed (`config` and `scanner`).
- `GOTOOLCHAIN=local GOPROXY=off go build ./...` passed.
- `git diff --check` passed; `gofmt -l` reported no files.

A duplicate targeted scanner test command was stopped during dependency compilation; the completed full scanner test run included that targeted test.
