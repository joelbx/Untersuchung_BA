# Checkpoint

Task: Preserve OSS access to leaf clusters during Teleport 6 migration by downgrading the existing admin role and assigning users to admin.

Status: Investigating root cause and local tests. `rg` is unavailable in this environment, so repository searches use `grep`/`find`.

Root cause: `migrateOSS` creates `ossuser`, then migrates users and trusted cluster mappings to that name. Existing leaf clusters use implicit admin-to-admin mapping, so a root-issued `ossuser` identity cannot map there. The admin role is already created at startup and is persisted through `UpsertRole`.

Pattern: `NewOSSUserRole` already defines the restricted permissions needed for migrated OSS users; `NewAdminRole` has broader write rules and root login. The role label can mark an in-place downgrade as complete.

Hypothesis: Replacing the existing admin role with the restricted specification, labeled `OSSMigratedV6`, and passing that role to existing user/trusted-cluster migration helpers preserves role-name compatibility. The focused `TestMigrateOSS` test was updated first; `GOPROXY=off GOSUMDB=off go test -mod=vendor ./lib/auth -run '^TestMigrateOSS$' -count=1` failed to compile as expected because `services.NewDowngradedOSSAdminRole` does not exist yet.

Implementation: Added `NewDowngradedOSSAdminRole`, replaced the stored admin role in `migrateOSS`, and changed legacy user creation to assign admin. Updated migration tests to assert role name, limited rules, label, user roles, and trusted cluster mappings. The first implementation compile failed because the `Role` interface lacks `SetMetadata`; changed to access the concrete `RoleV3` metadata returned by the existing constructor. The next test run failed because the minimal `newTestAuthServer` fixture does not create an admin role; the test now creates it as startup does. Focused `TestMigrateOSS` passes after these corrections.

Verification: `GOPROXY=off GOSUMDB=off go test -mod=vendor ./lib/auth -run '^TestMigrateOSS$' -count=1` passed. `GOPROXY=off GOSUMDB=off go test -mod=vendor ./lib/services ./tool/tctl/common` passed. `GOPROXY=off GOSUMDB=off go test -mod=vendor ./lib/auth` passed. `git diff --check` passed.

