Updated CVE reporting to use every content source associated with an OS family. Ubuntu reports now include Ubuntu API links, details, and CVSS v3 severity; `NEGLIGIBLE` maps to the LOW score range. CVE change checks also consider all family sources.

Verification: `GOPROXY=off GOSUMDB=off go test ./models ./detector ./reporter` passed for all three packages, and `git diff --check` passed.