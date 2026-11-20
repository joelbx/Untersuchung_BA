# Checkpoint

Task: Decouple payment token verification into injectable helpers and update payment consumers.

Implemented: `VerifyPayment`, `getDefaultVerifyPayment`, and `getCreatePaymentToken`; chargeable tokens return immediately, pending tokens use injected verification, and terminal initial statuses reject. Migrated all six direct callers, including the additional single-signup caller found by account type checking. The shared approval process now resolves a boolean for chargeable versus closed, canceled, or terminal failure states, clears timers and listeners, and supports configurable polling intervals under fake timers. Modal and PayPal callers translate false into their existing failure or cancellation behavior.

Verification:
- `yarn workspace @proton/components jest containers/payments/paymentTokenHelper.test.ts containers/payments/PaymentVerificationModal.test.tsx containers/payments/CreditsModal.test.tsx --runInBand --no-coverage --silent`: 3 suites, 32 tests passed.
- `yarn workspace @proton/components check-types`: exit 0.
- `yarn workspace proton-account check-types`: exit 0.
- `yarn workspace proton-account jest src/app/signup/PaymentStep.test.tsx --runInBand --no-coverage --silent`: 1 suite, 2 tests passed.
- `node_modules/.bin/eslint` on all changed source and test files with `--quiet`: exit 0.
- `git diff --check`: exit 0.

Tooling fallbacks: `rg` failed with `/bin/bash: rg: command not found`; searches used `git grep`. `yarn eslint ... --quiet` failed with `Usage Error: Couldn't find a script named "eslint"`; the local `node_modules/.bin/eslint` command succeeded. These checks have no remaining uncertainty.

The two CreditsModal saved-method assertions were corrected to match the existing tokenization contract: the purchase request contains a token payment object, while the saved method ID is only used in token creation.
