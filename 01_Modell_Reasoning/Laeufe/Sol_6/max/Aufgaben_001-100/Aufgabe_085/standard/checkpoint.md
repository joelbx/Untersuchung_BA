# Checkpoint

Task: distinguish newly detected and resolved CVEs in scan diff reports.

Status: implemented plus/minus selection, CVE diff statuses, format/count helpers, and report output labels. Diff package versions now come from the matching scan, with per-CVE overrides when both statuses share a package name. Added regression tests for selection, package provenance, labels, JSON statuses, and model helpers.

Verification: `GOPROXY=off GOSUMDB=off go test ./models ./report ./subcmds` passed; `git diff --check` passed. Final diff reviewed; changes are limited to diff selection, vulnerability models, report formatting, CLI flags, and relevant tests.
