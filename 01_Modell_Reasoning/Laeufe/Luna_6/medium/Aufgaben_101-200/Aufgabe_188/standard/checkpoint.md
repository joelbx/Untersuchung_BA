# Checkpoint

Implemented centralized storage units in `packages/shared/lib/helpers/size.ts`, including `BASE_SIZE` and `sizeUnits` (B through TB). `humanSize.ts` now consumes and re-exports those definitions, while legacy constants remain derived/re-exported for compatibility.

Updated member creation/edit/invite, organization setup, CSV import, calendar/contacts import limits, bonus storage constants, offer copy, and referral storage calculations. Updated CSV test expectations to use `sizeUnits.GB`.

Verification: the focused CSV Jest suite passed (64 tests). `git diff --check` passed. The components type check completed with an existing-looking type incompatibility in `packages/crypto/lib/worker/api.ts:579` involving two `openpgp` `PartialConfig` types; no diagnostics referenced changed files.
