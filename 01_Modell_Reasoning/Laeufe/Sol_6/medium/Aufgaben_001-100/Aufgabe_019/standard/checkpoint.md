# Checkpoint

Task: Fix Roles.Check validation and Roles.Equals set equality.
Status: Implemented and verified.
Changes: Roles.Check rejects duplicates while preserving Role.Check invalid-role validation; Roles.Equals compares distinct role sets; added role validation and equality cases to the existing suite.
Verification: GOPROXY=off go test ./lib/utils -check.f RolesTestSuite -count=1 passed; full lib/utils suite has an unrelated expired certificate fixture failure.
