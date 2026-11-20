Task: Replace version parsing in specified modules with a shared QVersionNumber helper.
Status: Complete. Added utils.parse_version using QVersionNumber.fromString().normalized(); updated Qt runtime/compiled checks, earlyinit minimum checks, distribution versions, and crash dialog comparison. Updated and added focused tests.
Verification: 345 focused tests passed with xvfb-run and xvfb pytest plugin disabled; remaining version utility tests passed (93 passed, 4 skipped, 1 deselected). The deselected test_unpatched exits in this environment during Chromium user-agent probing. git diff --check passed.
Constraints observed: Local repository only; no git history/index or harness configuration changes.
