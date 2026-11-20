Updated [roles.go](/app/roles.go) so `Check` rejects duplicate roles and `Equals` compares distinct role sets, including nil and empty lists. Added cases to the existing [role tests](/app/lib/utils/roles_test.go).

The role test suite passes. The full `lib/utils` suite has one unrelated failure because a certificate fixture expired in 2021.