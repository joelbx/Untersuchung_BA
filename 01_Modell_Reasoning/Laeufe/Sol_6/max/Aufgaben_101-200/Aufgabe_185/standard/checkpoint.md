# Checkpoint

Task: Correct the subscription cancellation expiry date to use the active term, while preserving renewal and free-plan behavior.

Current state: Updated `subscriptionExpires` with an optional cancellation context. Cancellation and disabled current renewal now use the active term's end and plan name. Legacy and newer cancellation confirmations, the success and reminder modals, and the downgrade flow now source their displayed term end from the utility. Normal scheduled-renewal and free-plan behavior remain covered.

Verification: 76 relevant Jest tests passed across seven suites. Components TypeScript check, Prettier check, ESLint check, and `git diff --check` passed.

Status: Complete. Final working-tree review found only the intended source and test edits.
