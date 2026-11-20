# Checkpoint

Issue: `tsh device enroll --current-device` panicked when enrollment failed after registration at the trusted-device limit.

Changes:
- Exposed `FakeDeviceService` through `testenv.E.Service` and added a mutex-protected device-limit toggle.
- Made fake enrollment return AccessDenied with the device-limit message.
- Preserved `currentDev` and `DeviceRegistered` from `RunAdmin` when enrollment fails.
- Added nil-safe fallback output in `printEnrollOutcome`.
- Added an enrollment regression test covering registration, device-limit failure, error text, and successful retry after disabling the limit.

Checks:
- `GOTOOLCHAIN=local GOPROXY=off go test ./lib/devicetrust/enroll ./lib/devicetrust/testenv` passed.
- `git diff --check` passed.
- `GOTOOLCHAIN=local GOPROXY=off go test ./tool/tsh/common -run '^$'` could not compile dependencies: `github.com/flynn/hid` reported `fatal error: linux/hidraw.h: No such file or directory`; `lib/inventory/metadata` reported `fatal error: gnu/libc-version.h: No such file or directory`. The check was stopped after these errors. CLI package build remains unverified in this environment.

Tooling: `rg` unavailable (`/bin/sh: rg: not found`); used local `grep`/`find`.
