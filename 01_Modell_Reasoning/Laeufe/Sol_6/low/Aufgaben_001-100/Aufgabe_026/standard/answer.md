Updated Vuls to use all CVE content types associated with an OS family. The change covers CVE change detection, source URLs, CPEs, references, CWE IDs, titles, summaries, and CVSS v3 scores. It also maps `NEGLIGIBLE` to the `LOW` score range and rough score while preserving the single-type mapping function.

The existing tests passed offline: `go test ./models ./detector ./reporter`.