Updated CVE source handling so Ubuntu reports include both Ubuntu and Ubuntu API data. Source URLs, report fields, CVSS v3 scores, and change detection now account for the relevant family sources. `NEGLIGIBLE` is mapped to the low severity range and rough score.

Added regression tests. `go test ./models ./detector ./reporter` passed.