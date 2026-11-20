Task: Resolve Red Hat OVAL advisory and fix-state integration.
Status: implemented and verified.
Changes: upgraded cached goval-dictionary to v0.9.5; validated advisory IDs; propagated OVAL package fix states through HTTP and database collection; removed Gost Red Hat CVE detection; added focused tests.
Verification: GOPROXY=off GOSUMDB=off go test ./oval ./gost ./detector; git diff --check (pass).
