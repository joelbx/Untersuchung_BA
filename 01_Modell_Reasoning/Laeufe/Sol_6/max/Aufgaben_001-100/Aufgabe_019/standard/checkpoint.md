# Checkpoint

Task: fix `Roles.Check` validation and `Roles.Equals` set comparison in `/app`.

Status: complete.

Changes: `Roles.Check` rejects duplicate entries while preserving `Role.Check` validation. `Roles.Equals` compares distinct role sets. Added regression cases for unknown and duplicate roles, empty lists, order independence, and duplicate insensitive equality.

Verification: `GOPROXY=off GOSUMDB=off go test -v ./lib/utils -run '^TestUtils$' -check.f 'RolesTestSuite.*' -count=1` (4 passed); `git diff --check` passed.
