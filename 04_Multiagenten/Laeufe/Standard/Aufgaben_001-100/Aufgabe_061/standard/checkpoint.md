Task: Fix process-to-package association when multiple package architectures or versions are installed.
Plan: Inspect current scanner and ownership parsing code, implement path-based mapping, update relevant tests, and run existing Go tests.
Status: Shared pkgPs implemented and both postScan paths refactored. RPM owner parsing now tolerates expected file errors and rejects malformed output. Regression test added. `go test ./scan -count=1` and `git diff --check` pass.
