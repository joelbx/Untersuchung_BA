# Checkpoint

- Added Ubuntu 20.04 extended support through 2030-04-01 and Ubuntu 22.04 standard/extended lifecycle dates through 2027-04-01 and 2032-04-01 in `config/os.go`.
- Added lifecycle checks proving both releases are recognized and support is active on 2026-01-01 in `config/os_test.go`.
- Verification: `go test ./config` passed; `git diff --check` passed.
