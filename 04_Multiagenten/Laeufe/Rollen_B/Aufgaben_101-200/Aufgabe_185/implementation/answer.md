Fixed the cancellation expiry display. The expiry utility now accepts an optional cancellation context and uses the active term when cancellation is in progress or auto-renew is disabled. The cancellation modal, confirmation screens, and post-cancellation screen now use that result.

Verification passed: 37 targeted tests, the components TypeScript check, Prettier, and `git diff --check`.