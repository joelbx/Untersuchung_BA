Amazon Linux 2023 is now recognized in the scanner, routed to the 2023 OVAL advisories, and given ALAS2023 source links. [config/os.go](/app/config/os.go:47) also normalizes the requested releases and adds EOL dates; unknown releases return `found=false`. The correctly spelled extended support method is available, with the existing spelling preserved for compatibility.

Offline tests passed: `GOPROXY=off GOSUMDB=off go test ./config ./models ./oval ./scanner`. `git diff --check` passed. One subagent implemented the scanner and advisory changes; another reviewed the EOL behavior.

The new June 30 EOL dates for 2023, 2025, 2027, and 2029 follow the repository’s convention. The repository contains no authoritative source to independently verify those dates.