Implemented the device limit handling and reporting fix.

- `FakeDeviceService` now exposes `SetDevicesLimitReached`, and `testenv.E` exposes its service.
- When the limit is enabled, enrollment returns the requested AccessDenied message. `RunAdmin` preserves the registered device and `DeviceRegistered` outcome when enrollment fails.
- `printEnrollOutcome` handles a nil device without panicking.
- Added a ceremony test for registration followed by device limit rejection.

`go test ./lib/devicetrust/enroll ./lib/devicetrust/testenv` passed. The `tool/tsh/common` tests could not run in this environment: with cgo enabled, required Linux headers are missing; with cgo disabled, build constraints exclude all files in `lib/system`. `git diff --check` passed.