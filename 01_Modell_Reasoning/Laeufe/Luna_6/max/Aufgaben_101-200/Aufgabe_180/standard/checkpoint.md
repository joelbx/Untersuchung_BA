# Work checkpoint

## Objective
Update OS end-of-life data and Windows cumulative-update mappings in `/app` per the issue, preserving existing mappings and ensuring build-based KB detection compiles and behaves correctly.

## Constraints
- Use local repository code and existing tests only; external research is blocked.
- Do not request downloads or delegate.
- Do not read credentials, private process files, benchmark solutions, or evaluator artifacts.
- Do not change git history, the index baseline, or harness configuration.
- Edit checked-out files and run relevant existing tests.

## Progress
- Confirmed no `AGENTS.md` files were found under the repository parent.
- Worktree was clean at start.
- Located `config/os.go`, `config/os_test.go`, `scanner/windows.go`, and `scanner/windows_test.go`.
- Updated Fedora 37/38/40, SUSE Enterprise 13/14, and macOS 11/12-15 lifecycle data.
- Appended named Windows KB rollup entries in revision order for Windows 10 22H2, Windows 11 22H2/23H2 builds 22621/22631, and Server 2022.
- Updated existing EOL and kernel-version detection expectations to reflect the new data.
- Ran `gofmt` and `git diff --check` successfully.
- `go test ./config ./scanner` passed.
- `go test ./scanner -run '^Test_windows_detectKBsFromKernelVersion$' -count=1` passed.
- `git diff --check` passed; only the four intended source/test files are modified.
- Objective complete.
