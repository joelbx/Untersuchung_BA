Updated `useMyCountry` to return a country code or `undefined`, and changed its callers to consume that single value. The user-settings loading checks remain in place.

`PhoneInput` now starts with no country when `defaultCountry` is empty or undefined. It adopts the first non-empty default that arrives after mount only if its country state is empty, then ignores later default changes.

The relevant Jest suites passed: 16 tests across 2 suites. `git diff --check` also passed.