# Checkpoint

Task: fix Roles.Check validation and Roles.Equals set semantics.
Status: implementation and focused role tests complete.
Changes: Roles.Check rejects duplicate roles after validating each role; Roles.Equals compares distinct role sets. Added regression cases in lib/utils/roles_test.go.
Verification: focused role tests pass; root package compiles; git diff --check passes.
Limit: full lib/utils suite fails in CertsSuite.TestRejectsSelfSignedCertificate because its certificate fixture expired in 2021.
