Task: Simplify useMyCountry to return a country code or undefined, update the named consumers, and implement the specified PhoneInput default-country initialization semantics.

Completed:
- useMyCountry now starts at undefined and returns only the country value; its location request remains shared across mounted consumers.
- Updated the seven named consumers to use a single country value. SetPhoneContainer and AccountRecoverySection still gate on their user-settings loading state.
- PhoneInput now starts with an empty country when the prop is absent or empty, accepts the first non-empty default when its internal country is empty, and retains that accepted default for the existing plus-then-clear behavior.

Verification:
- Existing focused suites passed: hooks/useMyCountry.test.ts and components/v2/phone/PhoneInput.test.tsx (13 tests).
- git diff --check passed.
