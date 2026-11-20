Implemented cancellation-aware expiry calculation in [payment.ts](/app/packages/components/containers/payments/subscription/helpers/payment.ts). Cancellation screens now use the active term’s end date and plan name, while free-plan results and normal upcoming-term behavior are preserved.

Updated cancellation date displays and regression assertions in the cancellation flow and prompt.

Validation passed: 54 focused tests, the `@proton/components` type check, Prettier, and `git diff --check`.