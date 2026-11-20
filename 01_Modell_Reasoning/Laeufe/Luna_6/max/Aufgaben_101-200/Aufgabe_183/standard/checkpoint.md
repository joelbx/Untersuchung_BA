# Checkpoint

Task: Fix Ubuntu lifecycle metadata so Ubuntu 20.04 has extended support through 2030-04-01 and Ubuntu 22.04 is recognized with standard support through 2027-04-01 and extended support through 2032-04-01.

Completed changes:
- Added the 20.04 and 22.04 lifecycle dates in `config/os.go` with regression coverage in `config/os_test.go`.
- Added Ubuntu 22.04 (`2204`/`jammy`) to the GOST release allowlist and its existing support test.
- Allowed Ubuntu 22 releases through the OVAL handler using its generic `linux` kernel definition so package vulnerability lookup can proceed.

Validation: `gofmt` completed; `go test ./config ./gost ./oval` passed; `git diff --check` passed.

Constraints observed: Used local repository code and tests only. No `AGENTS.md` files were found. No git history, index baseline, or harness configuration changes were made.
