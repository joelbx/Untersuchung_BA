# Checkpoint

Task: support Amazon Linux 2023+ release detection and EOL mappings.

Progress: updated `config/os.go` to normalize Amazon Linux releases 1, 2, 2022, 2023, 2025, 2027, and 2029; dotted releases normalize to 1 and unsupported/empty releases to unknown. Added standard support end dates for 2023, 2025, 2027, and 2029 and regression coverage in `config/os_test.go`.

Verification: `go test ./config` passed; `git diff --check` passed.
