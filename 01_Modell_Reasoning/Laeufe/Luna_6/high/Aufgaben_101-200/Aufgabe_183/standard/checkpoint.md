# Checkpoint

Task completed: Ubuntu lifecycle metadata and Ubuntu 22.04 CVE lookup eligibility are updated.

Changes:
- Ubuntu 20.04 extended support ends on 2030-04-01.
- Ubuntu 22.04 standard support ends on 2027-04-01 and extended support ends on 2032-04-01.
- Added Ubuntu 22.04 (`2204`, Jammy) to the Ubuntu CVE lookup allowlist.
- Added regression coverage for lifecycle status and release lookup eligibility.

Verification: `go test ./config ./gost` passed; `git diff --check` passed.
