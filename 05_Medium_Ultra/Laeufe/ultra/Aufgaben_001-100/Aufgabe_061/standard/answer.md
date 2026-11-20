Implemented shared process to package association in [base.go](/app/scan/base.go). Debian and Red Hat `postScan` now use their package ownership lookups. Red Hat also uses that lookup for `needsRestarting`, removing the `FindByFQPN` warning path. RPM query parsing ignores the three specified diagnostics and returns an error for malformed lines.

Delegated the Red Hat lookup and regression tests, then integrated and verified the patch. `GOPROXY=off GOSUMDB=off go test ./scan ./models` and `git diff --check` passed.

The package map retains one entry per name. Processes owned by another installed version or architecture are associated with that retained entry; the model cannot distinguish every installed variant.