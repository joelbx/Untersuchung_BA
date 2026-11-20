# Checkpoint

Implemented canonical EOL dates and OS identifiers in config/os.go, shared major parsing, per-target scan EOL warnings, Amazon release handling, and ordered warning rendering in scan summaries. Added focused date, boundary, normalization, and output tests. Verified with `GOPROXY=off GOSUMDB=off go test ./config ./util ./scan ./report ./oval ./gost` (all pass) and `git diff --check` (clean).
