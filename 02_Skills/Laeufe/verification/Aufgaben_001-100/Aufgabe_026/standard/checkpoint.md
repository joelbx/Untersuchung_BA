# Checkpoint

Task: include all OS-family CVE content sources throughout vulnerability reporting, and map NEGLIGIBLE severity to LOW.

Changes: added `GetCveContentTypes` for OS-family source mappings; applied it to CVE change checks in detector and reporter, source URLs, CPEs, references, CWEs, titles, and summaries. Included Ubuntu API in CVSS v3 retrieval and mapped NEGLIGIBLE to the LOW score and range. Added regression tests for mappings, ordering, URLs, scores, and change detection.

Verification (fresh after final edits): `GOPROXY=off GOSUMDB=off go test ./models ./detector ./reporter` exited 0; all three packages reported `ok`. `git diff --check` exited 0. Initial `rg` lookup was unavailable (`/bin/bash: rg: command not found`), so local searches used `grep` and `find`. An initial unqualified `go test` was stopped before any result; the completed verification explicitly disabled dependency fetching.
