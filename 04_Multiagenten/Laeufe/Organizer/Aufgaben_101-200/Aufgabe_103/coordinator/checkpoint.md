# Checkpoint

Task: fix RPM installed package, repoquery, source RPM filename, and update candidate parsing in scanner/redhatbase.go.
Status: complete.
Changes: preserve empty release with positional fields; share epoch/release version formatting; validate source RPM names and accept -src.rpm form; added empty-release and filename tests. Existing CentOS/Amazon update candidate tests pass.
Verification: go test ./scanner -count=1 passed; git diff --check passed.
Constraints: local repository and tests only; no git history, index baseline, or harness changes. No delegation used.
