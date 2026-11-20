# Checkpoint

Task: simplify `useMyCountry` return value and `PhoneInput` default-country initialization; update listed consumers.

Initial inspection: `rg` is unavailable (`/bin/bash: rg: command not found`); using local `find`/`grep` instead.

Verification pending.

Verification:
- `yarn workspace @proton/components test --runInBand --watch=false components/v2/phone/PhoneInput.test.tsx hooks/useMyCountry.test.ts` — passed, 2 suites / 17 tests.
- `yarn prettier --check packages/components/hooks/useMyCountry.tsx packages/components/components/v2/phone/PhoneInput.tsx packages/components/components/v2/phone/PhoneInput.test.tsx applications/account/src/app/containers/securityCheckup/routes/phone/SetPhoneContainer.tsx applications/account/src/app/public/ForgotUsernameContainer.tsx applications/account/src/app/reset/ResetPasswordContainer.tsx applications/account/src/app/signup/SignupContainer.tsx applications/account/src/app/single-signup-v2/mail/CustomStep.tsx applications/mail/src/app/components/onboarding/checklist/messageListPlaceholder/variants/new/UsersOnboardingReplaceAccountPlaceholder.tsx packages/components/containers/recovery/AccountRecoverySection.tsx` — passed.
- `yarn workspace @proton/components check-types --pretty false` — failed with TS2345 at `packages/crypto/lib/worker/api.ts:579`: incompatible `openpgp` vs nested `pmcrypto/node_modules/openpgp` `PartialConfig` types. This appears outside the edited files; full type status remains uncertain.
- After extending the PhoneInput test to cover a temporarily empty country, reran the same focused Jest command: passed, 2 suites / 17 tests. `yarn prettier --check packages/components/components/v2/phone/PhoneInput.test.tsx && git diff --check` also passed.
