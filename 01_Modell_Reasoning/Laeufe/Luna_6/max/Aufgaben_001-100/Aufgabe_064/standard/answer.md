Implemented the hook API and consumer updates. [useMyCountry.tsx](/app/packages/components/hooks/useMyCountry.tsx) now returns `string | undefined` and starts as `undefined`. The listed consumers use the single value; the settings screens retain their user settings gates.

[PhoneInput.tsx](/app/packages/components/components/v2/phone/PhoneInput.tsx) starts with no selected country when the default is absent or empty. It accepts an initial or late non-empty default once, then ignores later prop changes.

Validation: the two focused suites passed (13 tests), and `git diff --check` passed. The components type check remains blocked by an unrelated OpenPGP type mismatch in `../crypto/lib/worker/api.ts:579`.