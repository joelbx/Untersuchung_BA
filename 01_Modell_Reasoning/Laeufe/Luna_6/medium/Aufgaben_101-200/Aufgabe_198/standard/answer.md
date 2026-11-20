Implemented the Red Hat OVAL changes.

- Updated `goval-dictionary` to v0.9.5 so OVAL definitions include `AffectedResolution`.
- Filtered distro advisories by supported identifier prefixes; unsupported titles produce no advisory.
- Propagated fix states through HTTP and database OVAL lookups and preserved package status fields when merging.
- Removed Red Hat’s exported gost `DetectCVEs` method and routed Red Hat family CVE detection through OVAL.

Verified with `go test ./oval ./gost ./detector` and `git diff --check`; all passed.