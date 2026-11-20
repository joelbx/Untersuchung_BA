Task: Fix Roles.Check validation and Roles.Equals set semantics.
Status: Complete.
Changes: Roles.Check rejects duplicate roles and preserves Role.Check validation. Roles.Equals compares distinct-role sets, including nil/empty equivalence. Added role suite cases for valid/invalid/duplicate lists and equality symmetry.
Verification: go test -mod=vendor . passed; go test -mod=vendor ./lib/utils -check.f '^RolesTestSuite\.' passed; git diff --check passed. Full go test -mod=vendor ./lib/utils fails in unrelated CertsSuite.TestRejectsSelfSignedCertificate because fixture expired in 2021 under current 2026 date.
