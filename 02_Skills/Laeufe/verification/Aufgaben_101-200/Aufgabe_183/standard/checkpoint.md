# Checkpoint

- Task: correct Ubuntu 20.04 extended support and add Ubuntu 22.04 lifecycle metadata.
- Initial inspection: repository is a Go project; working tree was clean. `rg` is unavailable, so searches will use local `grep`/`find`.
- Changed `config/os.go`: Ubuntu 20.04 extended support ends 2030-04-01; Ubuntu 22.04 standard and extended support end 2027-04-01 and 2032-04-01. Changed `gost/ubuntu.go` to accept Ubuntu 22.04 for CVE lookup.
- Added lifecycle lookup/date/status cases in `config/os_test.go` and a 22.04 allowlist case in `gost/ubuntu_test.go`.
- Verification: `GOTOOLCHAIN=local GOPROXY=off go test ./config ./gost` exited 0; both packages passed. `GOTOOLCHAIN=local GOPROXY=off go test ./models` exited 0. `git diff --check` exited 0.
