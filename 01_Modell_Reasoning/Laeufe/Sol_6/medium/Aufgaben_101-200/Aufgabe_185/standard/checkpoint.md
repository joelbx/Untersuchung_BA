# Checkpoint

Task complete: cancellation expiry now uses the active subscription term.

Implemented: `subscriptionExpires` accepts optional cancellation context and selects the active term when cancellation is active or current auto-renew is disabled. Cancellation confirmation, reminder confirmation, and redirection screens read the date from the utility. Existing renewal and free-plan behavior is preserved. Regression tests cover scheduled future terms and free subscriptions.

Verification: focused utility and modal tests passed (34 tests); cancellation flow tests passed (19 tests); components type check passed; git diff check passed.
