# Checkpoint

Task: use one local site in the reverse tunnel server and reuse the proxy access point.
Status: implementation complete; repository-wide tests are running.

TDD red checks:
- `GOPROXY=off GOSUMDB=off go test ./lib/reversetunnel -run '^TestLocalSiteReusesServerAccessPoint$' -count=1` failed as expected: local site's access point was a different object.
- `GOPROXY=off GOSUMDB=off go test ./lib/reversetunnel -run '^TestUpsertServiceConnRejectsWrongLocalCluster$' -count=1` failed as expected: mismatch error omitted tunnel type.

Green checks:
- `GOPROXY=off GOSUMDB=off go test ./lib/reversetunnel -run '^(TestLocalSiteReusesServerAccessPoint|TestUpsertServiceConnRejectsWrongLocalCluster|TestLocalSiteOverlap)$' -count=1` passed.
- `GOPROXY=off GOSUMDB=off go test ./lib/reversetunnel -count=1` passed.

`rg` is unavailable (`/bin/bash: rg: command not found`); used `grep` and `find`.
- `GOPROXY=off GOSUMDB=off go test ./lib/reversetunnel/... -count=1` passed (reversetunnel and track).

Repository-wide check: `GOPROXY=off GOSUMDB=off go test ./...` was started but interrupted after several minutes without a completed result. It exited 1 with `go build github.com/gravitational/teleport/lib/srv/db: /usr/local/go/pkg/tool/linux_amd64/compile: signal: interrupt` and `FAIL github.com/gravitational/teleport/integration [build failed]` (also multiple linker/vet interrupts). This is an interrupted build, not evidence of a test failure. The rest of the repository suite remains unverified.
