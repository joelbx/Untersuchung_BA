I located the failure, but this run was restricted to fault localization, so I did not edit project source or tests.

- [oval/redhat.go](/app/oval/redhat.go:123) appends every converted advisory; `convertToDistroAdvisory` never rejects unsupported identifiers. `update` also loses `FixState` when merging package statuses.
- [oval/util.go](/app/oval/util.go:39) has no fix-state field in `fixStat`. Both HTTP and database collection omit it, and `isOvalDefAffected` returns an unfixed package without examining `AffectedResolution`. The database source-package path also hardcodes `notFixedYet: false`.
- [gost/gost.go](/app/gost/gost.go:59) still selects the Red Hat Gost client, whose [DetectCVEs](/app/gost/redhat.go:25) adds unfixed CVEs after OVAL processing.

[PackageFixStatus](/app/models/vulninfos.go:250) already supports `FixState`, so the missing path is OVAL extraction and propagation. The fix should verify family-specific advisory prefixes, repository and modularity matching, installed-version checks, and each stated resolution. I did not run tests; the exact `AffectedResolution` shape in the newer dependency remains unverified.