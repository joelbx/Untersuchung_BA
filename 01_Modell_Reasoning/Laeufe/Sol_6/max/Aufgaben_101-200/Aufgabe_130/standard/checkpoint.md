# Device enrollment limit fix

Status: implementation and regression tests complete. `go test ./lib/devicetrust/enroll ./lib/devicetrust/testenv -count=1` passes with local modules. The CLI package test cannot run here: the CGO build lacks linux/hidraw.h and gnu/libc-version.h, while disabling CGO excludes all files in lib/system. `git diff --check` and gofmt validation pass.

Changes: the fake service exposes a synchronized device limit switch; the test environment exposes the service; RunAdmin returns the registered device on enrollment error; CLI outcome printing handles a missing device. Regression tests cover registration at the limit, retry after clearing it, and the CLI fallback format.
