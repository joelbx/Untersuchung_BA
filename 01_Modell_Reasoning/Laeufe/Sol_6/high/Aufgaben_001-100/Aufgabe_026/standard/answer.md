Updated Vuls to use every CVE content source mapped to an OS family. Ubuntu reports now include Ubuntu API URLs and details in source ordering and CVSS v3 scoring. Change detection checks those additional sources, and `NEGLIGIBLE` maps to the low score range. The single-source mapping remains available.

The new mapping is in [models/cvecontents.go](/app/models/cvecontents.go); report scoring and presentation changes are in [models/vulninfos.go](/app/models/vulninfos.go).

Verification passed: `go test ./models ./detector ./reporter` with network fetching disabled, plus `git diff --check`.