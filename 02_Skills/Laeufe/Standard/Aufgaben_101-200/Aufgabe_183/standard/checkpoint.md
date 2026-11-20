Task: Correct Ubuntu 20.04 extended support end and add Ubuntu 22.04 lifecycle metadata.

Initial findings: Lifecycle lookup is in config/os.go, with tests in config/os_test.go. The repository is initially clean. `rg` is unavailable, so searches use grep.

Resolution: Added Ubuntu 20.04 extended support through 2030-04-01 and Ubuntu 22.04 standard/extended support through 2027-04-01/2032-04-01 in config/os.go. Added lifecycle boundary tests in config/os_test.go.

Checks passed: `GOPROXY=off GOSUMDB=off go test ./config`; `GOPROXY=off GOSUMDB=off go test ./models ./scanner`; `git diff --check`.
