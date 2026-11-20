# Checkpoint

## Objective
Resolve duplicated storage size definitions by using `@proton/shared/lib/helpers/size` as the authoritative source across the repository.

## Completed
- Added `packages/shared/lib/helpers/size.ts` with `BASE_SIZE`, `sizeUnits` (B/KB/MB/GB/TB), and `SizeUnits`.
- Updated `humanSize.ts` to use and re-export the centralized definitions.
- Migrated user provisioning/editing, organization setup, CSV storage, bonus allocations, offer storage copy, and file-size limits to `sizeUnits`; moved remaining `BASE_SIZE` imports to the helper.
- Removed `GIGA` and `BASE_SIZE` from `shared/lib/constants.ts`; no repository `GIGA` usages remain.

## Verification
- Components CSV suite: passed (64 tests).
- Drive-store encryption suite: passed (10 tests).
- Drive app encryption suite: passed (10 tests).
- Components/shared and app lint checks: passed; Docs Editor reports one pre-existing nested-ternary warning.
- Shared Karma suite bundled successfully but could not launch because Playwright's Chrome binary is absent.
- Shared and components type checks reach an existing OpenPGP type mismatch in `packages/crypto/lib/worker/api.ts`.
- Final diff whitespace check and legacy `GIGA`/inline GB formula scan are clean.
