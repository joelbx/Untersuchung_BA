# Checkpoint

- Objective: prefer `artist.*` from the artist folder when resolving artist images; expose each album's media directories and trace lookup durations.
- Status: implemented and verified.
- Changes: album media directories are stored and backfilled for existing databases; artist artwork checks the computed local folder before file, URL, and placeholder fallbacks; artist cache keys track local image changes; trace logs include lookup duration.
- Verification: `GOPROXY=off GOSUMDB=off go test ./model ./core/artwork ./scanner ./persistence ./db ./db/migration` passed. `git diff --check` passed.
- Constraints: local code/tests only; preserve git history, index baseline, and harness configuration.
