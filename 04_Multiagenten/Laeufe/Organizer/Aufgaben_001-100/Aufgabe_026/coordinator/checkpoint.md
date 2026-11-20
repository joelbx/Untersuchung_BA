Task: Fix multi-source CVE content handling for OS families in /app.
Status: complete.
Changes: family-to-sources mapping; use in change detection, URL/data ordering, titles/summaries; CVSS v3 includes Ubuntu API and other family sources; NEGLIGIBLE severity maps to LOW. Focused regression tests added for mapping, Ubuntu content, and both change detectors.
Verification: GOPROXY=off GOSUMDB=off go test ./models ./detector ./reporter passed; git diff --check passed.
Delegation: none.
Constraints observed: local code/tests only; git history, index baseline, harness configuration untouched.
