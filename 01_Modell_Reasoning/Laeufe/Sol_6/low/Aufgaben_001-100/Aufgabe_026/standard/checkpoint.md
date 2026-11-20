Task: Complete family-specific CVE source handling across vulnerability data retrieval and change detection.
Status: implemented and verified. Offline existing tests passed: go test ./models ./detector ./reporter. git diff --check passed.
Constraints: local code/tests only; preserve git history, index, and harness configuration.
