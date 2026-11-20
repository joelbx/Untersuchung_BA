Updated Ubuntu lifecycle data so 20.04 has extended support through April 1, 2030, and 22.04 has standard support through April 1, 2027 and extended support through April 1, 2032. Added 22.04 to the CVE client’s release allowlist so CVE lookup can proceed.

Regression tests failed for the reported gaps before the fixes and passed afterward. The full offline `go test ./...` suite passed.