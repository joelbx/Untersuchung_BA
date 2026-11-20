Updated Vuls to use every CVE content source associated with an OS family. Ubuntu reports now include UbuntuAPI details in source URLs, vulnerability fields, and CVSS v3 scores; change detection also checks that source. `NEGLIGIBLE` severity now maps to the low CVSS range.

Added focused tests. `go test ./models ./reporter ./detector` passed offline, and `git diff --check` passed.