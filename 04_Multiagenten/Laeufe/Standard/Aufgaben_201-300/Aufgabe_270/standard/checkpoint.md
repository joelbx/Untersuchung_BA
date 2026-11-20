Task: Fix public-page persisted session selection and initialization.
Status: Complete. Unified lookup returns latest valid session with UID/localID; public session and telemetry callers updated; old LAST_ACTIVE_PING constant references removed. Strict shared storage read enables error reports for malformed data and storage failures.
Verification: 2 focused suites, 12 tests passed; git diff --check passed. Drive type check blocked by existing packages/crypto OpenPGP type mismatch.
Constraints: Local code/tests only; no git history/index/harness changes.
