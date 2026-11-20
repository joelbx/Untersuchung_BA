VERDICT: FIX

**Code defect:** [DeviceDetailHeading.tsx](/app/src/components/views/settings/devices/DeviceDetailHeading.tsx:57) compares the draft with the *displayed* name. When `display_name` is undefined, the displayed name is the device ID; saving that ID closes the editor without persisting it. Compare the draft with the stored `display_name` so this change reaches `saveDeviceName`.

**Tests:** The existing device and session Jest suites passed: 5 suites, 53 tests, 19 snapshots. Exact command and results are recorded in [checkpoint.md](/app/.codex-role-output/checkpoint.md). **TEST_ENVIRONMENT_PROBLEM:** none.