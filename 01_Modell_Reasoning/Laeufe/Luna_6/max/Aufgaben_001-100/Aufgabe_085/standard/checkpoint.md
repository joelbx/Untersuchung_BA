# Checkpoint

Task: distinguish newly detected and resolved CVEs in vulnerability diff reports.

Plan: inspect repository instructions and the existing Go vulnerability diff code; implement diff status, configurable plus/minus filtering, formatting, and counts; run relevant existing tests.

Progress: implemented `DiffStatus`, CVE status formatting and counts; changed report diffs to filter additions/removals and source package records from the matching scan; exposed include/exclude controls in report and TUI commands; added status prefixes to report formats. Fixed a syslog map-key fallback found during the first test run. Relevant existing tests now pass.

Constraints: local repository and existing tests only; do not alter git history, index baseline, or harness configuration.
