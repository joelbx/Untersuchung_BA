Task: Fix Roles.Check validation and Roles.Equals set equality.
Status: Implemented and verified with the existing RolesTestSuite.
Changes: Roles.Check rejects unknown and duplicate roles; Roles.Equals compares distinct role sets. Added regression cases in lib/utils/roles_test.go.
Tests: go test ./lib/utils -check.f RolesTestSuite passed. go test ./lib/utils fails in CertsSuite.TestRejectsSelfSignedCertificate because its fixture expired in 2021 relative to the current 2026 date.
