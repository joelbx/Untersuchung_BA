I updated RPM ownership parsing so the three specified error lines are ignored, malformed lines return errors, and package resolution compares the full package identity. The required `pkgPs` implementation and Debian/Red Hat `postScan` refactor are still incomplete, so the issue is not fully resolved.

`go test ./scan` was still running when I stopped.