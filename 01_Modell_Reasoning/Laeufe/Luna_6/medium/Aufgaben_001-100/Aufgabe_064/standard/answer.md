Updated `useMyCountry` to return only `string | undefined`, starting as `undefined`. Updated the named consumers and removed country-loading checks while preserving user-settings gates.

`PhoneInput` now starts with no selected country for an empty or missing default, and adopts a late default once without applying later changes. Added tests for these cases.

Verification passed: 2 suites, 15 tests. `git diff --check` is clean.