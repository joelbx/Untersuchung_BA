# Checkpoint

Task: restore native OS directory scanning and add `utils.IsDirReadable`.
Status: implementation complete; scanner and utils tests pass.

Changes:
- Scanner traversal, directory stat/open, ignore checks, symlink checks, and audio file listing now use OS paths and operations.
- Traversal normalizes its root to an absolute path; Windows recycle bin skip preserved.
- Added `utils.IsDirReadable` and regression tests.

Verification:
- RED: `GOPROXY=off GOSUMDB=off go test ./scanner -run TestScanner -ginkgo.focus='reads the OS root' -count=1` failed with audio count 0 instead of 6.
- RED: `GOPROXY=off GOSUMDB=off go test ./utils -run TestIsDirReadable -count=1` failed with undefined IsDirReadable.
- RED: `GOPROXY=off GOSUMDB=off go test ./scanner -run TestScanner -ginkgo.focus='reports absolute paths' -count=1` failed because paths were relative.
- GREEN: `GOPROXY=off GOSUMDB=off go test ./scanner ./utils` passed.
- `GOPROXY=off GOSUMDB=off go test ./...` failed in scanner/metadata/taglib: 'correctly parses metadata from all files in folder' (unreadable fixture included), 'Correctly parses m4a (aac) gain tags' (duplicate gain values), and 'correctly handle unreadable file due to insufficient read permission' (no error). These tests and production package were untouched; the environment runs with enough permissions to read the fixture. TagLib also emits a deprecation warning. Remaining uncertainty: full suite remains red due to these unrelated failures.
- `git diff --check` passed.

Tooling: `rg` unavailable (`/bin/bash: rg: command not found`); used local `find` and `grep`.
