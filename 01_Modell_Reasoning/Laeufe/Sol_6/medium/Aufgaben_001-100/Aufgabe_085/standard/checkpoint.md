# Checkpoint
Task: distinguish new and resolved vulnerabilities in diff reports.
Status: implemented plus/minus filtering, statuses, package provenance, display formatting, and CLI controls.
Verification: go test ./models ./report ./subcmds passed; git diff --check passed.
