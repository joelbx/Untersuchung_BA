# Checkpoint

Task: Fix `tsh device enroll --current-device` when the enrolled device limit is reached.

Completed:
- Exposed `FakeDeviceService` through `testenv.E.Service` and added a synchronized device limit switch.
- Fake enrollment returns an access denied device limit error while registration remains available.
- `Ceremony.RunAdmin` retains the registered device on enrollment errors and labels device limit errors.
- `printEnrollOutcome` prints a fallback message for nil devices.
- Added regression tests for registration, denial, retry after clearing the limit, and nil output.

Verification:
- `go test ./lib/devicetrust/enroll ./lib/devicetrust/testenv` passed.
- `go test ./lib/devicetrust/enroll -run '^TestCeremony_RunAdmin$' -count=1` passed.
- `go test ./lib/devicetrust/authn -count=1` passed.
- `tool/tsh/common` test could not build: system headers `linux/hidraw.h` and `gnu/libc-version.h` are unavailable. With CGO disabled, `lib/system` has no buildable Go files.
