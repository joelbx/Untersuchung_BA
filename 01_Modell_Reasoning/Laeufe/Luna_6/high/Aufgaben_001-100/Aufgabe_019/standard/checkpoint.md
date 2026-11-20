# Checkpoint

Implemented the roles fix in `/app`:

- `Roles.Check` rejects duplicate values and still returns nil for empty and valid unique lists.
- `RoleRemoteProxy` is accepted by `Role.Check`, consistent with the declared built-in role.
- `Roles.Equals` compares distinct role sets, so ordering and duplicates do not affect equality, while differing distinct roles do.
- Added coverage for duplicates, empty input, `RoleRemoteProxy`, set equality, differing sets, and nil versus empty.

Verification: `go test ./lib/utils -check.f 'RolesTestSuite'` passes. The full `go test ./lib/utils ./` run is blocked by the existing `CertsSuite.TestRejectsSelfSignedCertificate` fixture, which expired in 2021; the root package compiles successfully.
