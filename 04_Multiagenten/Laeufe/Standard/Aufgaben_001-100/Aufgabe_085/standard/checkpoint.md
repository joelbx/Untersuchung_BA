Task: distinguish newly detected (+) and resolved (-) CVEs in diff reports.
Implemented: DiffStatus model field and helpers; directional CVE comparison; plus/minus filtering; package sourcing by scan; report CLI flags, visible status formatting, and tests.
Verification: go test ./models ./report ./subcmds passed; git diff --check passed.
