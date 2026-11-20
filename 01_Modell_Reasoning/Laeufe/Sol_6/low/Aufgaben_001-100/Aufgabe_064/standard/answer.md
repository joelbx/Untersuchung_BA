Updated `useMyCountry` to start as `undefined` and return only a country code or `undefined`. Its consumers now use the single value, while their user settings checks remain in place.

`PhoneInput` now starts with no country when `defaultCountry` is empty or undefined. It adopts the first non-empty default while its country is empty and ignores later default changes during that mount.

The relevant Jest suites passed: 15 tests across `PhoneInput` and `useMyCountry`.