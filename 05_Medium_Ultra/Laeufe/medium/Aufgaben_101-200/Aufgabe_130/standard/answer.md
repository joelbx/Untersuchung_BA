Fixed the `tsh device enroll --current-device` panic. When registration succeeds but enrollment hits the device limit, `RunAdmin` now returns the registered device and `DeviceRegistered` outcome with the error. The CLI printer also handles a nil device without crashing.

The fake service exposes `SetDevicesLimitReached`, and a regression test confirms that the device remains registered but unenrolled and that the error identifies the device limit.

`go test ./lib/devicetrust/enroll ./lib/devicetrust/testenv` passes. The CLI package compile check was blocked by missing system headers (`linux/hidraw.h` and `gnu/libc-version.h`).