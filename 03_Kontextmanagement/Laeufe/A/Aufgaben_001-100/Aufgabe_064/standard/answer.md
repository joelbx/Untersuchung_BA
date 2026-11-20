Updated `useMyCountry` to return a country code or `undefined`, changed all seven consumers to use the single value, and made `PhoneInput` start empty and adopt a delayed default country once.

The focused tests passed: 17 tests across two suites. The components type check is blocked by an unrelated existing `openpgp` type mismatch in `packages/crypto/lib/worker/api.ts`.