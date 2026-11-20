# Checkpoint

- Objective: restore report compatibility with pre-v0.13.0 string `listenPorts` results while retaining structured port data for scanning.
- Initial state: working tree clean; no repository `AGENTS.md` found.
- Completed: `AffectedProcess` reads legacy string ports and previous structured port objects; new scans store `ListenPortStats []PortStat`.
- Completed: destination selection, reachability updates, and report views now use the appropriate fields. Added parser and compatibility coverage.
- Verification: `GOPROXY=off GOSUMDB=off go test ./models ./scan ./report` passed; `git diff --check` passed.
