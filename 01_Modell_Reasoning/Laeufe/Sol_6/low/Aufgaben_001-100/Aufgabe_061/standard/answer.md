Updated the Debian and Red Hat scanners to use a shared `pkgPs` function that maps running processes to packages through their loaded files. Red Hat ownership lookup now matches the installed package’s version, release, and architecture, skips expected RPM diagnostics, and returns an error for malformed lines.

`go test ./scan ./models` passed, and `git diff --check` is clean.