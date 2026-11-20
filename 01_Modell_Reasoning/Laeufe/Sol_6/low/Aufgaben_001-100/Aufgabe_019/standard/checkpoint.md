# Checkpoint

Task: Fix Roles.Check validation and Roles.Equals set equality.
Status: Implemented and verified.
Changes: Roles.Check rejects duplicates and accepts declared RoleRemoteProxy; Roles.Equals compares distinct role sets; regression coverage added in lib/utils/roles_test.go.
Tests: `go test ./lib/utils -check.f RolesTestSuite` passed. Full `go test ./lib/utils` had one unrelated failure in CertsSuite.TestRejectsSelfSignedCertificate because its fixture expired in 2021.
