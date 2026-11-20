Implemented cancellation aware expiry calculation in [payment.ts](/app/packages/components/containers/payments/subscription/helpers/payment.ts). Cancellation context or disabled auto-renew now uses the active term’s end date and plan name, with the required expiry and renewal flags. Free plan results and normal scheduled renewal behavior are preserved.

Updated cancellation date displays to use the utility, and adjusted the cancellation modal test to check the active term when a future term exists.

Validation passed: 31 utility tests, 19 cancellation flow tests, 5 cancellation modal tests, and `git diff --check`. Targeted ESLint reported no errors and two test query warnings.