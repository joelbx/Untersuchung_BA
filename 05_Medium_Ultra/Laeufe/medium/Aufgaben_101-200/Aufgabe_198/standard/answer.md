Updated the Red Hat OVAL path to use the cached `goval-dictionary` v0.9.5, filter advisories by supported distribution prefixes, and carry package fix states through HTTP and database results. Gost no longer detects Red Hat family CVEs; OVAL supplies those findings.

`go test ./oval ./gost ./detector` passed, as did `git diff --check`.