# Checkpoint

Task: Restore legacy `listenPorts` report compatibility and move scan port details to `ListenPortStats`.
Status: Complete. Models accept string ports and earlier structured ports; scan collectors, destination selection, reachability updates, and report views use the new fields. Relevant tests passed: `GOPROXY=off go test -p 1 ./models ./scan ./report`.
Constraints: Edited checked-out files only; no git history, index baseline, or harness configuration changes. No external research or downloads.
