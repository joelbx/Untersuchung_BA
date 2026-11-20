Task: Resolve incomplete Ubuntu CVE data by supporting all OS family CVE content types throughout vulnerability fields and change detection.
Status: Complete. Added GetCveContentTypes; updated source URLs, CPE/reference/CWE order, title/summary order, CVSS v3 Ubuntu API handling, NEGLIGIBLE severity, and detector/reporter change detection. Added focused tests for mapping, Ubuntu content, and update detection.
Verification: `GOPROXY=off GOSUMDB=off go test ./models ./reporter ./detector` passed. `git diff --check` passed.
Constraints: Used local code and tests only; did not alter git history, index, or harness configuration.
