Task: Repair Red Hat family OVAL advisory filtering and package fix-state handling; remove Gost Red Hat CVE detection.
Status: Implemented and verified. Updated cached goval-dictionary dependency to v0.9.5; OVAL resolution states flow through HTTP/DB and package statuses; unsupported advisory titles are excluded; Gost returns Pseudo for Red Hat family and RedHat.DetectCVEs was removed.
Tests: GOPROXY=off GOSUMDB=off go test ./oval ./gost ./detector (passed). git diff --check (passed).
Constraints observed: local repository and existing tests only; no git history/index/harness changes.
