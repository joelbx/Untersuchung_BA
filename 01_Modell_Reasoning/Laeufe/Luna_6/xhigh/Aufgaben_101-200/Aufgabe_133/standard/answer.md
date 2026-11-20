Implemented the OSS migration fix. It now downgrades the existing `admin` role, marks it with `OSSMigratedV6`, and keeps user assignments and trusted cluster mappings on `admin`. Legacy user creation also assigns `admin`.

The role constructor is in [role.go](/app/lib/services/role.go:200), migration logic in [init.go](/app/lib/auth/init.go:506), and updated migration expectations in [init_test.go](/app/lib/auth/init_test.go:488).

**Tests passed:**

- `go test -p 1 ./lib/auth -run '^TestMigrateOSS$' -count=1`
- `go test -p 1 ./lib/services -run '^(TestRoleParse|TestValidateRole)$' -count=1`
- `go test -p 1 ./tool/tctl/common -count=1`

The tests were rerun serially after an initial parallel run exceeded the container’s process limit.