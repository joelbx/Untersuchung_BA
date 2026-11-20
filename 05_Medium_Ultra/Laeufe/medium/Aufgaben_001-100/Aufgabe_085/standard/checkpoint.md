# Checkpoint

Task: distinguish new and resolved CVEs in diff results.
Status: complete.
Implementation: diff accepts plus/minus booleans; additions and removals carry DiffStatus and the relevant scan's package data. Report and TUI flags select statuses, and report displays prefix CVE IDs in diff mode. VulnInfo.CveIDDiffFormat and VulnInfos.CountDiff added.
Verification: GOPROXY=off GOSUMDB=off go test ./models ./report ./subcmds passed; git diff --check passed.
