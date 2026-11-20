Updated the Red Hat-family OVAL path to filter advisories by distribution, carry package fix states into scan results, and use OVAL alone for Red Hat and rebuild package CVE detection. Upgraded the pinned `goval-dictionary` version for `AffectedResolution` support and added focused tests.

Verification: `go test ./oval ./gost ./detector ./models` and `git diff --check` passed offline.