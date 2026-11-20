Task: distinguish new and resolved vulnerabilities in diff reports.
Status: implementation and targeted verification complete.
Changes: diff plus/minus selection, status field and model helpers, package source by status, CLI flags, report labels, focused tests.
Verification: go test ./report ./models ./subcmds (exit 0); git diff --check (exit 0).
