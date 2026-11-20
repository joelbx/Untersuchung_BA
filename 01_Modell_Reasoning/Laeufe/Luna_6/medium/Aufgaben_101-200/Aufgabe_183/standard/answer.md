Updated Ubuntu lifecycle data: 20.04 extended support now ends on 1 April 2030; 22.04 has standard support through 1 April 2027 and extended support through 1 April 2032. Added 22.04 (Jammy) to Gost’s supported releases so CVE lookup recognizes it.

Added coverage in the existing config and Gost tests. `go test ./config ./gost` and `git diff --check` passed.