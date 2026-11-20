Implemented the Red Hat OVAL changes.

- Upgraded goval-dictionary to `v0.9.5` for `AffectedResolution` support. Advisories are now added only when their IDs match the supported family prefixes. ([go.mod](/app/go.mod:53), [redhat.go](/app/oval/redhat.go:158))
- Propagated fix states through HTTP and DB lookups, including `NotFixedYet` and `FixedIn`. “Will not fix” and “Under investigation” are treated as unaffected; other resolution states remain affected. ([util.go](/app/oval/util.go:372))
- Red Hat, CentOS, Rocky, and Alma now bypass Gost CVE detection, and `RedHat.DetectCVEs` was removed. ([gost.go](/app/gost/gost.go:58))

Verification passed with downloads disabled: `go test ./oval ./gost ./scanner` and `go test ./detector`.