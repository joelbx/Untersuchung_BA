Updated Vuls to use every CVE content source associated with an OS family. Ubuntu reports now include `UbuntuAPI` data in source URLs, vulnerability details, and CVSS v3 scores; CVE change detection also checks it. `NEGLIGIBLE` now maps to the LOW score range.

Added regression tests. `go test ./models ./detector ./reporter` and `git diff --check` pass.