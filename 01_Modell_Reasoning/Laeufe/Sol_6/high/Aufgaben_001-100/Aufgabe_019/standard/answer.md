Updated [roles.go](/app/roles.go) so `Check` rejects unknown and duplicate roles, while `Equals` compares distinct role sets regardless of order or duplicates. Added regression coverage in [roles_test.go](/app/lib/utils/roles_test.go).

The focused role tests pass. The full `lib/utils` suite has one unrelated failure: a certificate fixture expired in 2021.