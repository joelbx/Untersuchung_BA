Issue: Fix Roles.Check validation and Roles.Equals set semantics.
Completed: Roles.Check rejects duplicate and unknown roles; Role.Check accepts declared RoleRemoteProxy; Roles.Equals compares distinct-role sets, including nil/empty equivalence. Added role regression cases in lib/utils/roles_test.go.
Verification: go test -mod=vendor ./lib/utils -run TestUtils -check.f RolesTestSuite -count=1 passed. git diff --check passed. Full go test -mod=vendor ./lib/utils -count=1 failed only CertsSuite.TestRejectsSelfSignedCertificate because its fixture expired in 2021 and current date is 2026.
Delegation: none.
