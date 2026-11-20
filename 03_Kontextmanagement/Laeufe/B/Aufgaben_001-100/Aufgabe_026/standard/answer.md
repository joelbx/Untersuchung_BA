Resolved the vulnerability data issue in `/app`. CVE change detection, source URLs, report fields, titles, summaries, and CVSS v3 scores now consider all sources mapped to the OS family. `NEGLIGIBLE` maps to the low CVSS band, and the single-source mapping remains available.

Regression tests passed offline: `go test ./models ./detector ./reporter`.