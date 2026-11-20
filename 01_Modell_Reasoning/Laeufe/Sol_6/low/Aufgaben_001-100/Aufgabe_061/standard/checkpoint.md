Task: Fix process-to-package association for multiple installed architectures/versions.
Status: Completed. Shared pkgPs collects executable and mapped file paths, resolves owners, and associates processes. Debian and Red Hat postScan use it. RPM ownership validates version, release, and architecture; expected RPM diagnostics are skipped and malformed lines error.
Verification: go test ./scan ./models passed; git diff --check passed.
Constraints: Local repository only; git history, index, and harness configuration untouched.
