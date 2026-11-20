Implemented the device limit handling fix.

- Exposed `FakeDeviceService` through `testenv.E.Service` and added a synchronized limit toggle that returns the required `AccessDenied` message.
- Preserved the current device when `RunAdmin` returns an enrollment error, and added a nil-safe fallback in `printEnrollOutcome`.
- Added enrollment coverage confirming registration persists while enrollment is denied and the device remains unenrolled.

**Verification:** `go test ./lib/devicetrust/enroll ./lib/devicetrust/testenv` passes, and `git diff --check` passes. `tool/tsh/common` could not build because this container lacks required Linux headers and its SQLite C dependency fails to compile.