Task: simplify useMyCountry return value and PhoneInput default-country initialization.
Status: implementation complete. Hook returns string or undefined; all seven consumers updated; PhoneInput adopts one late non-empty default when country is empty.
Verification: PhoneInput and useMyCountry Jest suites pass (15 tests); targeted ESLint and Prettier checks pass; git diff --check passes.
