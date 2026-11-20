# Checkpoint

Task: Extract reusable payment token verification and update five callers.
Status: Extracted VerifyPayment, getDefaultVerifyPayment, and getCreatePaymentToken. Updated the five named callers plus the single-signup caller found by the account type check. Added token status and fake-timer polling tests.

Checks: packages/components TypeScript check passed (`./node_modules/.bin/tsc --noEmit --pretty false -p packages/components/tsconfig.json`). Initial test command from packages/components using `./node_modules/.bin/jest` failed because that relative executable does not exist; reran with `../../node_modules/.bin/jest`.

Final checks: `./node_modules/.bin/tsc --noEmit --pretty false -p applications/account/tsconfig.json` passed. `../../node_modules/.bin/jest --runInBand --no-coverage --forceExit containers/payments/paymentTokenHelper.test.ts containers/payments/PaymentVerificationModal.test.tsx containers/payments/CreditsModal.test.tsx containers/payments/EditCardModal.test.tsx containers/payments/subscription/SubscriptionModal.spec.tsx` ran 49 tests: 47 passed, 2 failed in CreditsModal.test.tsx. Those two existing assertions expect PaymentMethodID in the buy-credit request, while the existing toTokenPaymentMethod helper returns only Payment; this patch did not change that conversion. `git diff --check` passed.
