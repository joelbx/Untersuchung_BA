# Checkpoint

Task complete: added `drive_download_mechanism_success_rate_total` schema and counter registration; implemented `selectMechanismForDownload` in the Drive file saver; emitted terminal outcomes from `useDownloadMetrics` with status, retry, and mechanism labels; propagated preview size to reporting; added hook and selector tests.

Verification:
- `yarn workspace proton-drive test:ci src/app/store/_downloads/DownloadProvider/useDownloadMetrics.test.ts src/app/store/_downloads/fileSaver/fileSaver.test.ts --coverage=false` passed (2 suites, 20 tests).
- `yarn workspace proton-drive check-types --pretty false` passed after all edits.
- Prettier check on changed source files and `git diff --check` passed.

An earlier focused Jest run started before the test mock was updated and failed because its old mock lacked the new counter. The rerun above passed.

Navigation note: `rg` was unavailable (`/bin/bash: rg: command not found`); used `find` and `grep`.
