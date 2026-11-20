Implemented the process-to-package lookup fix in `/app`. Debian and Red Hat `postScan` now use a shared `pkgPs` function that collects process file paths, looks up their owners, and associates each process once per package. Red Hat ownership lookup matches by package name, avoiding spurious warnings when RPM reports another installed architecture or version.

RPM ownership parsing now ignores lines ending in “Permission denied,” “is not owned by any package,” or “No such file or directory,” and returns an error for malformed lines. A regression test covers mixed versions and architectures.

Verification passed: `go test ./scan -count=1` and `git diff --check`.