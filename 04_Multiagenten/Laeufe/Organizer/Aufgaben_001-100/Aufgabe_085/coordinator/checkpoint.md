Task: distinguish new and resolved CVEs in diff reports.
Status: implemented DiffStatus, formatting and counts; diff accepts plus/minus booleans, filters by CVE presence, marks statuses, and selects package records from the corresponding scan. Added CLI selection flags and display prefixes. Added regression tests.
Verification: go test ./models ./report ./subcmds passed; git diff --check passed. No delegations used.
