Issue: OSS v6 migration must retain admin role identity for trusted cluster mappings.
Completed: Added NewDowngradedOSSAdminRole with restricted OSS permissions and migration label. Migration retrieves admin, skips labeled roles, and replaces unlabeled admin; migrated users and trusted cluster mappings use admin. Legacy user creation uses admin. Updated migration tests to seed the existing admin role and assert new behavior.
Verification: go test ./lib/auth -run '^TestMigrateOSS$' -count=1 passed; go test ./lib/services ./tool/tctl/common -run '^$' passed; git diff --check passed.
