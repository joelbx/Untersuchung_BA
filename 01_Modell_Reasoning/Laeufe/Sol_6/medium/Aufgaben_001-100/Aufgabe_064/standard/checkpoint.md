# Checkpoint

Task: simplify `useMyCountry` to a single country value and update listed consumers; adjust `PhoneInput` default-country initialization.

Status: source edits complete. The hook starts with `undefined`, then uses existing static or API country detection. All listed consumers use the scalar value; user-settings gates remain. PhoneInput starts empty for an absent or empty default, adopts the first later non-empty default only while its country state is empty, and ignores subsequent default changes.

Verification: `useMyCountry.test.ts` and `PhoneInput.test.tsx` passed (19 tests after expanded tests). `git diff --check` passed. `yarn workspace @proton/components check-types` fails in unchanged `packages/crypto/lib/worker/api.ts:579` due to conflicting `openpgp` and `pmcrypto` types.
