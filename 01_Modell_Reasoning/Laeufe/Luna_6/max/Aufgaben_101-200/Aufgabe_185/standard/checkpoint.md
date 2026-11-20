# Checkpoint

Task: Fix subscription cancellation expiry dates so cancellation uses the currently active term, while preserving normal renewal and free-plan behavior.

Completed:
- Added an optional boolean cancellation context to `subscriptionExpires`.
- In cancellation context or when either the active or selected upcoming term has renewal disabled, the utility reports expiration of the active term and returns disabled-renewal flags plus the active plan title.
- Preserved upcoming-term behavior when renewal remains enabled and left free-plan results unchanged.
- Routed B2C/B2B cancellation confirmations, the legacy cancellation prompt, and the post-cancellation confirmation date through the utility.
- Updated existing regression assertions for active-term dates and renewal flags.

Validation:
- Focused helper/modal tests: 35 passed.
- Cancellation flow tests: 19 passed.
- `@proton/components` TypeScript check passed.
- Prettier check and `git diff --check` passed.
