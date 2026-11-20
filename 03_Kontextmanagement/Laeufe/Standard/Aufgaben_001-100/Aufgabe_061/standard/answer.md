Implemented shared `pkgPs` process-to-package mapping for Debian and Red Hat scanners. RPM ownership now matches the scanned package’s version, release, and architecture, skips the three specified file lookup messages, and returns an error for malformed output. Added a regression test covering duplicate rows and architecture and version mismatches.

`go test ./scan -count=1` passed.