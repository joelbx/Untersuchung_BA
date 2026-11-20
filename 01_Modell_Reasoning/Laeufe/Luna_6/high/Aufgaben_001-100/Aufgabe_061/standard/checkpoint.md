# Checkpoint

Task: Resolve incorrect package lookup for multiple installed package architectures/versions.

Implemented:
- Added shared `base.pkgPs` to collect process executable and mapped file paths, listener ports, and associate processes through an OS supplied owner lookup.
- Updated Debian and Red Hat `postScan` paths to call `pkgPs` with `getPkgName` and `getOwnerPkgs` respectively.
- Added RPM owner parsing that ignores permission denied, unowned path, and missing file diagnostics; malformed output returns an error. RPM's expected partial-result exit statuses remain usable, while execution errors are returned.
- Red Hat process association now uses the package name from the owner query and avoids failing `FindByFQPN` lookups for duplicate architecture/version records.

Verification: `go test ./scan` passed. `git diff --check` passed. The existing `parseInstalledPackagesLine` contract remains unchanged; ignorable diagnostics are handled in ownership query parsing.
