# OSS admin migration checkpoint

Implemented migration that retrieves the existing admin role, skips when marked with `OSSMigratedV6`, replaces it with a downgraded admin role, and maps existing users/trusted clusters to admin. Legacy `tctl users add` now assigns admin.

TDD red: `GOPROXY=off GOSUMDB=off go test ./lib/auth -run '^TestMigrateOSS$' -count=1` failed in EmptyCluster (missing migration label), User (ossuser assigned), and TrustedCluster (ossuser mapping).

TDD green: same command passed after implementation.

Affected package check: `GOPROXY=off GOSUMDB=off go test ./lib/services ./tool/tctl/common` passed.

Project suite: `GOPROXY=off GOSUMDB=off go test ./...` exited 1. Failures:
- `integration`: timed out after 10m; exact hung test is uncertain from the timeout report.
- `lib/cgroup`: `Suite.TestCleanup` and `Suite.TestCreate` failed mounting cgroup with `operation not permitted`.
- `lib/srv/regular`: `SrvSuite.TestProxyReverseTunnel` failed waiting for heartbeat announce.
- `lib/utils`: `CertsSuite.TestRejectsSelfSignedCertificate` expected unknown authority, but fixture expired on 2021-03-16 and current time is 2026-10-28.

`lib/auth` passed in the project suite. No dependency downloads were requested.
