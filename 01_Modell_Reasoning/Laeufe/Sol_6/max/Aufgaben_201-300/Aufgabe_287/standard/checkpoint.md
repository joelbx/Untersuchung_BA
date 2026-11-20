# Checkpoint

Task: Track scanned image file paths on albums, including migration and incremental scans.

Status: Implementation complete; affected package tests pass, including changed and deleted folder refresh coverage.

Findings: `dirStats` currently stores only `HasImages`; `refresher` builds albums before it knows all filesystem directories. Existing migrations use `forceFullRescan(tx)` to reset scan markers.

Implementation: Added `MediaFiles.Dirs()`, album `ImageFiles`, per-directory image names, album path aggregation, migration with forced rescan, and complete filesystem map propagation through changed/deleted directory refreshes. Added tests for directory sorting, image detection, path aggregation, and database persistence across refreshes.

Verification: `GOPROXY=off GOSUMDB=off go test ./model ./scanner ./persistence ./db` passed after final edits. `go test ./...` passed all packages except two existing TagLib tests that expect permission denial on a chmod 0222 fixture; root can read it. The container rejected a switch to an unprivileged user. The fixture's original ownership and mode were restored.

Constraints: Use local code and tests only; do not change git history, index baseline, or harness configuration.
