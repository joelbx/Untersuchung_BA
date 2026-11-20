# Checkpoint

Issue: centralize storage unit definitions in `@proton/shared/lib/helpers/size` and migrate storage calculations.

Status: investigating current definitions, imports, and test coverage before editing code.

Root cause: `humanSize.ts` owns `sizeUnits` but derives it from `BASE_SIZE` in the broad `constants.ts`; `constants.ts` separately exports `GIGA`, and feature code uses both it and literal gigabyte calculations. The new helper must own the base and all units to avoid a circular dependency when `constants.ts` consumes `sizeUnits`.

Hypothesis: moving the base and unit map to `helpers/size.ts`, then migrating callers, will preserve numeric behavior while eliminating duplicate definitions. A focused Jest reproduction was added and executed before the fix: `yarn workspace @proton/components test --runInBand containers/members/multipleUserCreation/sizeUnits.test.ts` failed as expected because the new module does not exist.

Verification: `yarn workspace @proton/components test --runInBand containers/members/multipleUserCreation/sizeUnits.test.ts containers/members/multipleUserCreation/csv.test.ts` passed after the final code edits (65 tests, 5 snapshots). The unit test confirms the base and B/KB/MB/GB/TB values; existing CSV tests confirm parsed storage values and file size limits.

Type check limitation: `yarn workspace @proton/shared check-types` exited 2 at `../crypto/lib/worker/api.ts:579` with TS2345. The `config` argument has incompatible `PartialConfig` types from `/app/node_modules/openpgp/openpgp` and `/app/node_modules/pmcrypto/node_modules/openpgp/openpgp`; the `preferredHashAlgorithm` enums differ. This file and these dependencies are untouched. Shared package type checking remains unverified pending resolution of that dependency mismatch; no downloads were attempted.

`yarn workspace @proton/components check-types` also exited 2 with the same TS2345 in `../crypto/lib/worker/api.ts:579`. This prevents a clean component-wide type check; the error is outside the edited files.

An additional `getInitialStorage` component import test was attempted with the same Jest command above but was interrupted after over a minute because loading the selector's dependency graph consumed substantial memory and produced no result. The extra test was removed; the final test run above passed. The selector's plan branch behavior is supported by source review, not a runtime test.

Final static checks: `git diff --check` succeeded; Prettier check of the new helper and primary edited files succeeded. Repository search found no remaining production `GIGA` references, imports of `BASE_SIZE` from `constants.ts`, or literal `1024 ** 3` calculations under components, shared/lib, or pass. The lone `1024 ** 3` match is the test's independent expected value.

Environment: `rg` is unavailable (`/bin/bash: rg: command not found`); using local `find` and `grep`.
