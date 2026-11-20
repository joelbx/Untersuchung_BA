# Checkpoint

Task: distinguish newly detected and resolved vulnerabilities in diff reports.

Implemented:
- Added `DiffStatus`, `CveIDDiffFormat`, and `CountDiff` to vulnerability models.
- Diff now accepts plus/minus booleans, filters unchanged CVEs, marks additions/removals, and takes package records from the matching scan.
- Report flags `-diff-plus` and `-diff-minus` default to true; display formats show markers and one-line summaries show counts.
- Added focused model and report tests for status serialization, filtering, package provenance, and list rendering.

Validation: `GOPROXY=off GOSUMDB=off go test ./models ./report ./subcmds` passed. `git diff --check` passed.
