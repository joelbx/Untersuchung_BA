Updated Vuls to use every CVE content source mapped to an OS family. Ubuntu reports now include Ubuntu API details in source URLs, prioritized fields, and CVSS v3 scores. Both change detectors check all family sources, and `NEGLIGIBLE` maps to the LOW score range.

Added regression tests. The full offline suite passed with `GOPROXY=off GOSUMDB=off go test ./...`.