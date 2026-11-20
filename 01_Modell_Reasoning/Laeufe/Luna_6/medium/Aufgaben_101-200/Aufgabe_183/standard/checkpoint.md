# Checkpoint

Task completed: Updated Ubuntu lifecycle metadata so 20.04 has extended support through 1 April 2030 and 22.04 has standard support through 1 April 2027 and extended support through 1 April 2032. Added Ubuntu 22.04 (`2204`, Jammy) to Gost's supported release allowlist so CVE data lookup recognizes it.

Coverage added to the existing config EOL tests and Gost supported-release tests. Verification: `go test ./config ./gost` passed; `git diff --check` passed.
