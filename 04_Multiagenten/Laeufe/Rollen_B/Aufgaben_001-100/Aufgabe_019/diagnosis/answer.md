I found the faults in [roles.go](/app/roles.go:106):

- `Roles.Check` calls `Role.Check` for each entry, so unknown values already return an error, but it never detects duplicates.
- `Roles.Equals` compares list lengths and then checks membership in only one direction. `{Auth, Auth}` therefore compares equal to `{Auth, Admin}`, while `{Auth}` compares unequal to `{Auth, Auth}`.

The existing [roles tests](/app/lib/utils/roles_test.go:43) cover an unknown value and ordinary equality, but lack duplicate and nil-versus-empty cases. A fix should validate uniqueness in `Check` and compare distinct-role sets in `Equals`. One open question is whether `RoleRemoteProxy`, which is declared but rejected by `Role.Check`, is intended to be valid.

**No source or test files were changed.** This run was restricted to fault localization, so the issue remains unresolved in the checkout.