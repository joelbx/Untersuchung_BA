Updated Ubuntu lifecycle data: 20.04 has extended support through 1 April 2030, and 22.04 has standard support through 1 April 2027 and extended support through 1 April 2032. I also added 22.04 to the Gost release allowlist so CVE lookup can process it.

Verification passed: `go test ./config ./gost`, `go test ./models`, and `git diff --check`.