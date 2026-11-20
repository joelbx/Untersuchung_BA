Updated [roles.go](/app/roles.go) so `Check` rejects unknown and duplicate roles, and `Equals` compares distinct role sets regardless of order or repeated entries. Added regression cases in [roles_test.go](/app/lib/utils/roles_test.go).

The focused role tests pass. The full `lib/utils` suite has one unrelated failure: a certificate fixture expired in 2021.