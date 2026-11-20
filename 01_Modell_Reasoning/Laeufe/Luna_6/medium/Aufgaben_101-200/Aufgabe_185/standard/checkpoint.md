# Checkpoint

Implemented cancellation-aware expiry calculation in `payment.ts`. Cancellation context and disabled auto-renew now select the active subscription term and report expiring/renew-disabled status, current term date, and its plan name. Free subscription output is unchanged. Cancellation flow confirmation date components in both B2C and B2B config now obtain their date through the utility.

Added utility coverage for cancellation context, disabled renewal with a scheduled term, and free-plan behavior. Updated the existing upcoming-term-disabled expectation to active-term expiry, as required.

Verification: `yarn workspace @proton/components test --runInBand containers/payments/subscription/helpers/payment.test.ts` passed (31 tests).
