Task: fix current-device enrollment failure at the device limit.
Status: updated fake service, RunAdmin error return, CLI nil guard, and enrollment regression test. `go test ./lib/devicetrust/enroll ./lib/devicetrust/testenv` passes. CLI package compile blocked by missing linux/hidraw.h and gnu/libc-version.h system headers. `git diff --check` passes.
