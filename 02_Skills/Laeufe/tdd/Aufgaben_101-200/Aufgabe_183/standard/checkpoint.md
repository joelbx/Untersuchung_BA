# Checkpoint

Task: correct Ubuntu 20.04 extended support and recognize Ubuntu 22.04 in lifecycle and CVE processing.

Completed: added lifecycle regression coverage in `config/os_test.go`, observed expected failures for missing Ubuntu 20.04 extended support and Ubuntu 22.04 lifecycle metadata, and updated `config/os.go` with the requested dates. Added Ubuntu 22.04 to the Gost Ubuntu release allowlist after observing its support test fail; CVE lookup now proceeds for 22.04.

Verification:
- `GOPROXY=off GOSUMDB=off go test ./config -run TestUbuntuLTSLifecycle -count=1`: failed before the fix for expected reasons; passed after the fix.
- `GOPROXY=off GOSUMDB=off go test ./gost -run 'TestUbuntu_Supported/22.04' -count=1`: failed before the fix for expected reason; passed after the fix.
- `GOPROXY=off GOSUMDB=off go test ./...`: passed after all changes.
- `git diff --check` and `gofmt -l config/os.go config/os_test.go gost/ubuntu.go gost/ubuntu_test.go`: passed.

`rg` was unavailable (`/bin/bash: rg: command not found`); local fallback searches succeeded. No remaining check uncertainty.
