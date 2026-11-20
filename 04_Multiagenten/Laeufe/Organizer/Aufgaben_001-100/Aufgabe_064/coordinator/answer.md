Updated [useMyCountry.tsx](/app/packages/components/hooks/useMyCountry.tsx) to start as `undefined` and return only a country code or `undefined`. The listed consumers now use that single value; user-settings loading checks remain in place.

Updated [PhoneInput.tsx](/app/packages/components/components/v2/phone/PhoneInput.tsx) to start with no displayed country when the default is empty or undefined. It adopts the first later non-empty default only if its country is still empty, then ignores later default changes. Added tests for those cases.

The targeted Jest suites passed: **17 tests**. Prettier and `git diff --check` passed. The components type check failed in unchanged `packages/crypto/lib/worker/api.ts` because of conflicting `openpgp` types. No delegation was used.