Task: distinguish new and resolved vulnerabilities in diff reports.
Status: implemented DiffStatus, formatting/counting methods, directional diff filters, package sourcing, CLI flags, and report display prefixes. Added directional regression test. Verified with go test ./models ./report ./subcmds and git diff --check.
