Task: simplify useMyCountry return value and PhoneInput defaultCountry initialization.
Status: complete.
Changes: hook starts undefined and returns only country; consumers updated; PhoneInput adopts the first non-empty default once while empty.
Verification: PhoneInput and useMyCountry Jest suites passed (15 tests); git diff --check passed.
