# Task checkpoint

Resolve the album image path tracking issue in the checked-out repository. Follow repository guidance, update the album schema/model and scanner flow, and run relevant existing tests. External research is out of scope.

## Progress
- Confirmed there is no `AGENTS.md` guidance and the worktree started clean.
- Found folder scan stats currently retain only `HasImages`, album refresh is centralized in `scanner/refresher.go`, and migrations use `forceFullRescan` to invalidate last scan timestamps.
- Implementation plan: retain detected image names in each folder's stats, expose unique sorted media directories, pass the complete filesystem directory map through changed/deleted processing and album refresh, persist joined image paths on albums, and add a migration that forces a full rescan.
- Implemented the model field, `MediaFiles.Dirs()`, folder image filename collection, album path aggregation, full directory map propagation, and migration `20221019120000`.
- Validation passed: `go test ./model ./scanner ./persistence` and `git diff --check`.
