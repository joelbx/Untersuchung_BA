Updated CVE source handling so Ubuntu reports include data from both Ubuntu and Ubuntu API. The change also applies all mapped family sources to URLs, field priority, CVSS v3 scores, and change detection, while preserving the existing single-source mapper. `NEGLIGIBLE` now maps to the LOW score range.

Regression tests passed: `go test ./models ./detector ./reporter -count=1`.