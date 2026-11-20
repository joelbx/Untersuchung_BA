# Checkpoint

Implemented the mechanism selector in the Drive file saver, added the v1 metric schema and counter registration, and updated `useDownloadMetrics` to record terminal outcomes using stateful `meta.size` or preview `link.size`. Added focused hook and selector tests.

Verification:
- `../../node_modules/.bin/jest --runInBand --coverage=false src/app/store/_downloads/DownloadProvider/useDownloadMetrics.test.ts src/app/store/_downloads/fileSaver/fileSaver.test.ts` from `applications/drive`: exit 0; 2 suites, 20 tests passed.
- `../../node_modules/.bin/tsc --noEmit --pretty false` from `applications/drive`: exit 0.
- `../../node_modules/.bin/tsc --noEmit --pretty false` from `packages/metrics`: exit 0.
- `../../node_modules/.bin/prettier --check` on changed Drive TS files: exit 0.
- `git diff --check`: exit 0.

`rg` was unavailable (`/bin/bash: rg: command not found`); local `find` and `git grep` were used.
