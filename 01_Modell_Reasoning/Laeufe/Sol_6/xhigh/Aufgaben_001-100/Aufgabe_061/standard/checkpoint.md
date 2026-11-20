# Checkpoint

Task: Fix process package ownership lookup with multiple installed RPM versions and architectures.
Status: Complete. Shared pkgPs collects executable and mapped paths, resolves owners through Debian/RPM callbacks, and attaches processes only to the matching installed version and architecture. RPM query parsing ignores permission, unowned, and missing-file lines and errors on malformed lines. Tests: GOPROXY=off GOSUMDB=off go test ./scan -count=1 (passed); git diff --check (passed).
