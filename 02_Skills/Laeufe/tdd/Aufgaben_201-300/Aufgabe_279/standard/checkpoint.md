# Checkpoint

Task: decouple payment token verification from token creation and update five consumers.
Status: inspecting repository; TDD required before production changes.
Tooling: `rg` unavailable (`/bin/bash: rg: command not found`); using local grep/find.

Implementation: injected VerifyPayment; getCreatePaymentToken and getDefaultVerifyPayment; migrated five named consumers plus single signup Step1. Polling uses configurable timer, resolves and cleans up on tab close, terminal status, or abort.
TDD: observed expected red failures for missing getCreatePaymentToken, abort rejection, missing getDefaultVerifyPayment, and consumed status message. Helper tests passed after corresponding changes.
Checks: components TypeScript `tsc --noEmit --pretty false -p packages/components/tsconfig.json` passed before the final consumed-status tweak. Affected tests: helper, EditCardModal, SubscriptionModal passed; CreditsModal.test.tsx has two failures expecting PaymentMethodID in buyCredit payload (unchanged token formatting in baseline). Full components and account suites currently running. Account TypeScript currently running.

Final verification so far:
- `jest containers/payments/paymentTokenHelper.test.ts --runInBand --coverage=false --forceExit`: 10/10 passed.
- Affected components Jest run: helper, EditCardModal, SubscriptionModal passed; CreditsModal failed two named tests: `should create payment token for saved card and then buy credits with it` and `should create payment token for saved paypal and then buy credits with it`. Both expect PaymentMethodID in buyCredit payload; the preexisting token helper returns only `Payment` for a chargeable token.
- `tsc --noEmit --pretty false -p packages/components/tsconfig.json`: passed (prior to final trivial status-message/timer tweak); rerun in progress.
- `tsc --noEmit --pretty false -p applications/account/tsconfig.json`: passed.
- Full account command `timeout 180s /app/node_modules/.bin/jest --coverage --runInBand --ci` in applications/account: 4 suites, 17 tests passed.
- Full components command `timeout 180s /app/node_modules/.bin/jest --coverage --runInBand --ci` in packages/components: timed out (exit 143); before timeout it reported the two CreditsModal failures above and four other passing suites. Full components suite remains unverified.
- `git diff --check`: passed.
Final reruns after all code edits: components TypeScript passed; helper Jest 10/10 passed. The full components suite was attempted but timed out at 180 seconds with the two CreditsModal failures above; no claim of full pass.
