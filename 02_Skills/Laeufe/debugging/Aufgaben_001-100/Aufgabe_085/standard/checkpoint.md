# Checkpoint

Task: distinguish new and resolved vulnerabilities in diff reports.

Status: investigation started. `rg` is unavailable in this environment; using local `find` and `grep` for repository inspection.

## Root cause and pattern

`report.diff` calls `getDiffCves`, which iterates only current CVEs. It classifies current-only entries as new but also includes shared CVEs when CVE metadata timestamps change; it never traverses previous-only entries. Package collection always looks in `current.Packages`, so a resolved CVE cannot carry the historical package. The diff call site in `report/report.go` has no plus/minus controls. Text/CSV/TUI displays use raw `CveID`.

Hypothesis: set membership of CVE IDs is the required distinction. Current-only IDs are plus, previous-only IDs are minus; shared IDs are unchanged for this feature regardless of metadata changes. A focused result test will establish that behavior and package provenance.

## Implementation and verification

Added `DiffStatus`, `CveIDDiffFormat`, and `CountDiff` in models. The report diff now takes `plus, minus bool`, includes only current-only and previous-only CVE IDs as requested, labels each included CVE, and builds package entries from the corresponding scan. The report and TUI commands expose `-diff-plus` and `-diff-minus`, both true by default. Diff displays use the signed CVE ID while links retain the plain ID.

Before the fix, `GOPROXY=off GOSUMDB=off go test ./report ./models -run 'TestDiffStatusesAndPackageSources|TestDiffFormattingAndCounts' -count=1` failed to compile because `DiffStatus`, `CountDiff`, and `CveIDDiffFormat` did not exist. After the fix, `GOPROXY=off GOSUMDB=off go test ./models ./report ./subcmds ./config -count=1` passed (the sqlite3 C compilation emitted an existing warning). `git diff --check` passed.
