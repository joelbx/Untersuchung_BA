Updated `useMyCountry` to return a country code or `undefined`, and changed all seven consumers to use the single value. PhoneInput now starts with no country for an empty or undefined default and adopts the first eligible country supplied after mount.

The targeted Jest suites pass (15 tests). ESLint, Prettier, and `git diff --check` also pass.