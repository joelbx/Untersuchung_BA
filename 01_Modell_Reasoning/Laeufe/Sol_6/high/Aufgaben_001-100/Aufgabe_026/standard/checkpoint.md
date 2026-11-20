# Checkpoint

Task: include all OS-family CVE content sources throughout vulnerability output and change detection, plus NEGLIGIBLE severity handling.

Completed: plural OS-family mapping; source URL and field priority updates; title/summary priority updates; CVSS v3 support for Ubuntu API and other mapped families; severity mapping; detector and reporter change detection; regression tests.

Verification: `GOPROXY=off GOSUMDB=off go test ./models ./detector ./reporter` passed. `git diff --check` passed.
