Task: simplify useMyCountry return value and PhoneInput default-country adoption.
Status: complete. All requested consumers updated; PhoneInput default adoption covered by tests.
Verification: targeted hook and PhoneInput tests passed (19 tests); PhoneInput rerun passed (16 tests); Prettier check and git diff --check passed. Components check-types blocked by existing OpenPGP type mismatch in packages/crypto/lib/worker/api.ts:579.
