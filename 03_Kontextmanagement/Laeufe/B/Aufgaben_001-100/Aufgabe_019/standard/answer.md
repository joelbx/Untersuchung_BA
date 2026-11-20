Updated [roles.go](/app/roles.go) so `Check` rejects duplicate roles and `Equals` compares distinct-role sets, including nil and empty lists. Added regression cases to [roles_test.go](/app/lib/utils/roles_test.go).

The targeted role tests pass. The full `lib/utils` suite has one unrelated failure caused by a certificate fixture that expired in 2021.