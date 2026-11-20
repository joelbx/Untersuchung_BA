Implemented shared `pkgPs` process ownership lookup and wired it into Debian and Red Hat `postScan`. RPM parsing now ignores permission, unowned, and missing-file lines while returning an error for malformed lines.

**Verified:** `go test ./scan -count=1` passes.

The package map stores one version per name, so ownership records for other installed versions or architectures are skipped rather than attributed to the wrong package.