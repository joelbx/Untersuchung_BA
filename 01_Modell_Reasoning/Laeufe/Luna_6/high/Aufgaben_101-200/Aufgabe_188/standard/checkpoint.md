# Checkpoint

Implemented centralized storage sizing in `packages/shared/lib/helpers/size.ts`. It now owns `BASE_SIZE` and `sizeUnits`; `humanSize` reuses and re-exports `sizeUnits` for compatibility. Migrated member provisioning/editing, organization setup, CSV imports, bonus storage, calendar/contacts size limits, storage offer copy, referral storage, and Drive size constants.

Verification:
- Existing CSV import Jest suite: passed, 64 tests / 5 snapshots.
- ESLint on changed component files: passed.
- ESLint on changed shared files: passed.
- `git diff --check`: passed.
- Components and shared package type checks both stop on the existing unrelated TS2345 error in `packages/crypto/lib/worker/api.ts:579` involving mismatched OpenPGP `PartialConfig` types.
