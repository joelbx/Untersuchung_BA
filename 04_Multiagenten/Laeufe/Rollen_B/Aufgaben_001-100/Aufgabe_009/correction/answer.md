Fixed the rename defect: saving the device ID as the name of an unnamed session now calls `saveDeviceName`. Added a regression test covering that save and a subsequent unchanged save.

The five device and session Jest suites pass: 54 tests and 19 snapshots. `git diff --check` passes. No TEST_ENVIRONMENT_PROBLEM.