# PassAliases issue checkpoint

Implemented the PassAliases provider hook, helper module, and explicit empty state. Split bridge vault lookup from vault creation and updated the bridge integration example.

Verification executed:

- `node_modules/.bin/jest --runInBand --config packages/components/jest.config.js packages/components/components/drawer/views/SecurityCenter/PassAliases` — 3 suites, 8 tests passed.
- `node_modules/.bin/tsc --noEmit -p packages/components/tsconfig.json` — exit 0.
- `node_modules/.bin/tsc --noEmit -p packages/pass/tsconfig.json` — exit 0.
- `node_modules/.bin/eslint` on changed TypeScript and TSX files with `--quiet` — exit 0.
- `git diff --check` — exit 0.

`rg` was unavailable (`/bin/bash: rg: command not found`); local `find` and `grep` were used. No dependency downloads were needed.
