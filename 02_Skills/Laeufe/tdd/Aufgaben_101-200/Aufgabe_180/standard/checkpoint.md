# Checkpoint

Task: update OS EOL data and Windows KB mappings using test-first changes.
Status: complete.

- `rg` was unavailable; used local `find` and `grep`.
- Lifecycle regression test failed on old Fedora, SUSE, and macOS values before implementation.
- Windows rollup regression test failed for all missing KBs before implementation.
- Updated existing exact expectations to reflect the added rollups and Fedora dates.
- `GOPROXY=off GOSUMDB=off go test ./config ./scanner -count=1` passed.
- `GOPROXY=off GOSUMDB=off go test ./...` passed.
- `git diff --check` passed.
