Resolved the Red Hat OVAL issue in the checked-out files. The analyser now accepts only supported advisory IDs, carries package fix states through HTTP and database lookups, and uses OVAL alone for Red Hat based package CVE detection. I also updated `goval-dictionary` to v0.9.5 and removed `RedHat.DetectCVEs`.

Verification passed: `go test ./oval ./gost ./detector` and `git diff --check`.