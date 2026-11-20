Implemented the role handling fix in [roles.go](/app/roles.go) and added coverage in [roles_test.go](/app/lib/utils/roles_test.go).

`Roles.Check` now rejects duplicates, and `Roles.Equals` compares distinct role sets regardless of order or repeated entries. `RoleRemoteProxy` is accepted as a valid built-in role.

The role suite passes: `go test ./lib/utils -check.f 'RolesTestSuite'`. The broader run hit an unrelated certificate test failure because its fixture expired in 2021; the root package compiled successfully.