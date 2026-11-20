# Checkpoint

- Task: ensure `oval.major("")` returns `""` while preserving behavior for non-empty input.
- Repository status at start: clean.
- Found: `major("")` sliced with an index of `-1` and panicked.
- Changed: added an early return for empty input and a case in `Test_major`.
- Verified: `GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test ./oval` and `go test ./report` with the same environment both pass. `git diff --check` passes.
