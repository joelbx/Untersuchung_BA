Updated [PayPalModal.tsx](/app/packages/components/containers/payments/PayPalModal.tsx:48) to save the payment method only when verification returns `true`. Closing, canceling, or failing verification no longer saves the token.

The exact reviewer Jest command passed: 2 suites, 17 tests. `git diff --check` also passed.