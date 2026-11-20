Updated the repository to use the locally cached goval-dictionary version with `AffectedResolution`. OVAL now restricts advisory IDs by distribution, carries package fix states through detection, and preserves existing package status details. Gost no longer detects CVEs for Red Hat families.

Regression tests were added, and `GOPROXY=off go test -mod=mod ./...` passed after the final edits.