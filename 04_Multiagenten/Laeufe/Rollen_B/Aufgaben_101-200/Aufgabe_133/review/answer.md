VERDICT: FIX

**Code defect:** [migrateOSS](/app/lib/auth/init.go:518) labels `admin` as migrated before updating users, trusted clusters, and GitHub connectors. If a later update fails, the next startup sees that label and skips the unfinished migration. Move the admin role update and completion label after the resource updates, and make interrupted trusted cluster CA updates retryable.

**Tests:** All executed successfully. They do not cover the interrupted migration path.

- `GOPROXY=off GOSUMDB=off go test ./lib/auth -run '^TestMigrateOSS$' -count=1` — passed
- `GOPROXY=off GOSUMDB=off go test ./lib/services -run '^TestCheckAccessToRemoteCluster$' -count=1` — passed
- `GOPROXY=off GOSUMDB=off go test ./tool/tctl/common -count=1` — passed

**TEST_ENVIRONMENT_PROBLEM:** None.