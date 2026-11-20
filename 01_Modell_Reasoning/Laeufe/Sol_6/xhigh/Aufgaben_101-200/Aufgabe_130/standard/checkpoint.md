# Device enrollment limit fix

Status: Fix implemented. Device trust tests pass. The focused tsh CLI test could not build in this environment.

Changes: Exposed the fake service with a mutex protected device limit switch; preserved the registered device on admin enrollment failure; added a nil-safe CLI outcome format and regression tests.

Verification: `GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test ./lib/devicetrust/enroll ./lib/devicetrust/testenv` passed.

CLI test limitation: The default build lacks `linux/hidraw.h` and `gnu/libc-version.h`; `CGO_ENABLED=0` excludes all files in `lib/system`.
