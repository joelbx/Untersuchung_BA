# Storage size constants issue

Status: implementation edited and final checks completed.

Changes: added `packages/shared/lib/helpers/size.ts` as the authoritative `BASE_SIZE` and `sizeUnits` source; migrated storage calculations and imports across shared and components. Drive Pro and Drive Business initial allocation now uses `sizeUnits.TB` per requirement.

Verification so far: `packages/components` Jest CSV suite passed (64 tests, 5 snapshots); targeted ESLint exited 0; `git diff --check` exited 0. Prettier initially reported seven files, then `prettier --write` formatted them.

Type-check limitation: both `../../node_modules/.bin/tsc --noEmit --pretty false -p tsconfig.json` in `/app/packages/shared` and `/app/packages/components` exited 2. Both report TS2345 at `../crypto/lib/worker/api.ts(579,77)`: `openpgp` `PartialConfig` is not assignable to the nested `pmcrypto/node_modules/openpgp` `PartialConfig` (`preferredHashAlgorithm`, `hash.md5`). This error is outside changed files; full workspace type correctness remains unverified.

Final checks: Prettier `--check` on all changed source files exited 0; `git diff --check` exited 0; source grep found no remaining `GIGA` or inline `1024 ** 3`/`1024 * 1024 * 1024` expressions in component containers or shared library.

Constraints: offline work only; preserve git history and index baseline. Verification results will be recorded here.
