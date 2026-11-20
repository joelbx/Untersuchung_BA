# Checkpoint

- Task: ensure `oval.major("")` returns `""` without changing parsing of non-empty strings.
- Initial inspection: worktree is clean; `oval/util.go` and `oval/util_test.go` are present. No `AGENTS.md` found.
- Reproduced: the new empty-input case in `Test_major` panicked at `oval/util.go:288` before the fix.
- Fix: return `""` immediately for `version == ""`; existing non-empty parsing code is unchanged.
- Verification: `GOPROXY=off GOSUMDB=off go test ./oval -run '^Test_major$' -count=1` passed, and `GOPROXY=off GOSUMDB=off go test ./oval ./report` passed.
- `git diff --check` passed. The diff contains only the early return and regression case.
