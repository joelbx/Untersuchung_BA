Updated `useMyCountry` to return `string | undefined`, starting at `undefined`, and changed the seven listed consumers to use that value. The user-settings loading gates remain in place.

`PhoneInput` now starts with no selected country when `defaultCountry` is absent or empty. It adopts the first non-empty default once when its internal country is empty, and retains that value for the existing clear behavior.

The existing hook and phone-input test suites passed: 13 tests total. `git diff --check` passed.