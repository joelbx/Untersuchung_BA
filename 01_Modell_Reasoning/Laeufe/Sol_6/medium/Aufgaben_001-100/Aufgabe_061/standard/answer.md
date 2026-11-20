Implemented the package lookup fix in the checked-out repository. A shared `pkgPs` function maps process files to owning packages; Debian and Red Hat now use it. RPM ownership parsing deduplicates owners across architectures, ignores the three specified file errors, and rejects malformed lines. The needs-restarting lookup also uses package ownership names to avoid the same full-version lookup warning.

`go test ./scan -count=1` and `git diff --check` passed.

The package inventory is still keyed by package name, so it cannot represent two installed versions or architectures of the same name as separate records.