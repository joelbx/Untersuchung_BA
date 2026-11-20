Task: Fix `Roles.Check` validation and `Roles.Equals` set equality in `/app`.

Findings: Both methods are in `roles.go`. `Check` checked individual roles but did not detect duplicates. `Equals` compared slice lengths and membership, which mishandled duplicate entries.

Changes: `Check` now rejects duplicate roles after validating each role. `Equals` compares distinct-role sets. Added regression cases to `lib/utils/roles_test.go`.

Verification: Focused role suite passed with `GOPROXY=off GOSUMDB=off go test -mod=vendor ./lib/utils -check.f Roles`. Root package build passed with `GOPROXY=off GOSUMDB=off go test -mod=vendor .`. Full `lib/utils` suite had one unrelated failure: `CertsSuite.TestRejectsSelfSignedCertificate` expects an unknown-authority error, but its certificate expired in 2021 and now returns an expiration error.
