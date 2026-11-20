Resolved the package lookup issue in `/app`. Debian and Red Hat post-scan processing now use shared process-to-package mapping and package ownership lookups. RPM ownership parsing skips the specified file diagnostics and errors on malformed lines, with a regression test for multiple architectures.

`go test ./scan -count=1` and `git diff --check` passed.